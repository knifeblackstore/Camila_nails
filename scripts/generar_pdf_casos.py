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
pdf.cell(0, 8, 'Matriz de Pruebas: 15 Casos Disenados y Validados', 0, 1, 'C')
pdf.cell(0, 8, 'Formato principal entregable: Libro de Calculo Excel (.xlsx)', 0, 1, 'C')

# --- INTRODUCCIÓN ---
pdf.add_page()
pdf.chapter_title('1. INTRODUCCION')
pdf.chapter_body('El diseno de casos de prueba y la configuracion precisa del ambiente de pruebas representan actividades fundamentales en el aseguramiento de la calidad del software (QA). Un caso de prueba bien formulado establece las condiciones bajo las cuales un evaluador puede determinar si una aplicacion o modulo cumple con los requerimientos tecnicos y funcionales esperados.\n\nEl presente informe compila la definicion formal del ambiente de pruebas utilizado para el proyecto "Camila Nails" y detalla la matriz de quince (15) casos de prueba ejecutados sobre los modulos de autenticacion, administracion de usuarios, creacion y mantenimiento de fichas clinicas, asi como la adaptabilidad de la interfaz de usuario en entornos moviles y modo oscuro. Todo el diseno cumple rigurosamente con los campos exigidos por la guia de aprendizaje y las normas de presentacion SENA.')

# --- AMBIENTE DE PRUEBAS ---
pdf.chapter_title('2. DEFINICION DEL AMBIENTE DE PRUEBAS')
pdf.chapter_body('Para asegurar que las pruebas reflejen condiciones reales y confiables de operacion, se establecio el siguiente ambiente de trabajo de hardware y software:\n\n'
                 'a) Entorno de Hardware: Equipo portatil / estacion de trabajo con procesador multinucleo de 64 bits, 8 GB de memoria RAM y conexion de red local.\n\n'
                 'b) Servidor Backend: Entorno de ejecucion Node.js (version 18+) configurado con el framework Express.js, escuchando en el puerto local 4000 (http://localhost:4000).\n\n'
                 'c) Motor de Base de Datos: MySQL Community Server 8.0, ejecutandose en el puerto 3306, con el pool de conexiones asincronas gestionado por mysql2 sobre la base "camila_nails".\n\n'
                 'd) Cliente Frontend: Aplicacion SPA construida con React.js y Vite, ejecutandose en http://localhost:5173.\n\n'
                 'e) Herramientas de Pruebas: \n'
                 '   - Postman v10+: Para la elaboracion y ejecucion de peticiones HTTP directas a la API REST (GET, POST, PUT, PATCH, DELETE).\n'
                 '   - Google Chrome DevTools: Para inspeccion de consola, pruebas de estres de layout y emulacion de dispositivos moviles (360px a 412px).')

# --- MATRIZ DE 15 CASOS ---
pdf.add_page()
pdf.chapter_title('3. MATRIZ DE CASOS DE PRUEBA (15 CASOS)')
pdf.chapter_body('A continuacion se presentan los quince (15) casos de prueba disenados e implementados, detallando cada uno de los campos solicitados en el instrumento de evaluacion:')

autor = "Andres Mauricio Valencia Arango"

casos_15 = [
    ("Caso 001 - Registro exitoso de nuevo cliente",
     f"Herramienta: Postman | Autor: {autor}\n"
     "Accion: POST /api/register con datos completos (nombre, usuario, correo, contrasena)\n"
     "Salida esperada: Codigo HTTP 200 OK con JSON {'success': true, 'message': 'Registro exitoso'}\n"
     "Salida obtenida: Codigo HTTP 200 OK y registro insertado en tabla 'users' de MySQL\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Baja\n"
     "Evidencia: Respuesta JSON status 200 en Postman y persistencia comprobada en DB\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 002 - Validacion de campos obligatorios en registro",
     f"Herramienta: Postman | Autor: {autor}\n"
     "Accion: POST /api/register omitiendo el campo 'email'\n"
     "Salida esperada: Codigo HTTP 400 Bad Request con {'success': false, 'error': 'Faltan campos'}\n"
     "Salida obtenida: Codigo HTTP 400 Bad Request retornado, impidiendo registros incompletos\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Captura de pantalla de Postman con status 400 y mensaje de validacion\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 003 - Control de usuario duplicado en registro",
     f"Herramienta: Postman | Autor: {autor}\n"
     "Accion: POST /api/register con correo o username previamente existente\n"
     "Salida esperada: Codigo HTTP 409 Conflict con mensaje {'error': 'Usuario o email ya existe'}\n"
     "Salida obtenida: Codigo HTTP 409 recibido impidiendo duplicidad en base de datos\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Respuesta 409 Conflict y rechazo de clave duplicada en MySQL\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 004 - Autenticacion exitosa de administrador",
     f"Herramienta: Postman | Autor: {autor}\n"
     "Accion: POST /api/login con credenciales validas de administrador\n"
     "Salida esperada: Codigo HTTP 200 OK con datos de perfil y validacion de rol 'admin'\n"
     "Salida obtenida: Acceso concedido satisfactoriamente con verificacion de rol admin\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Alta\n"
     "Evidencia: Contrasena validada con hash bcryptjs y retorno de sesion en Postman\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 005 - Rechazo de inicio de sesion con clave incorrecta",
     f"Herramienta: Postman | Autor: {autor}\n"
     "Accion: POST /api/login con usuario valido pero contrasena errada\n"
     "Salida esperada: Codigo HTTP 401 Unauthorized {'error': 'Contrasena incorrecta'}\n"
     "Salida obtenida: Codigo HTTP 401 recibido, impidiendo accesos vulnerables\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Alta\n"
     "Evidencia: Respuesta 401 Unauthorized documentada en Postman\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 006 - Consulta general de usuarios registrados",
     f"Herramienta: Postman | Autor: {autor}\n"
     "Accion: GET /api/users para alimentar la vista de administracion\n"
     "Salida esperada: Arreglo JSON con usuarios excluyendo contrasenas\n"
     "Salida obtenida: Arreglo retornado con status 200 OK y hashes omitidos por seguridad\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Baja\n"
     "Evidencia: Lista en formato JSON visualizada con Status 200 OK\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 007 - Modificacion de rol de usuario en tiempo real",
     f"Herramienta: Postman | Autor: {autor}\n"
     "Accion: PATCH /api/users/:id/role cambiando el rol de 'user' a 'admin'\n"
     "Salida esperada: Status 200 OK y actualizacion de permisos en tabla 'users'\n"
     "Salida obtenida: Rol actualizado y confirmado inmediatamente en el backend\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Respuesta PATCH status 200 OK con confirmacion de actualizacion\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 008 - Edicion de datos de usuario en panel admin",
     f"Herramienta: Postman / Chrome | Autor: {autor}\n"
     "Accion: PUT /api/users/:id actualizando nombre y correo electronico\n"
     "Salida esperada: Actualizacion en MySQL y mensaje {'message': 'Usuario actualizado'}\n"
     "Salida obtenida: Datos actualizados y reflejados en vivo en el formulario\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Respuesta PUT status 200 OK y actualizacion en la vista de React\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 009 - Eliminacion fisica de cuenta de usuario",
     f"Herramienta: Postman / Chrome | Autor: {autor}\n"
     "Accion: DELETE /api/users/:id con confirmacion de alerta previa\n"
     "Salida esperada: Registro removido fisicamente de MySQL con status 200 OK\n"
     "Salida obtenida: Status 200 OK {'message': 'Usuario eliminado'} y registro borrado\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Alta\n"
     "Evidencia: Comprobacion de registro ausente tras peticion DELETE ejecutada\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 010 - Creacion manual de Ficha Clinica desde Panel",
     f"Herramienta: Postman / Chrome | Autor: {autor}\n"
     "Accion: POST /api/fichas con nombre de cliente, telefono y servicio\n"
     "Salida esperada: Insercion en tabla 'fichas' con ID autoincremental y status 200\n"
     "Salida obtenida: Ficha creada correctamente con Status 200 OK e insertId asignado\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Alta\n"
     "Evidencia: Ficha persistida en MySQL y visible al instante en la lista del panel\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 011 - Consulta y recuperacion del historial de Fichas",
     f"Herramienta: Postman | Autor: {autor}\n"
     "Accion: GET /api/fichas para consultar todos los historiales clinicos\n"
     "Salida esperada: Retorno de todas las fichas ordenadas cronologicamente\n"
     "Salida obtenida: Arreglo JSON recibido con todos los historiales y servicios\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Baja\n"
     "Evidencia: Respuesta GET 200 OK visualizada en Postman con arreglo de fichas\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 012 - Modificacion y actualizacion de Ficha Clinica",
     f"Herramienta: Postman / Chrome | Autor: {autor}\n"
     "Accion: PUT /api/fichas/:id actualizando telefono y servicio asignado\n"
     "Salida esperada: Actualizacion en MySQL y mensaje {'message': 'Ficha actualizada'}\n"
     "Salida obtenida: Campos modificados en base de datos con confirmacion exitosa\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Peticion PUT 200 OK en Postman y sincronizacion en interfaz React\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 013 - Eliminacion fisica de Ficha de Cliente",
     f"Herramienta: Postman / Chrome | Autor: {autor}\n"
     "Accion: DELETE /api/fichas/:id con confirmacion del usuario\n"
     "Salida esperada: Registro de ficha eliminado de la base de datos con status 200 OK\n"
     "Salida obtenida: Status 200 OK {'message': 'Ficha eliminada'} y registro borrado\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Media\n"
     "Evidencia: Comprobacion en tabla 'fichas' y actualizacion dinamica en pantalla\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 014 - Contraste y legibilidad de inputs en Modo Oscuro",
     f"Herramienta: Google Chrome DevTools | Autor: {autor}\n"
     "Accion: Escritura y foco en los campos de formulario del panel de administracion\n"
     "Salida esperada: El texto escrito debe ser nitido y legible (blanco sobre fondo oscuro)\n"
     "Salida obtenida: Se detecto regla :focus con fondo blanco que ocultaba la letra; fue corregida en App.css\n"
     "Resultado: Aprobado | Seguimiento: BUG-UI-01 (Resuelto) | Severidad: Media\n"
     "Evidencia: Inspeccion de estilos en DevTools y verificacion visual en pantalla\n"
     f"Firma de aprobacion: {autor}"),

    ("Caso 015 - Diseno responsivo del Home y Navbar en moviles",
     f"Herramienta: Google Chrome DevTools (Responsive) | Autor: {autor}\n"
     "Accion: Emulacion de viewport en 360px y 412px de ancho en dispositivos moviles\n"
     "Salida esperada: Adaptacion fluida de lado a lado sin marco rigido ni desbordamiento lateral\n"
     "Salida obtenida: Ancho fijo de 1126px reemplazado por 100% fluido con padding movil perfecto\n"
     "Resultado: Aprobado | Seguimiento: N/A | Severidad: Baja\n"
     "Evidencia: Emulacion responsive en Google Chrome DevTools con visual amplia\n"
     f"Firma de aprobacion: {autor}")
]

for titulo_caso, contenido in casos_15:
    pdf.chapter_subtitle(titulo_caso)
    pdf.chapter_body(contenido)

# --- CONCLUSIONES Y FIRMA ---
pdf.add_page()
pdf.chapter_title('4. CONCLUSIONES')
pdf.chapter_body('1. La ejecucion de los quince (15) casos de prueba cubrio de manera integral todas las capas de la aplicacion: validaciones de seguridad de backend (bcryptjs, control de duplicados, codigos HTTP), persistencia de datos en MySQL y experiencia visual en React.\n\n'
                 '2. La identificacion y resolucion documentada de defectos reales (como la incidencia BUG-UI-01 en el foco del modo oscuro y la rigidez de ancho del layout) valida la efectividad del proceso de QA implementado.\n\n'
                 '3. El formato de matriz de casos de prueba en Excel (.xlsx) y este documento consolidan formalmente la evidencia técnica, respaldada con la firma del analista de pruebas.')

pdf.ln(15)
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 6, '_____________________________________________', 0, 1, 'C')
pdf.cell(0, 6, 'Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.set_font('Arial', '', 10)
pdf.cell(0, 5, 'Aprendiz / Analista de Pruebas de Software', 0, 1, 'C')
pdf.cell(0, 5, 'Ficha 3186645 - ADSO SENA', 0, 1, 'C')

pdf_path = 'Evidencia_GA9-220501096-AA2-EV01_CasosPrueba.pdf'
pdf.output(pdf_path, 'F')
print(f"PDF con 15 casos generado con exito: {pdf_path}")
