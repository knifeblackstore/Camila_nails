# -*- coding: utf-8 -*-
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Arial', 'B', 8.5)
            self.set_text_color(70, 70, 70)
            self.cell(0, 6, 'SENA | Analisis y Desarrollo de Software (ADSO) - Ficha 3186645', 0, 1, 'C')
            self.set_draw_color(57, 169, 0)
            self.set_line_width(0.4)
            self.line(12, 16, 198, 16)
            self.ln(5)

    def footer(self):
        self.set_y(-14)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(110, 110, 110)
        self.cell(0, 10, 'Evidencia GA10-220501097-AA3-EV01 | Pagina ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 13)
        self.set_fill_color(232, 245, 233)
        self.set_text_color(25, 80, 0)
        self.cell(0, 9, '  ' + title, 0, 1, 'L', 1)
        self.ln(3)

    def chapter_subtitle(self, subtitle):
        self.set_font('Arial', 'B', 11)
        self.set_text_color(35, 35, 35)
        self.cell(0, 7, subtitle, 0, 1, 'L')
        self.ln(1.5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10.5)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6.5, body)
        self.ln(2)

    def image_placeholder(self, title, description):
        self.ln(2)
        self.set_fill_color(240, 240, 240)
        self.set_draw_color(200, 200, 200)
        self.rect(self.get_x() + 15, self.get_y(), 160, 40, 'DF')
        self.set_y(self.get_y() + 15)
        self.set_font('Arial', 'I', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, '[ ' + title + ' ]', 0, 1, 'C')
        self.set_font('Arial', '', 9)
        self.cell(0, 5, description, 0, 1, 'C')
        self.set_y(self.get_y() + 20)
        self.ln(2)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# =========================================================================
# PÁGINA 1: PORTADA
# =========================================================================
pdf.add_page()
pdf.set_y(45)
pdf.set_font('Arial', 'B', 12)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 6, 'SERVICIO NACIONAL DE APRENDIZAJE - SENA', 0, 1, 'C')
pdf.cell(0, 6, 'CENTRO DE FORMACION TECNOLOGICA | REGIONAL RISARALDA', 0, 1, 'C')
pdf.ln(20)

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(25, 80, 0)
pdf.multi_cell(0, 8, 'EVIDENCIA GA10-220501097-AA3-EV01\nSoftware instalado en la plataforma del cliente', align='C')
pdf.ln(25)

pdf.set_font('Arial', '', 12)
pdf.set_text_color(40, 40, 40)
pdf.cell(0, 8, 'Programa de Formacion: Analisis y Desarrollo de Software (ADSO)', 0, 1, 'C')
pdf.cell(0, 8, 'Numero de Ficha: 3186645', 0, 1, 'C')
pdf.cell(0, 8, 'Aprendiz: Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.cell(0, 8, 'Instructor: Adornay Sanchez', 0, 1, 'C')
pdf.ln(20)
pdf.cell(0, 8, 'Pereira, Risaralda - 2026', 0, 1, 'C')

# =========================================================================
# PÁGINA 2: INTRODUCCIÓN Y ELECCIÓN DE HERRAMIENTAS
# =========================================================================
pdf.add_page()
pdf.chapter_title('1. INTRODUCCION')
pdf.chapter_body(
    'El despliegue de una aplicacion o pagina web en un entorno local es el paso previo '
    'fundamental antes de llevar el software a un servidor publico en internet. Este proceso, '
    'conocido como montaje de entorno de desarrollo o despliegue local, permite a los desarrolladores '
    'y analistas verificar que todos los recursos (HTML, CSS, JavaScript, imagenes) se ejecuten '
    'correctamente bajo un servidor web real, en lugar de simplemente abrir archivos estaticos en el navegador.\n\n'
    'En este informe se detalla el paso a paso tecnico para la instalacion de una plataforma '
    'de desarrollo local y el posterior montaje de una plantilla HTML gratuita. Se incluye la '
    'seleccion de las herramientas utilizadas y el procedimiento descriptivo para garantizar '
    'la accesibilidad del producto de prueba desde la plataforma del cliente (el entorno de trabajo '
    'local de Windows).'
)

pdf.chapter_title('2. SELECCION DE HERRAMIENTAS Y PLATAFORMA')

pdf.chapter_subtitle('2.1. Seleccion de la Plantilla HTML (Producto de Prueba)')
pdf.chapter_body(
    'Para efectos de este despliegue, se ha seleccionado una plantilla HTML/CSS gratuita '
    'de diseño tipo "Landing Page" (Pagina de aterrizaje). \n'
    '- Origen de la plantilla: Se utilizo el repositorio sugerido en Dev.to (https://dev.to/davidepacilio/40-free-html-landing-page-templates-3gfp).\n'
    '- Plantilla seleccionada: "Evelyn" (o equivalente HTML estatico). Es una plantilla moderna que incluye index.html, carpeta de hojas de estilo (CSS) y carpeta de recursos graficos (Images), ideal para validar un despliegue de contenido estatico.'
)

pdf.chapter_subtitle('2.2. Seleccion de la Plataforma de Desarrollo Local')
pdf.chapter_body(
    'Para montar el servidor de aplicaciones local, se ha seleccionado XAMPP. \n'
    'XAMPP es una distribucion de Apache completamente gratuita y facil de instalar que contiene '
    'MariaDB, PHP y Perl. \n\n'
    'Justificacion: \n'
    'Se eligio XAMPP porque empaqueta el servidor web Apache, que es el estandar mas utilizado '
    'a nivel global para servir documentos HTML y procesar PHP. Ademas, su panel de control '
    'brinda una interfaz grafica amigable para iniciar y detener el servidor sin necesidad de '
    'usar consolas de comandos.'
)

# =========================================================================
# PÁGINA 3: INSTALACIÓN DEL SERVIDOR
# =========================================================================
pdf.add_page()
pdf.chapter_title('3. PASO A PASO: INSTALACION DE LA PLATAFORMA (XAMPP)')

pdf.chapter_subtitle('Paso 1: Descarga del Instalador')
pdf.chapter_body(
    '1. Se ingresa al sitio oficial de Apache Friends (https://www.apachefriends.org/es/index.html).\n'
    '2. Se hace clic en el boton "XAMPP para Windows" para descargar la ultima version estable.\n'
    '3. Se espera a que finalice la descarga del archivo ejecutable (.exe).'
)
pdf.image_placeholder('Captura Descriptiva 1: Descarga de XAMPP', 'Sitio web oficial de Apache Friends mostrando el boton de descarga para Windows.')

pdf.chapter_subtitle('Paso 2: Ejecucion y Seleccion de Componentes')
pdf.chapter_body(
    '1. Se ejecuta el instalador descargado con permisos de Administrador.\n'
    '2. En la pantalla de seleccion de componentes, se deja marcado "Apache" (obligatorio para paginas HTML) y "PHP". No es indispensable MySQL para esta prueba estatica, pero se puede dejar por defecto.\n'
    '3. Se selecciona la ruta de instalacion por defecto, que generalmente es "C:\\xampp".'
)
pdf.image_placeholder('Captura Descriptiva 2: Asistente de instalacion', 'Ventana del asistente de XAMPP (Setup) donde se seleccionan los componentes a instalar.')

pdf.chapter_subtitle('Paso 3: Finalizacion y Panel de Control')
pdf.chapter_body(
    '1. Una vez terminada la instalacion, se desmarca o marca la opcion de abrir el Panel de Control y se da clic en "Finish".\n'
    '2. Al abrir el "XAMPP Control Panel", se observan los servicios disponibles (Apache, MySQL, FileZilla, etc.).\n'
    '3. Se hace clic en el boton "Start" ubicado al lado del modulo "Apache". El fondo del nombre "Apache" se pondra en color verde, indicando que el servidor web local esta funcionando en el puerto 80 (o 8080 si hay conflictos).'
)
pdf.image_placeholder('Captura Descriptiva 3: Panel de Control Apache Activo', 'Panel de XAMPP mostrando el modulo Apache resaltado en color verde y los puertos asignados (80, 443).')

# =========================================================================
# PÁGINA 4: DESPLIEGUE DEL PRODUCTO
# =========================================================================
pdf.add_page()
pdf.chapter_title('4. PASO A PASO: MONTAJE Y DESPLIEGUE DE LA PLANTILLA')

pdf.chapter_subtitle('Paso 1: Preparacion de los archivos HTML')
pdf.chapter_body(
    '1. Se descarga la plantilla HTML seleccionada en formato ZIP desde el sitio web.\n'
    '2. Se extrae (descomprime) el archivo ZIP en una carpeta temporal (por ejemplo, en Descargas). La carpeta debe contener el archivo "index.html" y las carpetas "css", "js", e "img".'
)
pdf.image_placeholder('Captura Descriptiva 4: Archivos de la Plantilla', 'Explorador de archivos mostrando el index.html y las carpetas de recursos extraidas del ZIP.')

pdf.chapter_subtitle('Paso 2: Montaje en el directorio de servidor (htdocs)')
pdf.chapter_body(
    '1. Se abre el Explorador de Archivos de Windows y se navega hasta la ruta de instalacion de XAMPP: "C:\\xampp\\htdocs".\n'
    '2. El directorio "htdocs" es la raiz publica del servidor Apache. Todo lo que se ponga aqui podra verse en el navegador.\n'
    '3. Se crea una nueva carpeta dentro de htdocs llamada "mi_proyecto_sena".\n'
    '4. Se copian todos los archivos de la plantilla extraida (index.html, css, etc.) y se pegan dentro de "C:\\xampp\\htdocs\\mi_proyecto_sena".'
)
pdf.image_placeholder('Captura Descriptiva 5: Ruta htdocs', 'Carpeta htdocs mostrando la subcarpeta "mi_proyecto_sena" con los archivos HTML en su interior.')

pdf.chapter_subtitle('Paso 3: Pruebas de Despliegue Local')
pdf.chapter_body(
    '1. Se abre un navegador web (Google Chrome, Firefox o Edge).\n'
    '2. En la barra de direcciones se escribe: "http://localhost/mi_proyecto_sena" y se presiona la tecla Enter.\n'
    '3. El navegador se comunica con el servidor Apache local, el cual lee el archivo index.html de la carpeta especificada y renderiza la plantilla web en la pantalla.'
)
pdf.image_placeholder('Captura Descriptiva 6: Despliegue Exitoso en el Navegador', 'Navegador Chrome mostrando la plantilla web renderizada perfectamente en la direccion localhost.')

# =========================================================================
# PÁGINA 5: CONCLUSIONES Y BIBLIOGRAFÍA
# =========================================================================
pdf.add_page()
pdf.chapter_title('5. CONCLUSIONES GENERALES')
pdf.chapter_body(
    '1. La instalacion de una plataforma de desarrollo local como XAMPP simplifica enormemente '
    'el proceso de despliegue de aplicaciones, al empaquetar servicios complejos como Apache '
    'en una interfaz grafica de facil gestion.\n\n'
    '2. El directorio raiz (htdocs en el caso de XAMPP) actua como el espacio de almacenamiento '
    'publico del servidor. Comprender como el servidor mapea la direccion "localhost" hacia esta '
    'carpeta fisica es fundamental para el montaje de cualquier sitio web.\n\n'
    '3. Desplegar una plantilla HTML mediante un servidor web local es una simulacion exacta '
    'del comportamiento que tendra la aplicacion en un hosting de produccion. Esto permite '
    'validar la carga de rutas, estilos y scripts de manera segura antes de ser presentados '
    'a un cliente real.'
)

pdf.chapter_title('6. REFERENCIAS BIBLIOGRAFICAS')
pdf.chapter_body(
    'Apache Friends. (2024). XAMPP Installers and Downloads. Recuperado de: https://www.apachefriends.org/es/index.html\n\n'
    'SENA. (2024). Componente Formativo: Identificación de requerimientos y despliegue local. Territorio SENA.\n\n'
    'Pacilio, D. (2020). 40 Free HTML Landing Page Templates. Dev.to Community. Recuperado de: https://dev.to/davidepacilio/40-free-html-landing-page-templates-3gfp'
)

pdf.ln(15)
pdf.set_font('Arial', 'B', 10.5)
pdf.cell(0, 5, '____________________________________________________', 0, 1, 'C')
pdf.cell(0, 5, 'Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.set_font('Arial', '', 9.5)
pdf.cell(0, 4.5, 'Aprendiz / Analista de Pruebas y Calidad de Software', 0, 1, 'C')
pdf.cell(0, 4.5, 'Ficha 3186645 - ADSO SENA Regional Risaralda', 0, 1, 'C')

reporte_path = 'Evidencia_GA10-220501097-AA3-EV01_Instalacion_Software.pdf'
pdf.output(reporte_path, 'F')
print(f"Reporte de instalacion y despliegue generado con exito: {reporte_path}")
