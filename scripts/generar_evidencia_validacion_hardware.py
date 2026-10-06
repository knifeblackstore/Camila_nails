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
        self.cell(0, 10, 'Evidencia GA10-220501097-AA2-EV01 | Pagina ' + str(self.page_no()), 0, 0, 'C')

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
        self.ln(4)

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
pdf.multi_cell(0, 8, 'EVIDENCIA GA10-220501097-AA2-EV01\nPlan de validacion de caracteristicas minimas\nde hardware para el software', align='C')
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
# PÁGINA 2: INTRODUCCIÓN Y OBJETIVOS
# =========================================================================
pdf.add_page()
pdf.chapter_title('1. INTRODUCCION')
pdf.chapter_body(
    'En el ciclo de vida del desarrollo de software, la fase de implantacion y despliegue '
    'representa el momento critico en el que una aplicacion pasa del entorno de desarrollo '
    'al entorno de produccion, donde sera consumida por los usuarios finales. Para garantizar '
    'que esta transicion sea exitosa, no basta con tener un codigo fuente optimizado; es '
    'estrictamente necesario que la infraestructura tecnologica que alojara dicho software '
    'cumpla con las caracteristicas de hardware y software proporcionales a la demanda esperada.\n\n'
    'El presente documento establece un "Plan de Validacion de Caracteristicas Minimas de Hardware", '
    'orientado especificamente a un escenario particular propuesto: una aplicacion web desarrollada '
    'en PHP, que requiere acceso a informacion persistente (bases de datos) para identificar y registrar '
    'usuarios, y que proyecta atender a una poblacion de aproximadamente 250 usuarios activos no '
    'concurrentes.\n\n'
    'A traves de este informe extenso, se desglosaran de manera metodologica los requerimientos '
    'de procesamiento, memoria, almacenamiento, conectividad de red y licenciamiento, estableciendo '
    'una hoja de ruta que permita al equipo de infraestructura auditar y validar si el servidor '
    '(sea fisico o basado en la nube) cumple con las condiciones minimas viables para sostener '
    'la operacion sin degradacion del servicio.'
)

pdf.chapter_title('2. OBJETIVOS DEL PLAN DE VALIDACION')
pdf.chapter_body(
    '- Definir los requerimientos de hardware exactos que soporten una arquitectura LAMP (Linux, Apache, MySQL, PHP) o similar, capaz de procesar las peticiones de 250 usuarios no concurrentes.\n'
    '- Establecer una lista de chequeo (checklist) ordenada que permita a los administradores de sistemas verificar cada componente critico del servidor antes del paso a produccion.\n'
    '- Analizar el impacto del software base (sistema operativo de red y motores de base de datos) sobre los recursos de hardware y sus respectivas implicaciones de licenciamiento.\n'
    '- Documentar las fuentes y normativas que respaldan la toma de decisiones en el alistamiento de infraestructura.'
)

# =========================================================================
# PÁGINA 3: ANÁLISIS DEL ESCENARIO Y PARÁMETROS
# =========================================================================
pdf.add_page()
pdf.chapter_title('3. ANALISIS DEL ESCENARIO TECNICO')
pdf.chapter_body(
    'Antes de listar los componentes de hardware a validar, es indispensable deconstruir '
    'las restricciones y proyecciones del caso de estudio provisto. El dimensionamiento '
    '(sizing) de un servidor depende directamente de tres factores claves:'
)

pdf.chapter_subtitle('3.1. Aplicacion web desarrollada en PHP')
pdf.chapter_body(
    'PHP es un lenguaje de scripting del lado del servidor que, tradicionalmente, se ejecuta '
    'de manera sincrona y bloqueante por cada peticion web (a traves de modulos como mod_php '
    'en Apache o PHP-FPM en Nginx). Esto significa que cada usuario que realiza una accion '
    'en la plataforma genera un proceso (o hilo) independiente en el servidor.\n\n'
    'Por lo tanto, la validacion de hardware debe contemplar suficiente memoria RAM para '
    'sostener multiples hilos de PHP abiertos simultaneamente, y una CPU con buena capacidad '
    'de procesamiento mononucleo para resolver la logica de negocio de los scripts PHP de '
    'manera rapida.'
)

pdf.chapter_subtitle('3.2. Acceso a informacion persistente (Base de Datos)')
pdf.chapter_body(
    'La aplicacion debe registrar e identificar usuarios, lo que implica el uso obligatorio '
    'de un Sistema Gestor de Bases de Datos Relacionales (RDBMS) como MySQL, MariaDB o '
    'PostgreSQL.\n\n'
    'Las bases de datos son los componentes mas demandantes en cualquier servidor. Requieren '
    'operaciones intensivas de lectura y escritura (I/O). En consecuencia, la validacion del '
    'hardware debe ser inflexible en exigir discos de estado solido (SSD o NVMe) y suficiente '
    'memoria RAM para que el motor de base de datos pueda almacenar los indices (Index Buffer) '
    'en memoria y no depender del disco.'
)

pdf.chapter_subtitle('3.3. Poblacion: 250 usuarios activos no concurrentes')
pdf.chapter_body(
    'Este es quizas el dato mas revelador para evitar sobrecostos. "250 usuarios activos" '
    'indica el tamano del padron de clientes, pero "no concurrentes" significa que no todos '
    'estan haciendo clic o procesando transacciones en el mismo segundo exacto.\n\n'
    'Si estimamos una concurrencia realista del 10% al 20%, el servidor debera manejar '
    'aproximadamente entre 25 y 50 peticiones simultaneas en los picos de mayor trafico. '
    'Esta carga es considerada "baja/moderada" para estandares modernos, lo que permite '
    'descartar servidores empresariales gigantes y optar por soluciones agiles como un Servidor '
    'Virtual Privado (VPS) economico pero bien optimizado.'
)

# =========================================================================
# PÁGINA 4: LISTA ORDENADA DE VERIFICACIÓN DE HARDWARE (CPU Y RAM)
# =========================================================================
pdf.add_page()
pdf.chapter_title('4. LISTA ORDENADA DE VALIDACION DE HARDWARE')
pdf.chapter_body(
    'A continuacion se desglosa la lista ordenada de elementos que deben ser auditados '
    'y validados en el servidor de destino para asegurar que se poseen las caracteristicas '
    'minimas de operacion.'
)

pdf.chapter_subtitle('Elemento 1: Unidad Central de Procesamiento (CPU)')
pdf.chapter_body(
    'Validacion a realizar: Verificar la cantidad de nucleos fisicos/virtuales y la frecuencia de reloj.\n\n'
    'Justificacion: Al usar PHP (un lenguaje que interpreta scripts por peticion) en combinacion '
    'con consultas a una base de datos, el procesador debe calcular y devolver las respuestas '
    'antes de que el usuario perciba lentitud. Para 50 conexiones concurrentes maximas:\n'
    '- Caracteristica Minima Requerida: 2 vCores (Nucleos Virtuales) a una velocidad base de 2.0 GHz o superior.\n'
    '- Metodo de validacion (Linux): Ejecutar el comando "lscpu" o "cat /proc/cpuinfo" en la terminal del servidor para confirmar que se cuenta con al menos 2 procesadores lógicos.\n'
    '- Criterio de Aprobacion: Si el servidor solo tiene 1 nucleo, se corre el riesgo de cuellos de botella si varios usuarios hacen consultas pesadas al mismo tiempo; se aprueba la validacion solo con 2 nucleos o mas.'
)

pdf.chapter_subtitle('Elemento 2: Memoria Principal (RAM)')
pdf.chapter_body(
    'Validacion a realizar: Auditar la capacidad de memoria RAM total instalada y la disponible tras el arranque del sistema operativo.\n\n'
    'Justificacion: La memoria RAM es el recurso critico en arquitecturas web tradicionales. Considerando el ecosistema LAMP:\n'
    ' - Sistema Operativo (Ubuntu Server): ~400 MB.\n'
    ' - Servidor Web (Apache/Nginx): ~200 MB.\n'
    ' - Base de Datos (MySQL) con indices de usuarios: ~500 MB - 1 GB.\n'
    ' - Procesos PHP-FPM (50 concurrentes a ~20MB cada uno): ~1 GB.\n'
    '- Caracteristica Minima Requerida: 2 GB de memoria RAM (Estrictamente minimo), siendo 4 GB lo recomendado para holgura operativa.\n'
    '- Metodo de validacion (Linux): Ejecutar el comando "free -h" o "htop" para confirmar la capacidad total de la memoria fisica.\n'
    '- Criterio de Aprobacion: El hardware debe demostrar contar con al menos 2048 MB de memoria RAM sin recurrir al espacio de paginacion (Swap), ya que el Swap degradaria la velocidad de las respuestas PHP.'
)

# =========================================================================
# PÁGINA 5: LISTA ORDENADA DE VERIFICACIÓN (ALMACENAMIENTO Y RED)
# =========================================================================
pdf.add_page()
pdf.chapter_subtitle('Elemento 3: Almacenamiento (Disco Duro)')
pdf.chapter_body(
    'Validacion a realizar: Comprobar la tecnologia del disco (HDD vs SSD) y el espacio de almacenamiento util disponible.\n\n'
    'Justificacion: Puesto que el enunciado especifica que "la aplicacion accede a informacion persistente para identificacion", '
    'la base de datos realizara lecturas y escrituras constantes. Un disco mecanico (HDD) tradicional generaria un embotellamiento '
    'severo (I/O Wait) que haria colapsar al servidor web esperando respuestas de la base de datos.\n'
    '- Caracteristica Minima Requerida: Disco de Estado Solido (SSD) o NVMe con al menos 30 GB de espacio total (10GB para el OS, '
    '5GB para dependencias y PHP, y 15GB para crecimiento de la base de datos de los 250 usuarios).\n'
    '- Metodo de validacion (Linux): Ejecutar "lsblk" o "df -h" para ver el tamano, y revisar la documentacion del proveedor (AWS, DigitalOcean, Azure) para garantizar que el volumen montado es SSD.\n'
    '- Criterio de Aprobacion: El plan falla automaticamente si se asignan discos magneticos HDD de 5400/7200 RPM.'
)

pdf.chapter_subtitle('Elemento 4: Interfaz de Red y Ancho de Banda')
pdf.chapter_body(
    'Validacion a realizar: Verificar la capacidad del puerto de red del servidor y el limite de transferencia mensual.\n\n'
    'Justificacion: Un software web no sirve de nada si el canal de comunicacion esta saturado. Aunque son solo 250 usuarios, '
    'si el software en PHP sirve interfaces graficas completas (HTML/CSS/JS) ademas de datos, la red debe soportar varios megabits por segundo.\n'
    '- Caracteristica Minima Requerida: Tarjeta de red con capacidad Gigabit Ethernet (1 Gbps) o, en su defecto, un enlace de al menos 100 Mbps simetricos en el centro de datos.\n'
    '- Metodo de validacion: Pruebas de ancho de banda usando herramientas como "iperf" o midiendo la respuesta con peticiones controladas.\n'
    '- Criterio de Aprobacion: La conexion de red del servidor debe responder a peticiones externas a traves del puerto 80 (HTTP) y 443 (HTTPS) sin excesiva latencia (ping menor a 150ms desde la zona geografica objetivo).'
)

# =========================================================================
# PÁGINA 6: SISTEMAS OPERATIVOS Y LICENCIAMIENTO
# =========================================================================
pdf.add_page()
pdf.chapter_title('5. SISTEMAS OPERATIVOS DE RED Y LICENCIAMIENTO')
pdf.chapter_body(
    'El componente formativo del SENA destaca la estrecha relacion entre el hardware y el software '
    'base (Sistemas Operativos). Como parte integral de este plan de validacion, se debe justificar '
    'el ecosistema de software bajo el cual operara la infraestructura.'
)

pdf.chapter_subtitle('5.1. Eleccion del Sistema Operativo de Red')
pdf.chapter_body(
    'Para alojar una aplicacion PHP con base de datos, las dos opciones dominantes son Microsoft Windows Server '
    'o una distribucion de GNU/Linux (como Ubuntu Server, Debian o AlmaLinux).\n\n'
    'Decision Validada: Se recomienda enfaticamente la eleccion de Linux (especificamente Ubuntu Server 22.04 LTS o 24.04 LTS) '
    'debido a que PHP y herramientas auxiliares (Apache/Nginx, MySQL) fueron creadas con arquitectura Unix en mente. '
    'Linux es considerablemente mas liviano, lo que significa que de los 2 GB de RAM propuestos en la caracteristica minima, '
    'Linux solo consumira una fraccion minima para si mismo, dejando el resto de recursos para la aplicacion PHP.'
)

pdf.chapter_subtitle('5.2. Verificacion de Licenciamiento de Software')
pdf.chapter_body(
    'El aspecto legal es vital para evitar multas a las organizaciones. La validacion del hardware '
    'debe ir acompanada de una validacion de licencias:\n\n'
    '- SO Linux: Se distribuye bajo licencias de codigo abierto (GPL, MIT, etc.), lo que exime al proyecto de pagos por licencias de servidor.\n'
    '- PHP: Publicado bajo la licencia PHP License (Open Source).\n'
    '- MySQL: Su edicion comunitaria (Community Server) esta licenciada bajo GPL, apta para el proyecto descrito sin costos adicionales.\n\n'
    'Criterio de Aprobacion: Al optar por el stack LAMP/LEMP, el proyecto no incurrira en costos por licenciamiento de software, lo que permite redirigir el presupuesto hacia la contratacion de mejor hardware (mas CPU y RAM SSD).'
)

# =========================================================================
# PÁGINA 7: CONCLUSIONES Y BIBLIOGRAFÍA
# =========================================================================
pdf.add_page()
pdf.chapter_title('6. CONCLUSIONES GENERALES')
pdf.chapter_body(
    '1. La proyeccion de 250 usuarios no concurrentes define un perfil de carga moderado-bajo. '
    'Esto significa que la adquisicion de un servidor de gama alta representaria un gasto innecesario (sobre-aprovisionamiento). '
    'Las caracteristicas minimas estructuradas en este documento (2 vCores, 2GB de RAM, 30GB SSD) son equilibradas y precisas.\n\n'
    '2. La dependencia de la aplicacion PHP a un motor de base de datos persistente convierte al almacenamiento '
    '(Disco de Estado Solido) y a la Memoria RAM en los dos elementos de hardware mas criticos del plan de validacion.\n\n'
    '3. Elaborar este plan de validacion antes del despliegue permite garantizar que la aplicacion funcionara de manera '
    'fluida, garantizando una excelente experiencia para el usuario final y previniendo caidas del sistema por agotamiento '
    'de recursos de maquina.\n\n'
    '4. Como Analista y Desarrollador de Software, aplicar los conocimientos sobre Sistemas Operativos de Red y '
    'licenciamiento otorga una vision holistica, donde el codigo y la infraestructura se alinean bajo estandares profesionales.'
)

pdf.chapter_title('7. REFERENCIAS BIBLIOGRAFICAS E INCLUSION DE FUENTES')
pdf.chapter_body(
    'SENA. (2024). Componente Formativo: Sistemas Operativos de Red y Licenciamiento. Territorio SENA.\n\n'
    'PHP Group. (2023). PHP: Instalación y configuración. Recuperado del manual oficial de PHP: https://www.php.net/manual/es/install.php\n\n'
    'Oracle Corporation. (2023). MySQL 8.0 Reference Manual: Hardware configuration. Recuperado de: https://dev.mysql.com/doc/refman/8.0/en/hardware-issues.html\n\n'
    'Canonical Ltd. (2023). Ubuntu Server Documentation: Minimum System Requirements. Recuperado de: https://ubuntu.com/server/docs\n\n'
    'DigitalOcean. (2021). Understanding the LAMP Stack on Linux. DigitalOcean Community Tutorials.'
)

pdf.ln(10)
pdf.set_font('Arial', 'B', 10.5)
pdf.cell(0, 5, '____________________________________________________', 0, 1, 'C')
pdf.cell(0, 5, 'Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.set_font('Arial', '', 9.5)
pdf.cell(0, 4.5, 'Aprendiz / Analista de Pruebas y Calidad de Software', 0, 1, 'C')
pdf.cell(0, 4.5, 'Ficha 3186645 - ADSO SENA Regional Risaralda', 0, 1, 'C')

reporte_path = 'Evidencia_GA10-220501097-AA2-EV01_Validacion_Hardware.pdf'
pdf.output(reporte_path, 'F')
print(f"Reporte de validacion de hardware generado con exito: {reporte_path}")
