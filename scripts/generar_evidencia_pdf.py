from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'SENA - Analisis y Desarrollo de Software', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Pagina ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 6, body)
        self.ln(4)

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 20, 'EVIDENCIA: API. GA7-220501096-AA5-EV02', 0, 1, 'C')
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.cell(0, 8, 'Programa: Analisis y Desarrollo de Software', 0, 1, 'C')
pdf.cell(0, 8, 'Estudiante: Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.cell(0, 8, 'Ficha: 3186645', 0, 1, 'C')
pdf.cell(0, 8, 'Instructor: Adornay Sanchez', 0, 1, 'C')
pdf.cell(0, 8, 'Proyecto: Camila Nails (API REST en Node.js y MySQL)', 0, 1, 'C')
pdf.ln(20)

pdf.add_page()
pdf.chapter_title('INDICE')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 8, '1. Introduccion', 0, 1)
pdf.cell(0, 8, '2. Objetivo', 0, 1)
pdf.cell(0, 8, '3. Ficha Tecnica', 0, 1)
pdf.cell(0, 8, '4. Pruebas de Endpoints (Postman)', 0, 1)
pdf.cell(0, 8, '5. Conclusion', 0, 1)

pdf.add_page()
pdf.chapter_title('1. INTRODUCCION')
pdf.chapter_body('El presente documento tiene como finalidad evidenciar la creacion y funcionamiento de la API REST desarrollada para el sistema de informacion web "Camila Nails". A traves de la herramienta Postman, se realizan peticiones HTTP para validar el correcto comportamiento de los diferentes endpoints, verificando los metodos GET, POST, PUT y DELETE para gestionar los usuarios y las fichas tecnicas de los clientes.')

pdf.chapter_title('2. OBJETIVO')
pdf.chapter_body('Demostrar la operatividad y funcionalidad de la interfaz de programacion de aplicaciones (API) del proyecto mediante la ejecucion de pruebas de consumo con Postman, asegurando que las operaciones CRUD (Crear, Leer, Actualizar, Borrar) sobre la base de datos MySQL se ejecuten de manera correcta segun los requisitos tecnicos del sistema.')

pdf.chapter_title('3. FICHA TECNICA')
pdf.chapter_body('- Arquitectura: Cliente-Servidor\n- Backend: Node.js con el framework Express.js\n- Base de Datos: MySQL (Modulo mysql2 para conexion asincrona)\n- Frontend: React.js (Vite)\n- Seguridad: Encriptacion de contraseñas con bcryptjs\n- Puerto del Servidor: 4000\n- Rutas principales expuestas:\n   * /api/users (GET, POST, PUT, DELETE)\n   * /api/register y /api/login (Autenticacion)\n   * /api/fichas (GET, POST)\n   * /api/pending (Gestion de aprobaciones)')

pdf.add_page()
pdf.chapter_title('4. PRUEBAS DE ENDPOINTS EN POSTMAN')
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, '4.1 Creacion de Usuarios (POST /api/register)', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 6, 'Se probaron multiples escenarios para el registro de usuarios. En el caso de que los datos esten incompletos, el servidor valida y responde con un codigo 400 Bad Request. A continuacion, se adjunta captura de pantalla del resultado arrojado en Postman durante las pruebas de error.')
pdf.ln(5)
try:
    pdf.image('C:/Users/usuario/.gemini/antigravity/brain/0f16d4c8-9b91-4828-aa07-1f7caec42c6d/.user_uploaded/media_1787970125271.png', w=170)
except Exception as e:
    pdf.cell(0, 8, '[Imagen no encontrada en la ruta]', 0, 1)
pdf.ln(10)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, '4.2 Lectura de Fichas Clinicas (GET /api/fichas)', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 6, 'Se realizo la peticion GET para consultar todas las fichas de los clientes almacenadas en la base de datos. El servidor devuelve un JSON con formato de arreglo que contiene todos los registros historicos, respondiendo con un codigo 200 OK.')
pdf.ln(5)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, '4.3 Borrado de un Usuario (DELETE /api/users/:id)', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 6, 'Para la accion de borrado, se comprobo que enviando una peticion DELETE al endpoint con el ID del usuario, este es eliminado fisicamente de la base de datos y se obtiene una confirmacion en formato JSON ({ "success": true, "message": "Usuario eliminado" }).')
pdf.ln(10)

pdf.chapter_title('5. CONCLUSION')
pdf.chapter_body('El desarrollo y las pruebas de la API del proyecto "Camila Nails" cumplen a cabalidad con los lineamientos tecnicos requeridos. Las respuestas de los endpoints son consistentes con la informacion solicitada, la validacion de errores funciona adecuadamente (evitando caidas del servidor por datos incompletos) y la integracion con la base de datos MySQL es estable, lo que garantiza el correcto funcionamiento del modelo de datos para el despliegue final del software.')

pdf.output('Evidencia_API_GA7-220501096-AA5-EV02.pdf', 'F')
print('PDF generado exitosamente.')
