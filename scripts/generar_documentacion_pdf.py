# Genera el PDF académico de evidencias del proyecto Camila nails.
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem, Preformatted
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'public' / 'documentacion-camila-nails-GA7-220501096-AA5-EV01.pdf'

# Colores y estilos del documento.
ACCENT = colors.HexColor('#c85f5b')
INK = colors.HexColor('#292321')
MUTED = colors.HexColor('#75645d')
SOFT = colors.HexColor('#f7ece7')
LINE = colors.HexColor('#dfcfc7')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyES', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.5, leading=16, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=9))
styles.add(ParagraphStyle(name='CoverKicker', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=ACCENT, alignment=TA_CENTER, spaceAfter=22))
styles.add(ParagraphStyle(name='CoverTitle', parent=styles['Title'], fontName='Helvetica-BoldOblique', fontSize=30, leading=34, textColor=ACCENT, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name='CoverSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=15, leading=21, textColor=INK, alignment=TA_CENTER, spaceAfter=30))
styles.add(ParagraphStyle(name='SectionTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=19, leading=23, textColor=INK, spaceAfter=14, borderPadding=(0, 0, 6, 0), borderColor=ACCENT, borderWidth=0, underlineWidth=0))
styles.add(ParagraphStyle(name='SubTitle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=ACCENT, spaceBefore=10, spaceAfter=7))
styles.add(ParagraphStyle(name='Caption', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=MUTED, alignment=TA_CENTER, spaceBefore=5, spaceAfter=15))
styles.add(ParagraphStyle(name='Small', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name='CodeBlock', parent=styles['Code'], fontName='Courier', fontSize=8.5, leading=12, textColor=colors.HexColor('#fff8f4')))

class NumberedDocTemplate(BaseDocTemplate):
    # Inserta numeración de página en todas las páginas excepto la portada.
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='normal')
        self.addPageTemplates([PageTemplate(id='main', frames=frame, onPage=self.draw_page)])

    def draw_page(self, canvas, doc):
        if doc.page > 1:
            canvas.saveState()
            canvas.setStrokeColor(LINE)
            canvas.line(2.2 * cm, 1.45 * cm, A4[0] - 2.2 * cm, 1.45 * cm)
            canvas.setFont('Helvetica', 8)
            canvas.setFillColor(MUTED)
            canvas.drawRightString(A4[0] - 2.2 * cm, 0.95 * cm, f'Camila nails · GA7-220501096-AA5-EV01 · {doc.page}')
            canvas.restoreState()


def p(text, style='BodyES'):
    return Paragraph(text, styles[style])


def image_evidence(filename, caption, fallback=None):
    # Usa la captura exportada o una imagen real del proyecto como respaldo visual.
    path = ROOT / 'public' / filename
    if not path.exists() and fallback:
        path = ROOT / 'src' / 'assets' / fallback
    if not path.exists():
        return [p(f'Recurso visual no disponible: {filename}', 'Small')]
    image = Image(str(path))
    image._restrictSize(16.8 * cm, 14.5 * cm)
    return [KeepTogether([image, p(caption, 'Caption')])]


def code_evidence(relative_path, caption, max_lines=28):
    # Presenta fragmentos reales del proyecto como evidencia de implementación.
    path = ROOT / relative_path
    if not path.exists():
        return [p(f'Código no disponible: {relative_path}', 'Small')]
    lines = path.read_text(encoding='utf-8').splitlines()[:max_lines]
    content = '\n'.join(f'{index + 1:02d}  {line}' for index, line in enumerate(lines))
    return [p(relative_path, 'SubTitle'), code_block(content), p(caption, 'Caption')]


def code_block(content):
    # Mantiene el código dentro de una caja oscura con contraste suficiente.
    block = Table([[Preformatted(content, styles['CodeBlock'])]], colWidths=[16.8 * cm])
    block.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), INK), ('BOX', (0, 0), (-1, -1), 0.6, ACCENT),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    return block


def build_story():
    story = []
    logo = ROOT / 'src' / 'assets' / 'logo-camila-nails.png.jpeg'

    # Portada.
    story.append(Spacer(1, 2.2 * cm))
    if logo.exists():
        cover_logo = Image(str(logo), width=3.3 * cm, height=3.3 * cm)
        story.append(cover_logo)
        story.append(Spacer(1, 0.55 * cm))
    story.extend([
        p('SERVICIO NACIONAL DE APRENDIZAJE · SENA', 'CoverKicker'),
        p('Camila nails', 'CoverTitle'),
        p('Diseño y desarrollo de servicios web - caso<br/><b>GA7-220501096-AA5-EV01</b>', 'CoverSubtitle'),
    ])
    cover_data = [
        [p('<b>Aprendiz:</b>', 'BodyES'), p('Andrés Mauricio Valencia Arango', 'BodyES')],
        [p('<b>Programa:</b>', 'BodyES'), p('Tecnología en Análisis y Desarrollo de Software', 'BodyES')],
        [p('<b>Ficha:</b>', 'BodyES'), p('3186645', 'BodyES')],
        [p('<b>Instructor:</b>', 'BodyES'), p('Adonay Sánchez', 'BodyES')],
    ]
    table = Table(cover_data, colWidths=[3.1 * cm, 11.6 * cm], hAlign='CENTER')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), SOFT), ('BOX', (0, 0), (-1, -1), 0.6, LINE),
        ('LINEBEFORE', (0, 0), (0, -1), 3, ACCENT), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.extend([table, Spacer(1, 2.0 * cm), p('Pereira, Colombia · 23 de agosto de 2026', 'Small'), PageBreak()])

    # Índice.
    story.extend([p('Índice', 'SectionTitle')])
    toc = [[p('<b>Contenido</b>', 'BodyES'), p('<b>Página</b>', 'BodyES')]]
    for name, page in [('1. Introducción', '3'), ('2. Objetivos', '4'), ('3. Descripción y desarrollo del proyecto', '5'), ('4. Tecnologías y arquitectura', '7'), ('5. Evidencias visuales del proyecto', '8'), ('6. Conclusiones', '11')]:
        toc.append([p(name, 'BodyES'), p(page, 'BodyES')])
    table = Table(toc, colWidths=[14.4 * cm, 1.4 * cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), SOFT), ('BOX', (0, 0), (-1, -1), 0.6, LINE),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, LINE), ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.extend([table, PageBreak()])

    # Introducción.
    story.extend([p('1. Introducción', 'SectionTitle'),
        p('El presente documento describe el diseño y desarrollo de <b>Camila nails</b>, un servicio web creado para presentar los servicios de un estudio de uñas, orientar a sus clientes y facilitar la solicitud de citas. El proyecto responde a la necesidad de contar con una presencia digital clara, atractiva y funcional, donde la información comercial pueda consultarse desde distintos dispositivos.'),
        p('La solución fue construida como una aplicación web moderna con React y Vite. Su interfaz incorpora una identidad visual cálida, navegación por secciones, catálogo de estilos, información sobre esmaltes, guía de enfermedades de las uñas, autenticación de usuarios, perfil personal y un flujo de agendamiento que conecta con WhatsApp.'),
        p('También se implementó una separación de permisos: los clientes consultan el contenido y gestionan su perfil, mientras que el administrador cuenta con herramientas privadas para autorizar cambios y administrar imágenes del catálogo.'), PageBreak()])

    # Objetivos.
    story.extend([p('2. Objetivos', 'SectionTitle'), p('2.1 Objetivo general', 'SubTitle'), p('Diseñar y desarrollar un servicio web para Camila nails que permita presentar sus servicios de manera atractiva, facilitar la interacción con los clientes y ofrecer herramientas de administración de contenidos.'), p('2.2 Objetivos específicos', 'SubTitle')])
    objectives = ['Construir una interfaz responsive, clara y coherente con la identidad visual del emprendimiento.', 'Organizar la información en las secciones de historia, estilos, esmaltes y cuidado de las uñas.', 'Implementar registro e inicio de sesión para controlar el acceso a funciones privadas.', 'Permitir que clientes y administrador actualicen el nombre de su perfil.', 'Restringir las herramientas de edición, aprobación y carga de imágenes al administrador.', 'Facilitar la solicitud de citas mediante un formulario conectado a WhatsApp.']
    story.extend([ListFlowable([ListItem(p(item), leftIndent=12) for item in objectives], bulletType='bullet', leftIndent=18), PageBreak()])

    # Desarrollo funcional.
    story.extend([p('3. Descripción y desarrollo del proyecto', 'SectionTitle'), p('3.1 Interfaz pública', 'SubTitle'), p('La página de inicio presenta la propuesta de valor del estudio, un bloque visual de inspiración, servicios destacados y llamados a la acción. La navegación permite acceder a la historia profesional, estilos de uñas, marcas de esmaltes y guía de enfermedades.'), p('3.2 Autenticación y perfiles', 'SubTitle'), p('El sistema cuenta con registro e inicio de sesión. La sesión conserva los datos básicos del usuario y distingue entre el rol de cliente y el rol de administrador. Cada usuario autenticado dispone de un perfil desde el cual puede cambiar su nombre sin modificar su usuario, correo ni permisos.'), p('3.3 Agendamiento', 'SubTitle'), p('La sección de contacto está protegida para usuarios autenticados. El formulario solicita nombre, teléfono, fecha, hora y notas; luego prepara un mensaje codificado y abre WhatsApp con la información de la reserva.'), p('3.4 Administración', 'SubTitle'), p('El administrador puede acceder al panel privado, revisar propuestas, aprobar o rechazar cambios y subir imágenes para los servicios. Estas opciones no se muestran a los clientes, conservando una experiencia pública limpia y evitando exponer controles de gestión.'), PageBreak()])

    # Arquitectura.
    story.extend([p('4. Tecnologías y arquitectura', 'SectionTitle')])
    tech = [['Frontend', 'React 19, React Router y Vite.'], ['Estilos', 'CSS con variables, diseño responsive, tarjetas, navegación tipo burbuja y tipografías editoriales.'], ['Backend', 'Node.js con Express y endpoints REST para autenticación, perfiles, propuestas y archivos.'], ['Persistencia', 'LowDB con archivo JSON para usuarios, propuestas e imágenes; localStorage como respaldo offline.'], ['Seguridad funcional', 'Rutas protegidas, rol administrativo, contraseñas almacenadas mediante hash y respuestas sin contraseña.'], ['Comunicación', 'Proxy de Vite hacia el servidor local y enlace de reserva mediante WhatsApp.']]
    tech_table = Table([[p(f'<b>{a}</b>', 'BodyES'), p(b, 'BodyES')] for a, b in tech], colWidths=[4.1 * cm, 11.7 * cm])
    tech_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, -1), SOFT), ('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8)]))
    story.extend([tech_table, p('4.1 Estructura principal', 'SubTitle'), code_block('src/\n  App.jsx              Rutas y composición principal\n  AuthProvider.jsx     Estado de autenticación y perfil\n  components/          Barra, lightbox y rutas protegidas\n  pages/               Inicio, catálogo, contacto, login y administración\n  assets/              Logo, fotografías y recursos visuales\nserver/\n  index.js             API Express\n  db.json              Persistencia local'), PageBreak()])

    # Proceso de construcción con fragmentos del código fuente.
    story.extend([p('4.2 Proceso de construcción', 'SubTitle'), p('El servicio se construyó por etapas. Primero se organizó la aplicación React y sus rutas; luego se incorporaron los componentes visuales, la autenticación, el perfil de usuario y finalmente el backend para persistir la información.'), p('Etapa 1 · Estructura de la aplicación', 'SubTitle')])
    story.extend(code_evidence('src/App.jsx', 'Las rutas separan las páginas públicas de las secciones protegidas.', 25))
    story.extend([p('Etapa 2 · Gestión de usuarios', 'SubTitle')])
    story.extend(code_evidence('src/AuthProvider.jsx', 'El proveedor centraliza login, registro, roles y actualización del perfil.', 32))
    story.append(PageBreak())
    story.extend([p('Etapa 3 · Servicios del backend', 'SubTitle')])
    story.extend(code_evidence('server/index.js', 'La API Express recibe las solicitudes de registro, login y actualización del nombre.', 35))
    story.extend([p('Etapa 4 · Resultado visual', 'SubTitle'), p('El resultado combina la lógica anterior con una identidad visual de tonos cálidos, navegación tipo burbuja, catálogo de servicios e imágenes de referencia.')])
    story.extend(image_evidence('evidencia-pagina-inicio.png', 'Figura 5. Captura real de la página principal en funcionamiento.', 'logo-camila-nails.png.jpeg'))
    story.append(PageBreak())

    # Evidencias.
    story.extend([p('5. Impresiones visuales del proyecto', 'SectionTitle'), p('Las siguientes impresiones documentan la interfaz visual implementada, sus recursos gráficos y las principales pantallas del servicio web.')])
    evidences = [
        ('evidencia-inicio.png', 'Figura 1. Identidad visual de Camila nails usada en la página de inicio.', 'logo-camila-nails.png.jpeg'),
        ('evidencia-estilos.png', 'Figura 2. Recursos visuales del catálogo de estilos y servicios de uñas.', 'styles/builder-gel.jpg'),
        ('evidencia-esmaltes.png', 'Figura 3. Identidad visual de la sección de marcas de esmaltes.', 'styles/Esmaltado semipermanente.jpg'),
        ('evidencia-registro.png', 'Figura 4. Logo utilizado en las pantallas de inicio de sesión y registro.', 'logo-camila-nails.png.jpeg'),
    ]
    for filename, caption, fallback in evidences:
        story.extend(image_evidence(filename, caption, fallback))
    story.append(PageBreak())

    # Conclusiones.
    story.extend([p('6. Conclusiones', 'SectionTitle'), p('El desarrollo de Camila nails permitió integrar diseño visual, navegación, autenticación y comunicación con el cliente en un mismo servicio web. La interfaz presenta la marca de forma atractiva y organiza la información para que pueda consultarse con facilidad.'), p('La incorporación de roles mejora la separación entre la experiencia del cliente y las tareas administrativas. De esta manera, los visitantes encuentran una página limpia y los usuarios autenticados pueden acceder a funciones específicas como el agendamiento y la edición de su perfil.'), p('Finalmente, el proyecto demuestra la aplicación práctica de tecnologías actuales para construir una solución escalable. Como trabajo futuro se podrían incorporar autenticación con tokens, una base de datos de producción, confirmaciones automáticas de citas y un editor visual para contenidos.'), Spacer(1, 0.7 * cm), p('Documento elaborado como evidencia del proyecto “Diseño y desarrollo de servicios web - caso. GA7-220501096-AA5-EV01”.', 'Small')])
    return story


# Construye el PDF final en la carpeta public.
doc = NumberedDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=2.2 * cm, leftMargin=2.2 * cm, topMargin=2 * cm, bottomMargin=2 * cm, title='Documentación Camila nails - GA7-220501096-AA5-EV01', author='Andrés Mauricio Valencia Arango')
doc.build(build_story())
print(OUTPUT)
