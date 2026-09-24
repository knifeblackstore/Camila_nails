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
        self.cell(0, 10, 'Evidencia GA9-220501096-AA2-EV01 - Pagina ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 13)
        self.set_fill_color(232, 245, 233)
        self.set_text_color(30, 91, 0)
        self.cell(0, 9, '  ' + title, 0, 1, 'L', 1)
        self.ln(3)

    def chapter_subtitle(self, subtitle):
        self.set_font('Arial', 'B', 11)
        self.set_text_color(40, 40, 40)
        self.cell(0, 7, subtitle, 0, 1, 'L')
        self.ln(1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, body)
        self.ln(3)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# --- PORTADA ---
pdf.add_page()
pdf.set_y(50)
pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(30, 91, 0)
pdf.multi_cell(0, 8, 'EVIDENCIA: GA9-220501096-AA2-EV01\nDisena casos y define el ambiente de pruebas de software segun proyecto', align='C')
pdf.ln(15)

pdf.set_font('Arial', '', 12)
pdf.set_text_color(40, 40, 40)
pdf.cell(0, 8, 'Programa: Analisis y Desarrollo de Software (ADSO)', 0, 1, 'C')
pdf.cell(0, 8, 'Ficha de Caracterizacion: 3186645', 0, 1, 'C')
pdf.cell(0, 8, 'Aprendiz / Analista: Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.cell(0, 8, 'Instructor: Adornay Sanchez', 0, 1, 'C')
pdf.ln(10)
pdf.cell(0, 8, 'Proyecto: Sistema de Gestion Web "Camila Nails"', 0, 1, 'C')
pdf.cell(0, 8, 'Formato principal entregable: Libro de Calculo Excel (.xlsx)', 0, 1, 'C')

# --- INTRODUCCIÓN ---
pdf.add_page()
pdf.chapter_title('1. INTRODUCCION')
pdf.chapter_body('El diseno de casos de prueba y la configuracion precisa del ambiente de pruebas representan actividades fundamentales en el aseguramiento de la calidad del software (QA). Un caso de prueba bien formulado establece las condiciones bajo las cuales un evaluador puede determinar si una aplicacion o modulo cumple con los requerimientos tecnicos y funcionales esperados.\n\nEl presente informe compila la definicion formal del ambiente de pruebas utilizado para el proyecto "Camila Nails" y detalla la matriz de casos de prueba ejecutada sobre los modulos de autenticacion, administracion de usuarios, creacion y mantenimiento de fichas clinicas, asi como la adaptabilidad de la interfaz de usuario en entornos moviles y modo oscuro. Todo el diseno cumple rigurosamente con los campos exigidos por la guia de aprendizaje y las normas de presentacion SENA.')

# --- AMBIENTE DE PRUEBAS ---
pdf.chapter_title('2. DEFINICION DEL AMBIENTE DE PRUEBAS')
pdf.chapter_body('Para asegurar que las pruebas reflejen condiciones reales y confiables de operacion, se establecio el siguiente ambiente de trabajo de hardware y software:\n\n'
                 'a) Entorno de Hardware: Equipo portatil / estacion de trabajo con procesador multinucleo de 64 bits, 8 GB de memoria RAM y conexion de red local.\n\n'
                 'b) Servidor Backend: Entorno de ejecucion Node.js (version 18+) configurado con el framework Express.js, escuchando en el puerto local 4000 (http://localhost:4000).\n\n'
                 'c) Motor de Base de Datos: MySQL Community Server 8.0, ejecutandose en el puerto 3306, con el pool de conexiones asincronas gestionado por mysql2 sobre la base "camila_nails".\n\n'
                 'd) Cliente Frontend: Aplicacion SPA construida con React.js y Vite, ejecutandose en http://localhost:5173.\n\n'
                 'e) Herramientas de Pruebas: \n'
                 '   - Postman v10+: Para la elaboracion y ejecucion de peticiones HTTP directas a la API REST (GET, POST, PUT, DELETE).\n'
                 '   - Google Chrome DevTools: Para inspeccion de consola, pruebas de estres de layout y emulacion de dispositivos moviles (360px a 412px).')

# --- MATRIZ DE CASOS ---
pdf.add_page()
pdf.chapter_title('3. MATRIZ DETALLADA DE CASOS DE PRUEBA')
pdf.chapter_body('A continuacion se presentan los casos de prueba disenados e implementados, detallando cada uno de los campos solicitados en el instrumento de evaluacion:')

casos_texto = [
    ("Caso 001 - Registro de nuevo usuario cliente",
     "Herramienta: Postman\n"
     "Autor: Andres Mauricio Valencia Arango\n"
     "Accion: POST /api/register con datos completos (nombre, usuario, correo, contrasena)\n"
     "Salida esperada: Codigo HTTP 200 OK con JSON {'success': true, 'message': 'Registro exitoso'}\n"
     "Salida obtenida: Codigo HTTP 200 OK y registro insertado en tabla 'users' de MySQL\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Baja\n"
     "Evidencia: Respuesta JSON status 200 en Postman y persistencia comprobada en DB\n"
     "Firma de aprobacion: Andres Mauricio Valencia Arango"),

    ("Caso 002 - Validacion de campos obligatorios en registro",
     "Herramienta: Postman\n"
     "Autor: Andres Mauricio Valencia Arango\n"
     "Accion: POST /api/register omitiendo el campo 'email'\n"
     "Salida esperada: Codigo HTTP 400 Bad Request con {'success': false, 'error': 'Faltan campos'}\n"
     "Salida obtenida: Codigo HTTP 400 Bad Request retornado, impidiendo registros inconsistentes\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Captura de pantalla de Postman con status 400 y mensaje de validacion\n"
     "Firma de aprobacion: Andres Mauricio Valencia Arango"),

    ("Caso 003 - Autenticacion de usuario administrador",
     "Herramienta: Postman\n"
     "Autor: Andres Mauricio Valencia Arango\n"
     "Accion: POST /api/login con credenciales validas de administrador\n"
     "Salida esperada: Codigo HTTP 200 OK con datos de perfil y rol 'admin'\n"
     "Salida obtenida: Acceso concedido satisfactoriamente con verificacion de rol admin\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Alta\n"
     "Evidencia: Contrasena validada mediante hash bcryptjs y respuesta JSON recibida\n"
     "Firma de aprobacion: Andres Mauricio Valencia Arango"),

    ("Caso 004 - Creacion manual de Ficha de Cliente desde Panel",
     "Herramienta: Postman / Navegador Chrome\n"
     "Autor: Andres Mauricio Valencia Arango\n"
     "Accion: POST /api/fichas con nombre, telefono y servicio\n"
     "Salida esperada: Registro insertado en tabla 'fichas' con ID autoincremental\n"
     "Salida obtenida: Ficha creada correctamente con Status 200 OK e insertId retornado\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Alta\n"
     "Evidencia: Registro almacenado en MySQL y visualizado en el listado del panel\n"
     "Firma de aprobacion: Andres Mauricio Valencia Arango"),

    ("Caso 005 - Modificacion y edicion de Ficha de Cliente",
     "Herramienta: Postman\n"
     "Autor: Andres Mauricio Valencia Arango\n"
     "Accion: PUT /api/fichas/:id con datos actualizados de servicio y telefono\n"
     "Salida esperada: Actualizacion en MySQL y mensaje {'message': 'Ficha actualizada'}\n"
     "Salida obtenida: Campos modificados en base de datos con respuesta exitosa\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Peticion PUT 200 OK en Postman y sincronizacion de datos\n"
     "Firma de aprobacion: Andres Mauricio Valencia Arango"),

    ("Caso 006 - Eliminacion fisica de registro (Usuario o Ficha)",
     "Herramienta: Postman\n"
     "Autor: Andres Mauricio Valencia Arango\n"
     "Accion: DELETE /api/users/:id con confirmacion previa\n"
     "Salida esperada: Registro removido fisicamente de MySQL con status 200 OK\n"
     "Salida obtenida: Status 200 OK {'message': 'Usuario eliminado'} y registro borrado\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Confirmacion de eliminacion y comprobacion de ausencia en GET\n"
     "Firma de aprobacion: Andres Mauricio Valencia Arango"),

    ("Caso 007 - Contraste y visibilidad de inputs en Modo Oscuro",
     "Herramienta: Google Chrome DevTools\n"
     "Autor: Andres Mauricio Valencia Arango\n"
     "Accion: Escritura y foco en los campos de formulario del panel de administracion\n"
     "Salida esperada: El texto escrito debe ser nitido y legible (blanco sobre fondo oscuro)\n"
     "Salida obtenida: Se detecto regla :focus con fondo blanco que ocultaba la letra; fue corregida en App.css\n"
     "Resultado: Aprobado | Seguimiento: BUG-UI-01 (Resuelto) | Severidad: Media\n"
     "Evidencia: Inspeccion de estilos en DevTools y verificacion visual en pantalla\n"
     "Firma de aprobacion: Andres Mauricio Valencia Arango"),

    ("Caso 008 - Adaptabilidad y diseno responsivo en pantalla movil",
     "Herramienta: Google Chrome DevTools (Responsive Emulator)\n"
     "Autor: Andres Mauricio Valencia Arango\n"
     "Accion: Emulacion de viewport en 375px y 412px de ancho\n"
     "Salida esperada: Reorganizacion de componentes a columna unica sin desbordamiento horizontal\n"
     "Salida obtenida: Se elimino el ancho fijo de 1126px del root; el contenido ahora fluye correctamente\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Baja\n"
     "Evidencia: Inspeccion satisfactoria en simulador de dispositivos de Chrome\n"
     "Firma de aprobacion: Andres Mauricio Valencia Arango")
]

for titulo_caso, contenido in casos_texto:
    pdf.chapter_subtitle(titulo_caso)
    pdf.chapter_body(contenido)

# --- CONCLUSIONES Y FIRMA ---
pdf.add_page()
pdf.chapter_title('4. CONCLUSIONES')
pdf.chapter_body('1. La estructuracion y ejecucion metódica de los casos de prueba permitio verificar el cumplimiento de los requerimientos tanto en la capa logica (Backend con Express y MySQL) como en la capa de presentacion (Frontend con React).\n\n'
                 '2. La identificacion y correccion de no conformidades (como el comportamiento del foco en formularios en modo oscuro y el ancho rigido del contenedor) demuestra la utilidad practica del ambiente de pruebas para pulir la experiencia de usuario antes de la salida a produccion.\n\n'
                 '3. La creacion del formato en Excel permite un seguimiento auditable y formal del ciclo de pruebas, contando con el respaldo y firma del analista responsable.')

pdf.ln(15)
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 6, '_____________________________________________', 0, 1, 'C')
pdf.cell(0, 6, 'Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.set_font('Arial', '', 10)
pdf.cell(0, 5, 'Aprendiz / Analista de Pruebas de Software', 0, 1, 'C')
pdf.cell(0, 5, 'Ficha 3186645 - ADSO SENA', 0, 1, 'C')

pdf_path = 'Evidencia_GA9-220501096-AA2-EV01_CasosPrueba.pdf'
pdf.output(pdf_path, 'F')
print(f"PDF generado con exito: {pdf_path}")
