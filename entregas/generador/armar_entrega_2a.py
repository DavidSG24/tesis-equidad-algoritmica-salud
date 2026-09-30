# -*- coding: utf-8 -*-
"""Construye la entrega 1B sobre una copia de la plantilla institucional INFOTEC.

Estrategia: se conserva intacto el andamiaje de la plantilla (portada con cajas
de texto, secciones, encabezados, pies, campo de indice general, saltos de
pagina y de seccion) y se sustituye unicamente el texto de relleno, clonando
los parrafos modelo de la propia plantilla para heredar su tipografia.
"""
import copy
import shutil
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import Cm, Pt
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.path.insert(0, str(Path(__file__).parent))
import contenido_2a as C

BASE = Path("/Users/davidsegundogarcia/Documents")
PLANTILLA = BASE / "plantilla infotec/Plantilla Tesis MCDI_ProyectoTerminal.docx"
FIGDIR = BASE / "tesis"
DESTDIR = BASE / "entregas"
DEST = DESTDIR / "2A_Marco_metodologico_David_Segundo.docx"
V1 = DESTDIR / "1B_Marco_teorico_y_antecedentes_David_Segundo_v1_prerevision.docx"

# Indices (base 0) de los parrafos modelo de la plantilla, usados como molde.
M_H2 = 175      # "1.1 Planteamiento del problema"  -> Normal (Web), Arial 14 negrita
M_H3 = 181      # "1.1.1 ..."                        -> Heading 3
M_BODY = 176    # cuerpo justificado, Arial 12, 1.5
M_CENTER = 188  # parrafo centrado (contenia una imagen de relleno)
M_PORTADILLA = 167  # "Generalidades" -> Arial 26 negrita, derecha

# ---------------------------------------------------------------------------
#  Resaltado de cambios
#  La entrega 2A debe senalar en amarillo lo que cambio respecto de la version
#  que reviso el asesor. En lugar de marcarlo a mano, se compara cada parrafo
#  contra el texto de esa version: lo que no aparece ahi, se resalta.
# ---------------------------------------------------------------------------
def _norm(t):
    return " ".join(t.replace("**", "").split()).strip()


_PREVIO = set()
if V1.exists():
    _doc_v1 = Document(str(V1))
    for _p in _doc_v1.paragraphs:
        if _p.text.strip():
            _PREVIO.add(_norm(_p.text))
    for _t in _doc_v1.tables:
        for _fila in _t.rows:
            for _c in _fila.cells:
                if _c.text.strip():
                    _PREVIO.add(_norm(_c.text))


def es_nuevo(texto):
    """True si el texto no estaba en la version revisada por el asesor."""
    return bool(_PREVIO) and _norm(texto) not in _PREVIO


DESTDIR.mkdir(exist_ok=True)
shutil.copy2(PLANTILLA, DEST)
doc = Document(str(DEST))
PARAS = list(doc.paragraphs)          # instantanea con los indices originales
BODY = doc.element.body
TABLE_STYLE = doc.tables[0].style


# ---------------------------------------------------------------------------
#  Utilidades de construccion de parrafos
# ---------------------------------------------------------------------------
def _blank_clone(model_idx):
    """Clona un parrafo modelo y devuelve (elemento, Paragraph) sin runs."""
    el = copy.deepcopy(PARAS[model_idx]._p)
    for child in list(el):
        if child.tag in (qn('w:r'), qn('w:hyperlink'), qn('w:bookmarkStart'),
                         qn('w:bookmarkEnd'), qn('w:proofErr')):
            el.remove(child)
    return el, Paragraph(el, doc)


def _add_marked_text(par, text, size=None, italic=False, resaltar=False):
    """Anade runs a partir de un texto con marcado **negrita**."""
    model_run = None
    for i, chunk in enumerate(text.split("**")):
        if not chunk:
            continue
        run = par.add_run(chunk)
        run.bold = (i % 2 == 1)
        run.font.name = "Arial"
        if size is not None:
            run.font.size = Pt(size)
        if italic:
            run.italic = True
        if resaltar:
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW
        model_run = run
    if model_run is None:                      # texto vacio
        run = par.add_run("")
        run.font.name = "Arial"
    return par


def _set_outline_level(el, level):
    """Fija el nivel de esquema para que el indice automatico recoja el titulo."""
    pPr = el.find(qn('w:pPr'))
    if pPr is None:
        pPr = OxmlElement('w:pPr')
        el.insert(0, pPr)
    for old in pPr.findall(qn('w:outlineLvl')):
        pPr.remove(old)
    lvl = OxmlElement('w:outlineLvl')
    lvl.set(qn('w:val'), str(level))
    pPr.append(lvl)


def p_body(text, size=12):
    el, par = _blank_clone(M_BODY)
    _add_marked_text(par, text, size, resaltar=es_nuevo(text))
    return [el]


def p_h2(text):
    el, par = _blank_clone(M_H2)
    _add_marked_text(par, text, 14, resaltar=es_nuevo(text))
    for r in par.runs:
        r.bold = True
    _set_outline_level(el, 1)
    par.paragraph_format.space_before = Pt(18)
    par.paragraph_format.space_after = Pt(6)
    return [el]


def p_h3(text):
    el, par = _blank_clone(M_H3)
    _add_marked_text(par, text, resaltar=es_nuevo(text))
    for r in par.runs:
        r.bold = True
        r.font.size = Pt(12.5)
    par.paragraph_format.space_before = Pt(12)
    par.paragraph_format.space_after = Pt(4)
    return [el]


def p_bullet(text):
    el, par = _blank_clone(M_BODY)
    _add_marked_text(par, "•  " + text, 12, resaltar=es_nuevo("•  " + text))
    pf = par.paragraph_format
    pf.left_indent = Cm(1.0)
    pf.first_line_indent = Cm(-0.55)
    pf.space_after = Pt(4)
    return [el]


def p_nota(text):
    el, par = _blank_clone(M_BODY)
    _add_marked_text(par, text, 11, italic=True, resaltar=es_nuevo(text))
    pf = par.paragraph_format
    pf.left_indent = Cm(0.9)
    pf.right_indent = Cm(0.9)
    pf.space_before = Pt(8)
    pf.space_after = Pt(8)
    return [el]


def p_blank():
    el, par = _blank_clone(M_BODY)
    par.add_run("")
    return [el]


def p_caption(text, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=8):
    el, par = _blank_clone(M_BODY)
    _add_marked_text(par, text, 10, resaltar=es_nuevo(text))
    par.style = doc.styles["Caption"]
    pf = par.paragraph_format
    pf.alignment = align
    pf.line_spacing = 1.0
    pf.left_indent = None
    pf.first_line_indent = None
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    for r in par.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10)
    return [el]


def p_ref(text):
    """Referencia bibliografica con sangria francesa (APA)."""
    el, par = _blank_clone(M_BODY)
    _add_marked_text(par, text, 12)
    pf = par.paragraph_format
    pf.left_indent = Cm(1.25)
    pf.first_line_indent = Cm(-1.25)
    pf.line_spacing = 1.5
    pf.space_after = Pt(10)
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return [el]


_BM_ID = [1000]


def _marcar(el, nombre):
    """Envuelve el parrafo en un marcador, referenciable desde los indices."""
    _BM_ID[0] += 1
    start = OxmlElement('w:bookmarkStart')
    start.set(qn('w:id'), str(_BM_ID[0]))
    start.set(qn('w:name'), nombre)
    end = OxmlElement('w:bookmarkEnd')
    end.set(qn('w:id'), str(_BM_ID[0]))
    pPr = el.find(qn('w:pPr'))
    if pPr is not None:
        pPr.addnext(start)
    else:
        el.insert(0, start)
    el.append(end)


def _campo_pageref(par, nombre):
    """Inserta un campo PAGEREF; Word lo resuelve al actualizar los campos."""
    el = par._p
    piezas = [
        ('fldChar', 'begin', None),
        ('instrText', None, f' PAGEREF {nombre} \\h '),
        ('fldChar', 'separate', None),
        ('text', None, '1'),
        ('fldChar', 'end', None),
    ]
    for tipo, tipo_char, texto in piezas:
        r = OxmlElement('w:r')
        rPr = OxmlElement('w:rPr')
        fonts = OxmlElement('w:rFonts')
        fonts.set(qn('w:ascii'), 'Arial')
        fonts.set(qn('w:hAnsi'), 'Arial')
        rPr.append(fonts)
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), '22')
        rPr.append(sz)
        r.append(rPr)
        if tipo == 'fldChar':
            fc = OxmlElement('w:fldChar')
            fc.set(qn('w:fldCharType'), tipo_char)
            r.append(fc)
        elif tipo == 'instrText':
            it = OxmlElement('w:instrText')
            it.set(qn('xml:space'), 'preserve')
            it.text = texto
            r.append(it)
        else:
            t = OxmlElement('w:t')
            t.text = texto
            r.append(t)
        el.append(r)


def p_entrada_indice(texto, bookmark):
    """Entrada de indice de figuras o tablas, con puntos de relleno y pagina."""
    el, par = _blank_clone(M_BODY)
    pf = par.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf.line_spacing = 1.15
    pf.space_after = Pt(8)
    pf.left_indent = Cm(0.9)
    pf.first_line_indent = Cm(-0.9)
    pPr = el.find(qn('w:pPr'))
    tabs = OxmlElement('w:tabs')
    tab = OxmlElement('w:tab')
    tab.set(qn('w:val'), 'right')
    tab.set(qn('w:leader'), 'dot')
    tab.set(qn('w:pos'), '9355')
    tabs.append(tab)
    pPr.append(tabs)
    run = par.add_run(texto)
    run.font.name = "Arial"
    run.font.size = Pt(11)
    run.add_tab()
    _campo_pageref(par, bookmark)
    return [el]


def p_figure(ruta, pie, numero):
    """Devuelve [parrafo con imagen, pie de figura]."""
    el, par = _blank_clone(M_CENTER)
    par.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_before = Pt(10)
    par.paragraph_format.space_after = Pt(2)
    par.add_run().add_picture(str(FIGDIR / ruta), width=Cm(15.5))
    pie_el = p_caption(f"Figura {numero}. {pie}")
    _marcar(pie_el[0], f"_Fig{numero}")
    return [el] + pie_el


def p_table(pie, filas, numero):
    """Devuelve [titulo de tabla, tabla, espacio]."""
    titulo = p_caption(f"Tabla {numero}. {pie}",
                       align=WD_ALIGN_PARAGRAPH.LEFT, space_before=12, space_after=4)
    _marcar(titulo[0], f"_Tab{numero}")
    ncols = len(filas[0])
    tabla = doc.add_table(rows=len(filas), cols=ncols)
    tabla.style = TABLE_STYLE
    tabla.autofit = True
    # la fila de encabezado se repite si la tabla se parte entre paginas
    trPr = tabla.rows[0]._tr.get_or_add_trPr()
    trPr.append(OxmlElement('w:tblHeader'))
    for i, fila in enumerate(filas):
        for j, celda in enumerate(fila):
            cell = tabla.cell(i, j)
            cell.text = ""
            par = cell.paragraphs[0]
            pf = par.paragraph_format
            pf.space_before = Pt(2)
            pf.space_after = Pt(2)
            pf.line_spacing = 1.0
            pf.alignment = (WD_ALIGN_PARAGRAPH.CENTER if i == 0
                            else WD_ALIGN_PARAGRAPH.LEFT)
            run = par.add_run(celda)
            run.font.name = "Arial"
            run.font.size = Pt(9.5)
            run.bold = (i == 0)
    tbl_el = tabla._tbl
    tbl_el.getparent().remove(tbl_el)          # se saca del final del documento
    espacio = p_blank()
    return titulo + [tbl_el] + espacio


# ---------------------------------------------------------------------------
#  Numeracion de figuras y tablas en orden documental
# ---------------------------------------------------------------------------
def numerar(bloques, estado):
    """Anade el numero correlativo a los bloques 'fig' y 'tab'."""
    salida = []
    for blk in bloques:
        if blk[0] == 'fig':
            estado['fig'] += 1
            estado['lista_fig'].append((estado['fig'], blk[2]))
            salida.append(('fig', blk[1], blk[2], estado['fig']))
        elif blk[0] == 'tab':
            estado['tab'] += 1
            estado['lista_tab'].append((estado['tab'], blk[1]))
            salida.append(('tab', blk[1], blk[2], estado['tab']))
        else:
            salida.append(blk)
    return salida


ESTADO = {'fig': 0, 'tab': 0, 'lista_fig': [], 'lista_tab': []}
CAP1_N = numerar(C.CAP1, ESTADO)          # Capitulo 1. Introduccion
MARCO_N = numerar(C.CAP_MARCO, ESTADO)    # Capitulo 2. Marco teorico
METODO_N = numerar(C.CAP_METODO, ESTADO)  # Capitulo 3. Metodologia
ANEXO_N = numerar(C.ANEXO, ESTADO)


def render(bloques):
    """Traduce una lista de bloques a elementos XML."""
    out = []
    for blk in bloques:
        kind = blk[0]
        if kind == 'p':
            out += p_body(blk[1])
        elif kind == 'h2':
            out += p_h2(blk[1])
        elif kind == 'h3':
            out += p_h3(blk[1])
        elif kind == 'b':
            out += p_bullet(blk[1])
        elif kind == 'nota':
            out += p_nota(blk[1])
        elif kind == 'blank':
            out += p_blank()
        elif kind == 'fig':
            out += p_figure(blk[1], blk[2], blk[3])
        elif kind == 'tab':
            out += p_table(blk[1], blk[2], blk[3])
        else:
            raise ValueError(f"bloque desconocido: {kind}")
    return out


# ---------------------------------------------------------------------------
#  Sustitucion de regiones
# ---------------------------------------------------------------------------
def reemplazar(start, end, elementos):
    """Sustituye los parrafos originales [start, end] por los elementos dados."""
    prev = PARAS[start]._p
    for el in elementos:
        prev.addnext(el)
        prev = el
    for i in range(start, end + 1):
        el = PARAS[i]._p
        parent = el.getparent()
        if parent is not None:
            parent.remove(el)


def set_texto(idx, texto, size=None):
    """Reescribe el texto de un parrafo conservando el formato de su primer run."""
    par = PARAS[idx]
    if not par.runs:
        run = par.add_run(texto)
        run.font.name = "Arial"
        if size:
            run.font.size = Pt(size)
        return
    par.runs[0].text = texto
    if size:
        par.runs[0].font.size = Pt(size)
    for r in par.runs[1:]:
        r.text = ""


# --- se procesa de atras hacia adelante para no invalidar los indices --------

# Anexo 1
set_texto(303, "ANEXO 1")
set_texto(304, C.ANEXO_TITULO)
reemplazar(305, 317, render(ANEXO_N))

# Fuentes de consulta
refs = p_blank()
for r in C.REFERENCIAS:
    refs += p_ref(r)
reemplazar(285, 295, refs)

# Conclusiones y recomendaciones
set_texto(283, "")
reemplazar(279, 282, render(C.CONCLUSIONES))

# Capitulo 3 -> Marco metodologico
reemplazar(247, 272, p_blank() + render(METODO_N))
set_texto(246, "Capítulo 3. Marco metodológico")
set_texto(245, "Marco metodológico")

# Capitulo 2 -> Marco teorico
reemplazar(206, 238, p_blank() + render(MARCO_N))
set_texto(205, "Capítulo 2. Marco teórico y trabajos relacionados")
set_texto(203, "Marco teórico")

# Capitulo 1 -> Introduccion
reemplazar(169, 198, p_blank() + render(CAP1_N))   # el 198 es relleno vacio y dejaba una hoja suelta
set_texto(168, "Capítulo 1. Introducción")
set_texto(167, "Introducción")

# Hoja preliminar: la plantilla la titula "Introduccion", pero el capitulo 1
# ya lo es; se retitula para no duplicar el encabezado.
reemplazar(158, 161, p_blank() + render(C.PRESENTACION))
set_texto(157, "Presentación")

# Resumen
reemplazar(152, 155, render(C.RESUMEN))

# Glosario
glos = []
for letra, entradas in C.GLOSARIO:
    el, par = _blank_clone(M_BODY)
    _add_marked_text(par, f"“{letra}”", 12)
    for r in par.runs:
        r.bold = True
    par.paragraph_format.space_before = Pt(10)
    par.paragraph_format.space_after = Pt(4)
    glos.append(el)
    for entrada in entradas:
        glos += p_body(entrada)
reemplazar(140, 148, glos)

# Abreviaturas y acronimos: se rellena la tabla existente
tabla_abrev = doc.tables[0]
while len(tabla_abrev.rows) > 1:
    tr = tabla_abrev.rows[-1]._tr
    tr.getparent().remove(tr)
for i, (sigla, desc) in enumerate(C.ABREVIATURAS):
    row = tabla_abrev.rows[0] if i == 0 else tabla_abrev.add_row()
    for j, txt in enumerate((sigla, desc)):
        cell = row.cells[j]
        cell.text = ""
        par = cell.paragraphs[0]
        par.paragraph_format.space_before = Pt(2)
        par.paragraph_format.space_after = Pt(2)
        par.paragraph_format.line_spacing = 1.0
        run = par.add_run(txt)
        run.font.name = "Arial"
        run.font.size = Pt(10)
        run.bold = (i == 0)
reemplazar(118, 137, [])

# Indice de tablas
idx_tab = p_blank()
for num, pie in ESTADO['lista_tab']:
    idx_tab += p_entrada_indice(f"Tabla {num}. {pie}", f"_Tab{num}")
reemplazar(89, 114, idx_tab)

# Indice de figuras
idx_fig = p_blank()
for num, pie in ESTADO['lista_fig']:
    idx_fig += p_entrada_indice(f"Figura {num}. {pie}", f"_Fig{num}")
reemplazar(61, 86, idx_fig)


# ---------------------------------------------------------------------------
#  Portada (cajas de texto)
# ---------------------------------------------------------------------------
A_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
WP_NS = "{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}"
V_NS = "{urn:schemas-microsoft-com:vml}"


def _set_sz(rPr, half_points):
    for tag in ('w:sz', 'w:szCs'):
        for old in rPr.findall(qn(tag)):
            rPr.remove(old)
        el = OxmlElement(tag)
        el.set(qn('w:val'), str(half_points))
        rPr.append(el)


def _titulo_en_run(t_el, principal, subtitulo):
    """Escribe titulo y subtitulo con dos tamanos dentro de la caja de texto."""
    r = t_el.getparent()
    rPr = r.find(qn('w:rPr'))
    if rPr is None:
        rPr = OxmlElement('w:rPr')
        r.insert(0, rPr)
    _set_sz(rPr, 36)                       # 18 pt para el titulo
    t_el.text = principal
    t_el.set(qn('xml:space'), 'preserve')

    r2 = copy.deepcopy(r)
    for child in list(r2):
        if child.tag != qn('w:rPr'):
            r2.remove(child)
    _set_sz(r2.find(qn('w:rPr')), 24)      # 12 pt para el subtitulo
    for _ in range(2):
        r2.append(OxmlElement('w:br'))
    t2 = OxmlElement('w:t')
    t2.text = subtitulo
    t2.set(qn('xml:space'), 'preserve')
    r2.append(t2)
    r.addnext(r2)


def rellenar_portada():
    p = PARAS[1]._p

    # La caja del titulo se agranda: el titulo real ocupa mas que el marcador.
    for ext in p.iter(A_NS + "ext"):
        if ext.get("cy") == "915120":
            ext.set("cy", "2160000")
    for ext in p.iter(WP_NS + "extent"):
        if ext.get("cy") == "915670":
            ext.set("cy", "2160000")
    # La caja de lugar y fecha se ensancha: "agosto, 2026." no cabe en una linea.
    for ext in p.iter(A_NS + "ext"):
        if ext.get("cy") == "356760":
            ext.set("cx", "2750000")
    for ext in p.iter(WP_NS + "extent"):
        if ext.get("cy") == "357505":
            ext.set("cx", "2750000")
    for shape in list(p.iter(V_NS + "rect")) + list(p.iter(V_NS + "shape")):
        estilo = shape.get("style") or ""
        if "height:72pt" in estilo:
            shape.set("style", estilo.replace("height:72pt", "height:170pt"))

    objetivos = list(p.iter(qn('w:t')))
    nombres = 0
    for t in objetivos:
        txt = (t.text or "").strip()
        if txt.endswith("NOMBRE DEL PROYECTO”"):
            _titulo_en_run(t, C.PORTADA["titulo"], C.PORTADA["subtitulo"])
        elif txt == "“":
            t.text = ""
        elif txt == "(TIPO DE PROYECTO)":
            t.text = C.PORTADA["tipo"]
        elif txt == "(Nombre y Apellidos)":
            t.text = (C.PORTADA["alumno"] if nombres % 2 == 0
                      else C.PORTADA["asesor"])
            nombres += 1
        elif txt == "mes, año.":
            t.text = C.PORTADA["fecha"]
            rPr = t.getparent().find(qn('w:rPr'))
            if rPr is not None:
                for u in rPr.findall(qn('w:u')):      # el marcador iba subrayado
                    rPr.remove(u)


rellenar_portada()


# ---------------------------------------------------------------------------
#  Numeracion de paginas: la plantilla reinicia en romanos las secciones
#  finales (fuentes de consulta y anexos). Se elimina para que la numeracion
#  arabiga sea continua desde la introduccion hasta el final.
# ---------------------------------------------------------------------------
#  Se conserva el reinicio en romanos de las preliminares (seccion 2) y el
#  arranque de la numeracion arabiga en la introduccion (seccion 3); se
#  eliminan los reinicios intermedios, calibrados para el texto de relleno.
for i, sec in enumerate(doc.sections):
    if i in (0, 1, 2, 3):
        continue
    pn = sec._sectPr.find(qn('w:pgNumType'))
    if pn is not None:
        sec._sectPr.remove(pn)

#  Las secciones 8 y 9 solo contienen un parrafo vacio de relleno cada una y
#  producian dos paginas en blanco entre los capitulos 2 y 3; se vuelven
#  continuas. OJO: el w:type describe como ARRANCA su propia seccion, de modo
#  que tocar la 7 eliminaria el salto que separa la portadilla del capitulo 2
#  del cuerpo del capitulo.
for i in (8, 9):
    sectPr = doc.sections[i]._sectPr
    for old in sectPr.findall(qn('w:type')):
        sectPr.remove(old)
    tipo = OxmlElement('w:type')
    tipo.set(qn('w:val'), 'continuous')
    sectPr.insert(0, tipo)

doc.save(str(DEST))
print("OK ->", DEST)
print("figuras:", ESTADO['lista_fig'])
print("tablas:", [n for n, _ in ESTADO['lista_tab']])
