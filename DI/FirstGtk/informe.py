from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors


# Función para crear el informe
def generar_informe():
    # Crear objeto canvas para el PDF
    pdf_file = "informe_albaran.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Agregar el logo
    c.drawImage("ruta_del_logo.png", 250, 770, width=100, height=30)

    # Título de la sección
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 740, "Albará")

    # Tabla de datos de albarán
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.whitesmoke)
    c.rect(90, 720, 400, 100, fill=1)  # Caja de color de fondo
    c.setFillColor(colors.black)

    c.drawString(100, 700, "Número albarán: 1")
    c.drawString(100, 680, "Número cliente: 1")
    c.drawString(100, 660, "Nome cliente: Ana")
    c.drawString(100, 640, "Apellidos: Gago Lima")
    c.drawString(300, 700, "Data: 2-07-2023")
    c.drawString(300, 680, "Data entrega: 15-07-2023")

    # Título de la sección "Detalle"
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 620, "Detalle")

    # Crear tabla de productos
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.whitesmoke)
    c.rect(90, 570, 400, 60, fill=1)  # Caja de fondo
    c.setFillColor(colors.black)

    # Encabezados de la tabla
    c.drawString(100, 550, "Código producto")
    c.drawString(200, 550, "Descripción")
    c.drawString(300, 550, "Cantidad")
    c.drawString(400, 550, "Precio unitario")

    # Datos de los productos
    c.drawString(100, 530, "1")
    c.drawString(200, 530, "Vespa 150")
    c.drawString(300, 530, "1")
    c.drawString(400, 530, "10500")

    c.drawString(100, 510, "2")
    c.drawString(200, 510, "Casco retro")
    c.drawString(300, 510, "2")
    c.drawString(400, 510, "45")

    # Guardar el PDF
    c.save()


# Llamar la función para generar el informe
generar_informe()
