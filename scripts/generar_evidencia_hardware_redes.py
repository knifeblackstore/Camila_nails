# -*- coding: utf-8 -*-
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Arial', 'B', 9)
            self.set_text_color(70, 70, 70)
            self.cell(0, 6, 'SENA | Analisis y Desarrollo de Software (ADSO) - Ficha 3186645', 0, 1, 'C')
            self.set_draw_color(57, 169, 0)
            self.set_line_width(0.4)
            self.line(12, 16, 198, 16)
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(110, 110, 110)
        self.cell(0, 10, 'Evidencia GA10-220501097-AA1-EV01 | Pagina ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(232, 245, 233)
        self.set_text_color(25, 80, 0)
        self.cell(0, 8, '  ' + title, 0, 1, 'L', 1)
        self.ln(3)

    def chapter_subtitle(self, subtitle):
        self.set_font('Arial', 'B', 10.5)
        self.set_text_color(35, 35, 35)
        self.cell(0, 6.5, subtitle, 0, 1, 'L')
        self.ln(1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, body)
        self.ln(3)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# --- PORTADA ---
pdf.add_page()
pdf.set_y(45)
pdf.set_font('Arial', 'B', 11)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 6, 'SERVICIO NACIONAL DE APRENDIZAJE - SENA', 0, 1, 'C')
pdf.cell(0, 6, 'CENTRO DE FORMACION TECNOLOGICA | REGIONAL RISARALDA', 0, 1, 'C')
pdf.ln(15)

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(25, 80, 0)
pdf.multi_cell(0, 8, 'EVIDENCIA GA10-220501097-AA1-EV01\nConceptos y principios de hardware e instalacion de software', align='C')
pdf.ln(20)

pdf.set_font('Arial', '', 12)
pdf.set_text_color(40, 40, 40)
pdf.cell(0, 7, 'Programa de Formacion: Analisis y Desarrollo de Software (ADSO)', 0, 1, 'C')
pdf.cell(0, 7, 'Numero de Ficha: 3186645', 0, 1, 'C')
pdf.cell(0, 7, 'Aprendiz: Andres Mauricio Valencia Arango', 0, 1, 'C')
pdf.cell(0, 7, 'Instructor: Adornay Sanchez', 0, 1, 'C')
pdf.ln(15)
pdf.cell(0, 7, 'Pereira, Risaralda - 2026', 0, 1, 'C')

# --- INTRODUCCIÓN ---
pdf.add_page()
pdf.chapter_title('1. INTRODUCCION')
pdf.chapter_body(
    'En el desarrollo y despliegue de soluciones informáticas, como es el caso del proyecto web "Camila Nails", la codificación es solo una parte del proceso. Para que la aplicación sea accesible a los usuarios, es imperativo establecer una infraestructura tecnológica subyacente robusta. Esto implica tomar decisiones críticas sobre el hardware, el sistema operativo del servidor y comprender los fundamentos de redes que permitirán la comunicación entre el cliente y el servidor.\n\n'
    'Este informe detalla los conceptos esenciales de redes y networking necesarios para la fase de implantación. Se analiza el sistema operativo óptimo para alojar la aplicación, se identifican las entidades globales que estandarizan las telecomunicaciones, se exploran las familias de protocolos de transmisión de datos (OSI y TCP/IP) y se categorizan los medios físicos y lógicos por donde viaja la información.'
)

# --- OBJETIVO ---
pdf.chapter_title('2. OBJETIVO')
pdf.chapter_body(
    'Consolidar los conceptos fundamentales de infraestructura tecnológica, hardware, instalación de software de servidor y networking, con el propósito de fundamentar teóricamente el proceso de alistamiento e implantación del proyecto de software "Camila Nails" en un entorno productivo.'
)

# --- DESARROLLO DE LA TEMÁTICA ---
pdf.chapter_title('3. DESARROLLO DE LA TEMATICA')

pdf.chapter_subtitle('3.1. Caracteristicas del Sistema Operativo Seleccionado')
pdf.chapter_body(
    'Para el despliegue del backend en Node.js y la base de datos MySQL de "Camila Nails", la plataforma seleccionada es GNU/Linux, especificamente la distribucion Ubuntu Server 22.04 LTS o 24.04 LTS. Las caracteristicas que fundamentan esta eleccion son:\n\n'
    '- Estabilidad y Rendimiento: Linux gestiona eficientemente los recursos de hardware (CPU, RAM), permitiendo ejecutar servicios continuos (daemons) sin necesidad de una interfaz gráfica que consuma recursos innecesarios.\n'
    '- Seguridad Robusta: Posee sistemas avanzados de permisos de usuarios, firewalls integrados (UFW/iptables) y actualizaciones criticas constantes, vital para proteger la base de datos de clientes.\n'
    '- Compatibilidad Nivel Empresarial: Node.js, PM2 (gestor de procesos) y MySQL tienen soporte nativo y un rendimiento optimizado en entornos Unix/Linux.\n'
    '- Software Libre y Costo Eficiente: Al ser de codigo abierto, elimina costos de licenciamiento de sistema operativo, permitiendo invertir presupuesto en mejor hardware o servicios en la nube (AWS, DigitalOcean).'
)

pdf.chapter_subtitle('3.2. Organizaciones Estandarizadoras de Redes y Networking')
pdf.chapter_body(
    'Para asegurar que dispositivos de diferentes fabricantes puedan comunicarse entre si en internet, existen entidades que definen reglas y estandares globales:\n\n'
    '1. IEEE (Institute of Electrical and Electronics Engineers): Define estándares físicos y de enlace de datos, siendo su contribución más famosa la norma IEEE 802.3 (Ethernet) e IEEE 802.11 (Wi-Fi).\n'
    '2. ISO (International Organization for Standardization): Creadores del famoso Modelo OSI, un marco de referencia vital para entender cómo se estructuran las comunicaciones en red.\n'
    '3. IETF (Internet Engineering Task Force): Encargados de desarrollar y promover los estándares de Internet (como TCP/IP, HTTP, DNS) documentados a través de los RFC (Request for Comments).\n'
    '4. ITU-T (International Telecommunication Union - Telecommunication Standardization Sector): Regula estándares internacionales de telecomunicaciones, especialmente en transmisión de voz, video y fibra óptica.'
)

pdf.chapter_subtitle('3.3. Familias de Protocolos de Transmision y Recepcion de Datos')
pdf.chapter_body(
    'Los protocolos son conjuntos de reglas que dictan cómo se formatean, transmiten y reciben los datos. Las dos grandes familias o modelos arquitectónicos son:\n\n'
    'A) Modelo OSI (Open Systems Interconnection):\n'
    'Es un modelo conceptual de 7 capas (Fisica, Enlace de datos, Red, Transporte, Sesion, Presentacion, Aplicacion). Sirve principalmente como herramienta educativa y de diseno para estructurar como la información viaja desde el cable físico hasta el navegador del usuario.\n\n'
    'B) Modelo TCP/IP (Transmission Control Protocol / Internet Protocol):\n'
    'Es el modelo practico y el estandar de facto en el que se basa Internet hoy en dia. Se divide en 4 capas operativas:\n'
    '- Acceso a la Red (hardware y direcciones MAC).\n'
    '- Internet (IP, enrutamiento de paquetes).\n'
    '- Transporte (TCP para transmision confiable, UDP para velocidad).\n'
    '- Aplicacion (HTTP/HTTPS, FTP, SMTP, usados por proyectos web como Camila Nails para transferir los JSON de la API).'
)

pdf.chapter_subtitle('3.4. Medios de Transmision (Guiados y No Guiados)')
pdf.chapter_body(
    'El canal por donde viajan las señales electromagneticas o lumninicas entre el servidor y los clientes se divide en dos grandes grupos:\n\n'
    '1. Medios Guiados (Alámbricos):\n'
    'Confinan la señal a traves de un medio fisico tangible. Ejemplos:\n'
    '- Cable de Par Trenzado (Cobre): Como el UTP Cat6, muy usado en redes LAN.\n'
    '- Cable Coaxial: Usado en conexiones de banda ancha de proveedores de internet.\n'
    '- Fibra Optica: Transmite datos como pulsos de luz. Es crucial para conectar los grandes centros de datos (Datacenters) donde estara alojado el servidor de la aplicacion, ofreciendo la mayor velocidad y ancho de banda.\n\n'
    '2. Medios No Guiados (Inalámbricos):\n'
    'Transmiten las ondas electromagneticas a traves del aire o el vacio, sin un conducto fisico restrictivo. Ejemplos:\n'
    '- Radiofrecuencias (Wi-Fi, Bluetooth).\n'
    '- Microondas (Terrestres y satelitales, utiles para conectar zonas remotas).\n'
    '- Redes Celulares (4G LTE, 5G), fundamentales para que los clientes accedan a la aplicacion desde sus dispositivos moviles.'
)

# --- CONCLUSIONES ---
pdf.chapter_title('4. CONCLUSIONES')
pdf.chapter_body(
    '- La selección de un sistema operativo orientado a servidores, como Ubuntu Linux, es una decisión estratégica que impacta directamente en el rendimiento, la seguridad y los costos de operación durante la implantación del software.\n'
    '- Comprender las entidades estandarizadoras y los modelos de red (TCP/IP y OSI) es esencial para el tecnólogo ADSO, ya que permite diagnosticar problemas de conectividad (troubleshooting) y entender cómo la aplicación web interactúa con el mundo exterior.\n'
    '- La infraestructura física, compuesta por medios guiados y no guiados, dicta las limitaciones de latencia y velocidad; diseñar un software optimizado ayuda a mitigar las restricciones inherentes a las redes inalámbricas o conexiones de bajo ancho de banda.'
)

# --- REFERENCIAS BIBLIOGRÁFICAS ---
pdf.add_page()
pdf.chapter_title('5. REFERENCIAS BIBLIOGRAFICAS')
pdf.chapter_body(
    'Cisco Networking Academy. (2020). Introduction to Networks Companion Guide (CCNAv7). Cisco Press.\n\n'
    'Kurose, J. F., & Ross, K. W. (2021). Computer Networking: A Top-Down Approach (8th ed.). Pearson.\n\n'
    'Stallings, W. (2014). Data and Computer Communications (10th ed.). Pearson.\n\n'
    'Tanenbaum, A. S., & Wetherall, D. J. (2011). Redes de computadoras (5ta ed.). Pearson Educacion.'
)

pdf.output('Evidencia_GA10-220501097-AA1-EV01_Hardware_Redes.pdf', 'F')
print("PDF generado correctamente.")
