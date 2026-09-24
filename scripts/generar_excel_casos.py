# -*- coding: utf-8 -*-
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# ==========================================
# HOJA 1: FORMATO DE CASOS DE PRUEBA
# ==========================================
ws1 = wb.active
ws1.title = "Casos de Prueba"
ws1.views.sheetView[0].showGridLines = True

# Paleta de colores SENA
verde_sena = "39A900"
verde_oscuro = "1E5B00"
verde_claro = "E8F5E9"
gris_claro = "F4F6F7"
borde_gris = "D0D3D4"

font_titulo = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
font_subtitulo = Font(name="Calibri", size=11, bold=True, color="1E5B00")
font_header_tabla = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
font_bold = Font(name="Calibri", size=10, bold=True, color="000000")
font_normal = Font(name="Calibri", size=10, color="202020")
font_aprobado = Font(name="Calibri", size=10, bold=True, color="1B5E20")

fill_verde_sena = PatternFill(start_color=verde_sena, end_color=verde_sena, fill_type="solid")
fill_verde_oscuro = PatternFill(start_color=verde_oscuro, end_color=verde_oscuro, fill_type="solid")
fill_verde_claro = PatternFill(start_color=verde_claro, end_color=verde_claro, fill_type="solid")
fill_gris = PatternFill(start_color=gris_claro, end_color=gris_claro, fill_type="solid")
fill_aprobado = PatternFill(start_color="C8E6C9", end_color="C8E6C9", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color=borde_gris),
    right=Side(style='thin', color=borde_gris),
    top=Side(style='thin', color=borde_gris),
    bottom=Side(style='thin', color=borde_gris)
)

# Encabezado General
ws1.merge_cells("A1:K1")
ws1["A1"] = "SERVICIO NACIONAL DE APRENDIZAJE - SENA"
ws1["A1"].font = Font(name="Calibri", size=12, bold=True, color="FFFFFF")
ws1["A1"].fill = fill_verde_oscuro
ws1["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[1].height = 24

ws1.merge_cells("A2:K2")
ws1["A2"] = "EVIDENCIA GA9-220501096-AA2-EV01: DISEÑA CASOS Y DEFINE EL AMBIENTE DE PRUEBAS DE SOFTWARE SEGÚN PROYECTO"
ws1["A2"].font = font_titulo
ws1["A2"].fill = fill_verde_sena
ws1["A2"].alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[2].height = 28

# Metadatos del Aprendiz y Proyecto
metadatos = [
    ("Programa:", "Análisis y Desarrollo de Software (ADSO)", "Ficha:", "3186645"),
    ("Aprendiz / Analista:", "Andrés Mauricio Valencia Arango", "Instructor:", "Adornay Sanchez"),
    ("Proyecto:", "Sistema de Gestión Web 'Camila Nails' (React + Node.js + MySQL)", "Fecha de Ejecución:", "Septiembre 2026")
]

row_idx = 4
for label1, val1, label2, val2 in metadatos:
    ws1[f"A{row_idx}"] = label1
    ws1[f"A{row_idx}"].font = font_bold
    ws1[f"A{row_idx}"].fill = fill_verde_claro
    
    ws1.merge_cells(f"B{row_idx}:F{row_idx}")
    ws1[f"B{row_idx}"] = val1
    ws1[f"B{row_idx}"].font = font_normal
    
    ws1[f"G{row_idx}"] = label2
    ws1[f"G{row_idx}"].font = font_bold
    ws1[f"G{row_idx}"].fill = fill_verde_claro
    
    ws1.merge_cells(f"H{row_idx}:K{row_idx}")
    ws1[f"H{row_idx}"] = val2
    ws1[f"H{row_idx}"].font = font_normal
    
    for col in range(1, 12):
        col_letter = get_column_letter(col)
        ws1[f"{col_letter}{row_idx}"].border = thin_border
    
    ws1.row_dimensions[row_idx].height = 20
    row_idx += 1

# Sección: Definición del Ambiente de Pruebas
row_idx += 1
ws1.merge_cells(f"A{row_idx}:K{row_idx}")
ws1[f"A{row_idx}"] = "1. DEFINICIÓN DEL AMBIENTE DE PRUEBAS"
ws1[f"A{row_idx}"].font = font_titulo
ws1[f"A{row_idx}"].fill = fill_verde_oscuro
ws1[f"A{row_idx}"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
ws1.row_dimensions[row_idx].height = 24
row_idx += 1

ambiente_datos = [
    ("Componente", "Detalle Técnico y Configuración del Ambiente"),
    ("Sistema Operativo", "Windows 11 Home / Pro (Arquitectura 64-bit)"),
    ("Servidor de Backend", "Node.js v18+ con Framework Express.js en puerto local http://localhost:4000"),
    ("Motor de Base de Datos", "MySQL Server 8.0 en puerto 3306 (Base de datos: camila_nails)"),
    ("Frontend / Cliente Web", "React.js empaquetado con Vite en entorno http://localhost:5173"),
    ("Navegadores de Prueba", "Google Chrome v128+ y Microsoft Edge para pruebas de compatibilidad y DevTools"),
    ("Herramientas de Pruebas", "Postman v10+ (Pruebas de API REST / Endpoints) y Chrome DevTools (Pruebas de UI/Responsivo)")
]

for item, desc in ambiente_datos:
    is_hdr = (item == "Componente")
    ws1.merge_cells(f"A{row_idx}:C{row_idx}")
    ws1[f"A{row_idx}"] = item
    ws1[f"A{row_idx}"].font = font_header_tabla if is_hdr else font_bold
    ws1[f"A{row_idx}"].fill = fill_verde_sena if is_hdr else fill_verde_claro
    ws1[f"A{row_idx}"].alignment = Alignment(horizontal="center" if is_hdr else "left", vertical="center", indent=1)
    
    ws1.merge_cells(f"D{row_idx}:K{row_idx}")
    ws1[f"D{row_idx}"] = desc
    ws1[f"D{row_idx}"].font = font_header_tabla if is_hdr else font_normal
    ws1[f"D{row_idx}"].fill = fill_verde_sena if is_hdr else PatternFill(fill_type=None)
    ws1[f"D{row_idx}"].alignment = Alignment(horizontal="center" if is_hdr else "left", vertical="center", indent=1)
    
    for col in range(1, 12):
        col_letter = get_column_letter(col)
        ws1[f"{col_letter}{row_idx}"].border = thin_border
        
    ws1.row_dimensions[row_idx].height = 20
    row_idx += 1

# Sección: Formato de Casos de Prueba
row_idx += 1
ws1.merge_cells(f"A{row_idx}:K{row_idx}")
ws1[f"A{row_idx}"] = "2. FORMATO DE MATRIZ DE CASOS DE PRUEBA"
ws1[f"A{row_idx}"].font = font_titulo
ws1[f"A{row_idx}"].fill = fill_verde_oscuro
ws1[f"A{row_idx}"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
ws1.row_dimensions[row_idx].height = 24
row_idx += 1

headers_columnas = [
    ("N° Caso", 10),
    ("Herramienta Utilizada", 16),
    ("Autor del Caso de Prueba", 24),
    ("Descripción / Módulo", 26),
    ("Salida Esperada", 28),
    ("Salida Obtenida", 28),
    ("Resultado", 14),
    ("Seguimiento", 14),
    ("Severidad", 12),
    ("Evidencia", 26),
    ("Firma de Aprobación", 24)
]

for col_i, (h_title, _) in enumerate(headers_columnas, start=1):
    cell = ws1.cell(row=row_idx, column=col_i, value=h_title)
    cell.font = font_header_tabla
    cell.fill = fill_verde_sena
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border

ws1.row_dimensions[row_idx].height = 32
row_idx += 1

autor_firma = "Andrés Mauricio Valencia Arango"

casos = [
    (
        "CP-001",
        "Postman",
        autor_firma,
        "Registro exitoso de nuevo usuario cliente (POST /api/register)",
        "Código HTTP 200 OK con JSON {'success': true, 'message': 'Registro exitoso'}",
        "Código HTTP 200 OK recibido y registro almacenado en tabla 'users' de MySQL",
        "Aprobado",
        "N/A",
        "Baja",
        "Respuesta JSON status 200 en Postman y registro en base de datos",
        autor_firma
    ),
    (
        "CP-002",
        "Postman",
        autor_firma,
        "Validación de campos obligatorios en registro (POST /api/register sin email)",
        "Código HTTP 400 Bad Request con mensaje de error {'error': 'Faltan campos'}",
        "Código HTTP 400 Bad Request retornado correctamente evitando registros incompletos",
        "Aprobado",
        "N/A",
        "Media",
        "Captura de pantalla de Postman con código 400 y mensaje de validación",
        autor_firma
    ),
    (
        "CP-003",
        "Postman",
        autor_firma,
        "Autenticación de usuario administrador en sistema (POST /api/login)",
        "Código HTTP 200 OK retornando datos de usuario y validación de rol 'admin'",
        "Acceso otorgado correctamente con datos de perfil y rol de administrador",
        "Aprobado",
        "N/A",
        "Alta",
        "Validación de contraseña encriptada con bcryptjs y sesión iniciada",
        autor_firma
    ),
    (
        "CP-004",
        "Postman / Chrome",
        autor_firma,
        "Creación manual de Ficha de Cliente desde Panel de Admin (POST /api/fichas)",
        "Registro insertado en tabla 'fichas' con ID autoincremental y mensaje de éxito",
        "Ficha creada satisfactoriamente con Status 200 OK e insertId asignado",
        "Aprobado",
        "N/A",
        "Alta",
        "Inserción reflejada en MySQL y visualización en tiempo real en la UI",
        autor_firma
    ),
    (
        "CP-005",
        "Postman",
        autor_firma,
        "Actualización y edición de datos de cliente (PUT /api/fichas/:id)",
        "Modificación exitosa de nombre, teléfono y servicio devolviendo confirmación",
        "Campos modificados en base de datos con respuesta {'message': 'Ficha actualizada'}",
        "Aprobado",
        "N/A",
        "Media",
        "Petición PUT 200 OK en Postman y actualización visual en la tabla",
        autor_firma
    ),
    (
        "CP-006",
        "Postman",
        autor_firma,
        "Eliminación física de un usuario o ficha (DELETE /api/users/:id)",
        "Registro eliminado de la base de datos MySQL con status 200 OK",
        "Status 200 OK {'message': 'Usuario eliminado'} y registro borrado en DB",
        "Aprobado",
        "N/A",
        "Media",
        "Comprobación de registro ausente tras petición DELETE ejecutada",
        autor_firma
    ),
    (
        "CP-007",
        "Chrome DevTools",
        autor_firma,
        "Contraste y visibilidad de inputs en Modo Oscuro (Formularios Admin)",
        "El texto debe ser claramente legible (blanco sobre fondo oscuro) al escribir",
        "Se detectó fondo blanco en focus que ocultaba texto blanco; corregido en CSS",
        "Aprobado",
        "BUG-UI-01",
        "Media",
        "Regla CSS modificada (App.css) e inspección exitosa en DevTools",
        autor_firma
    ),
    (
        "CP-008",
        "Chrome DevTools",
        autor_firma,
        "Diseño responsivo del Home y Panel en dispositivos móviles (360px a 412px)",
        "Adaptación fluida de columnas a 1 sola columna sin scroll horizontal indeseado",
        "Reorganización de layout exitosa con padding adecuado para móviles y tablets",
        "Aprobado",
        "N/A",
        "Baja",
        "Inspección en modo emulación responsive de Google Chrome",
        autor_firma
    )
]

for cp in casos:
    c_num, c_tool, c_autor, c_desc, c_esp, c_obt, c_res, c_seg, c_sev, c_evi, c_firma = cp
    
    ws1.cell(row=row_idx, column=1, value=c_num).alignment = Alignment(horizontal="center", vertical="center")
    ws1.cell(row=row_idx, column=2, value=c_tool).alignment = Alignment(horizontal="center", vertical="center")
    ws1.cell(row=row_idx, column=3, value=c_autor).alignment = Alignment(horizontal="left", vertical="center")
    ws1.cell(row=row_idx, column=4, value=c_desc).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws1.cell(row=row_idx, column=5, value=c_esp).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    ws1.cell(row=row_idx, column=6, value=c_obt).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    
    res_cell = ws1.cell(row=row_idx, column=7, value=c_res)
    res_cell.alignment = Alignment(horizontal="center", vertical="center")
    res_cell.font = font_aprobado
    res_cell.fill = fill_aprobado
    
    ws1.cell(row=row_idx, column=8, value=c_seg).alignment = Alignment(horizontal="center", vertical="center")
    ws1.cell(row=row_idx, column=9, value=c_sev).alignment = Alignment(horizontal="center", vertical="center")
    ws1.cell(row=row_idx, column=10, value=c_evi).alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    
    firma_cell = ws1.cell(row=row_idx, column=11, value=c_firma)
    firma_cell.alignment = Alignment(horizontal="center", vertical="center")
    firma_cell.font = font_bold
    
    for col in range(1, 12):
        col_letter = get_column_letter(col)
        c = ws1[f"{col_letter}{row_idx}"]
        c.border = thin_border
        if col != 7: # El resultado ya tiene su propio font
            if col != 11:
                c.font = font_normal
            if row_idx % 2 == 0 and col != 11:
                c.fill = fill_gris
                
    ws1.row_dimensions[row_idx].height = 42
    row_idx += 1

# Ajustar ancho de columnas
for col_i, (_, w) in enumerate(headers_columnas, start=1):
    col_letter = get_column_letter(col_i)
    ws1.column_dimensions[col_letter].width = w

# Guardar libro Excel
excel_path = "Evidencia_GA9-220501096-AA2-EV01_CasosPrueba.xlsx"
wb.save(excel_path)
print(f"Archivo Excel generado con éxito: {excel_path}")
