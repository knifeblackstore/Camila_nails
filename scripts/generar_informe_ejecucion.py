# -*- coding: utf-8 -*-
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, 'SENA - Analisis y Desarrollo de Software (ADSO) | Ficha 3186645', 0, 1, 'C')
        self.set_draw_color(57, 169, 0) # Verde SENA
        self.set_line_width(0.5)
        self.line(10, 18, 200, 18)
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, 'Evidencia GA9-220501096-AA3-EV01 - Pagina ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 13)
        self.set_fill_color(232, 245, 233)
        self.set_text_color(30, 91, 0)
        self.cell(0, 9, '  ' + title, 0, 1, 'L', 1)
        self.ln(3)

    def chapter_subtitle(self, subtitle):
        self.set_font('Arial', 'B', 10.5)
        self.set_text_color(40, 40, 40)
        self.cell(0, 7, subtitle, 0, 1, 'L')
        self.ln(1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 9.5)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.2, body)
        self.ln(3)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# --- PORTADA ---
pdf.add_page()
pdf.set_y(50)
pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(30, 91, 0)
pdf.multi_cell(0, 8, 'EVIDENCIA: GA9-220501096-AA3-EV01\nDocumenta pruebas de software, de acuerdo a la planificacion', align='C')
pdf.ln(15)

pdf.set_font('Arial', '', 12)
pdf.set_text_color(40, 40, 40)
pdf.cell(0, 8, 'Programa: Analisis y Desarrollo de Software (ADSO)', 0, 1, 'C')
pdf.cell(0, 8, 'Ficha de Caracterizacion: 3186645', 0, 1, 'C')
pdf.cell(0, 8, 'Aprendiz / Analista de Calidad: Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.cell(0, 8, 'Instructor Asignado: Adornay Sanchez', 0, 1, 'C')
pdf.ln(10)
pdf.cell(0, 8, 'Proyecto: Sistema de Informacion Web "Camila Nails"', 0, 1, 'C')
pdf.cell(0, 8, 'Componente: Informe de Ejecucion de Pruebas y Enlace de Grabacion', 0, 1, 'C')

# --- INTRODUCCIÓN ---
pdf.add_page()
pdf.chapter_title('1. INTRODUCCION')
pdf.chapter_body('La ejecucion y documentacion de pruebas constituye la etapa practica culminante en el ciclo de aseguramiento de calidad (QA). Esta actividad valida fehacientemente que los modulos programados correspondan a las especificaciones de diseño, verificando que las entradas, salidas y comportamientos del sistema ante contingencias operen conforme a lo planificado.\n\nEl presente informe compila el registro de ejecucion de las pruebas de software efectuadas sobre el proyecto "Camila Nails" (desarrollado con arquitectura desacoplada en React.js, Node.js/Express y base de datos MySQL). Se documentan los resultados obtenidos de quince (15) casos de prueba tecnicos, las metricas de efectividad alcanzadas, el tratamiento de incidencias identificadas y el enlace de acceso a la grabacion audiovisual que respalda la ejecucion en vivo del proceso.')

# --- ENLACE A GRABACIÓN DE VIDEO ---
pdf.chapter_title('2. ENLACE A LA GRABACION AUDIOVISUAL DE PRUEBAS')
pdf.chapter_body('En cumplimiento con el requisito de proporcionar una grabacion de pantalla de la ejecucion de las pruebas, se ha dispuesto el registro audiovisual demostrativo disponible a traves del siguiente enlace seguro:')

pdf.set_fill_color(245, 247, 248)
pdf.set_draw_color(57, 169, 0)
pdf.rect(15, pdf.get_y(), 180, 24, 'DF')
pdf.set_xy(18, pdf.get_y() + 3)
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(30, 91, 0)
pdf.cell(0, 5, 'Enlace de la Grabacion Audiovisual en YouTube (Clic para abrir):', 0, 1)
pdf.set_font('Arial', 'U', 10)
pdf.set_text_color(0, 70, 200)
pdf.set_x(18)
video_url = 'https://youtu.be/LNVPlmUUfMA'
pdf.cell(0, 7, video_url, 0, 1, 'L', link=video_url)
pdf.ln(13)

pdf.set_font('Arial', '', 9.5)
pdf.set_text_color(30, 30, 30)
pdf.chapter_body('Descripcion del video: En la grabacion se exhibe la ejecucion sincrona del servidor Backend (puerto 4000), el Frontend en React (puerto 5173), la ejecucion de peticiones en Postman (POST, GET, PUT, DELETE) y la interaccion fluida en el Panel de Administrador tanto en modo claro como en modo oscuro.')

# --- AMBIENTE DE EJECUCIÓN ---
pdf.chapter_title('3. AMBIENTE TECNOLOGICO DE EJECUCION')
pdf.chapter_body('- Sistema Operativo: Microsoft Windows 11 Home/Pro (x64).\n'
                 '- Backend Runtime: Node.js version 18.x sobre Express.js (http://localhost:4000).\n'
                 '- Base de Datos: MySQL Community Server 8.0 (localhost:3306, Base: camila_nails).\n'
                 '- Frontend Runtime: React.js empaquetado con Vite (http://localhost:5173).\n'
                 '- Herramientas de Prueba Empleadas: Postman v10.x y Google Chrome DevTools.')

# --- MÉTRICAS DE EJECUCIÓN ---
pdf.add_page()
pdf.chapter_title('4. CONSOLIDADO DE METRICAS DE EJECUCION')
pdf.chapter_body('A continuacion se sintetizan los indicadores de cobertura y desempeno obtenidos durante la sesion de pruebas:')

metricas = [
    ("Metrica de Calidad", "Valor Obtenido", "Porcentaje"),
    ("Total de Casos de Prueba Planificados", "15 casos", "100%"),
    ("Total de Casos de Prueba Ejecutados", "15 casos", "100%"),
    ("Casos de Prueba con Resultado Aprobado (Exitosos)", "15 casos", "100%"),
    ("Casos de Prueba Rechazados / Fallidos", "0 casos", "0%"),
    ("Incidencias Detectadas y Resueltas (Bugs)", "1 caso (BUG-UI-01)", "Corregido"),
    ("Tasa de Efectividad del Software", "100% Satisfactorio", "Aprobado")
]

pdf.set_font('Arial', 'B', 9.5)
for i, (m_nom, m_val, m_por) in enumerate(metricas):
    if i == 0:
        pdf.set_fill_color(57, 169, 0)
        pdf.set_text_color(255, 255, 255)
    else:
        pdf.set_fill_color(240, 244, 240) if i % 2 == 0 else 255
        pdf.set_text_color(30, 30, 30)
        pdf.set_font('Arial', '' if i > 0 else 'B', 9)

    pdf.cell(90, 7, '  ' + m_nom, 1, 0, 'L', True)
    pdf.cell(50, 7, m_val, 1, 0, 'C', True)
    pdf.cell(45, 7, m_por, 1, 1, 'C', True)

pdf.ln(5)

# --- FORMATO DE SEGUIMIENTO DE CASOS ---
pdf.chapter_title('5. FORMATO DE SEGUIMIENTO Y REGISTRO DE PRUEBAS EJECUTADAS')
pdf.chapter_body('Detalle del seguimiento caso a caso, especificando el comportamiento obtenido frente a lo planificado:')

autor = "Andres Mauricio Valencia Arango"

casos_ejecutados = [
    ("CP-001: Registro de nuevo cliente", "POST /api/register", "Aprobado", "Respuesta HTTP 200 con registro insertado en MySQL."),
    ("CP-002: Validacion de campos vacios", "POST /api/register", "Aprobado", "HTTP 400 Bad Request retornado, impidiendo registros nulos."),
    ("CP-003: Control de usuario duplicado", "POST /api/register", "Aprobado", "HTTP 409 Conflict retornado por duplicidad de email/username."),
    ("CP-004: Autenticacion de administrador", "POST /api/login", "Aprobado", "Acceso otorgado con status 200 y rol 'admin' validado."),
    ("CP-005: Rechazo de clave incorrecta", "POST /api/login", "Aprobado", "HTTP 401 Unauthorized bloqueando el acceso no autorizado."),
    ("CP-006: Consulta general de usuarios", "GET /api/users", "Aprobado", "Listado JSON retornado con exclusion de passwords por seguridad."),
    ("CP-007: Modificacion de rol de usuario", "PATCH /api/users/:id/role", "Aprobado", "Cambio de rol de cliente a administrador reflejado en DB."),
    ("CP-008: Edicion de perfil de usuario", "PUT /api/users/:id", "Aprobado", "Actualizacion exitosa de nombre y correo en MySQL."),
    ("CP-009: Eliminacion fisica de usuario", "DELETE /api/users/:id", "Aprobado", "Registro eliminado permanentemente con confirmacion previa."),
    ("CP-010: Creacion manual de Ficha", "POST /api/fichas", "Aprobado", "Insercion exitosa con ID generado y visualizada en UI."),
    ("CP-011: Listado historico de Fichas", "GET /api/fichas", "Aprobado", "Arreglo completo de registros clinicos retornado con status 200."),
    ("CP-012: Actualizacion de Ficha Clinica", "PUT /api/fichas/:id", "Aprobado", "Modificacion de servicio y telefono confirmada con status 200."),
    ("CP-013: Eliminacion de Ficha Clinica", "DELETE /api/fichas/:id", "Aprobado", "Registro removido de la tabla 'fichas' satisfactoriamente."),
    ("CP-014: Visibilidad en Modo Oscuro", "Chrome DevTools", "Aprobado (BUG-UI-01)", "Fondo blanco en focus corregido; contraste optimo garantizado."),
    ("CP-015: Adaptabilidad responsiva movil", "Chrome DevTools", "Aprobado", "Visualizacion fluida de borde a borde en pantallas de 360-412px.")
]

for cp_id, cp_acc, cp_res, cp_det in casos_ejecutados:
    pdf.set_font('Arial', 'B', 9)
    pdf.set_text_color(30, 91, 0)
    pdf.cell(75, 6, cp_id, 0, 0, 'L')
    pdf.set_font('Arial', 'I', 8.5)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(50, 6, f'Metodo: {cp_acc}', 0, 0, 'L')
    pdf.set_font('Arial', 'B', 8.5)
    pdf.set_text_color(27, 94, 32)
    pdf.cell(0, 6, f'[{cp_res}]', 0, 1, 'R')
    
    pdf.set_font('Arial', '', 8.5)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 4.5, f'Resultado: {cp_det} | Analista: {autor}')
    pdf.ln(1)

# --- GESTIÓN DE INCIDENCIAS ---
pdf.add_page()
pdf.chapter_title('6. TRATAMIENTO DE INCIDENCIAS Y LECCIONES APRENDIDAS')
pdf.chapter_body('Durante la fase de evaluacion visual se identifico la siguiente anomalia funcional/visual:\n\n'
                 '- Codigo de Incidencia: BUG-UI-01.\n'
                 '- Severidad: Media.\n'
                 '- Descripcion de la falla: En los campos de formulario del panel de administracion en tema oscuro, al interactuar (focus) sobre el campo, el CSS forzaba una propiedad "background: rgba(255,255,255,0.9)", provocando que el texto blanco se mimetizara con el fondo claro y quedara ilegible.\n'
                 '- Accion Correctiva Aplicada: Se retiro la regla fija en src/App.css, asignando el color de superficie semitransparente del tema oscuro y preservando el borde de acento luminiscente. La re-evaluacion confirmo resolucion al 100%.\n\n'
                 '- Anomalia de Visualizacion: El ancho fijo de 1126px en el contenedor raiz generaba marcos negros vacios en monitores de alta resolucion y desbordamientos en pantallas moviles estrechas. Se resolvio modificando src/index.css a un esquema fluido de ancho completo (100%) con padding elastico.')

# --- CONCLUSIONES ---
pdf.chapter_title('7. CONCLUSIONES')
pdf.chapter_body('1. La ejecucion metódica del plan de pruebas sobre la totalidad de los 15 casos demostro la solidez técnica y operativa del software "Camila Nails", alcanzando una tasa de efectividad del 100% en las funciones criticas de negocio.\n\n'
                 '2. La integracion del backend en Node.js/Express con la base de datos relacional MySQL responde de manera segura ante escenarios de datos incompletos o accesos no autorizados mediante codigos de estado HTTP estandarizados (400, 401, 409).\n\n'
                 '3. El registro audiovisual complementario y los formatos diligenciados aportan evidencia comprobable de que el software se encuentra listo para su pase a produccion o despliegue en la nube.')

pdf.ln(12)
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 6, '_____________________________________________', 0, 1, 'C')
pdf.cell(0, 6, 'Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.set_font('Arial', '', 10)
pdf.cell(0, 5, 'Aprendiz / Analista de Calidad de Software', 0, 1, 'C')
pdf.cell(0, 5, 'Ficha 3186645 - ADSO SENA', 0, 1, 'C')

pdf_path = 'Evidencia_GA9-220501096-AA3-EV01_InformeEjecucionPruebas.pdf'
pdf.output(pdf_path, 'F')
print(f"Informe de ejecucion generado exitosamente: {pdf_path}")
