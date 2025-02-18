from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from conexionBD import ConexionBD


def generar_albaran_pdf(numero_albaran, nombre_archivo):
    # Conectar a la base de datos
    conexion = ConexionBD("modelosClasicos.dat")
    conexion.conectaBD()
    conexion.creaCursor()

    try:
        # query albaran
        consulta_albaran = "SELECT * FROM ventas WHERE numeroAlbara = ?"
        albaran = conexion.consultaConParametros(consulta_albaran, numero_albaran)
        if not albaran:
            print("No se encontró el albarán.")
            return
        albaran = albaran[0]

        # query cliente
        consulta_cliente = "SELECT * FROM clientes WHERE numeroCliente = ?"
        cliente = conexion.consultaConParametros(consulta_cliente, albaran[3])
        if not cliente:
            print("No se encontró el cliente.")
            return
        cliente = cliente[0]

        # qurey detalles
        consulta_detalle = "SELECT * FROM detalleVentas WHERE numeroAlbaran = ?"
        detalles = conexion.consultaConParametros(consulta_detalle, numero_albaran)
        if not detalles:
            print("No se encontraron detalles de venta.")
            return

        # Query productos
        productos = []
        for detalle in detalles:
            consulta_producto = "SELECT * FROM produtos WHERE codigoProduto = ?"
            producto = conexion.consultaConParametros(consulta_producto, detalle[1])
            if producto:
                productos.append(producto[0])



        # Crear PDF
        doc = SimpleDocTemplate(nombre_archivo, pagesize=A4)
        elementos = []
        styles = getSampleStyleSheet()

        # --- Encabezado "Albarán" ---
        elementos.append(Paragraph("<b>ALBARÁN</b>", styles["Title"]))
        elementos.append(Spacer(1, 12))

        # --- Datos del albarán ---
        tabla_albaran = Table([
            ["Número de Albarán", albaran[0], "Data", albaran[1]],
            ["Número de Cliente", cliente[0], "Data Entrega", albaran[2]],
            ["Nome Cliente", cliente[1], "Apelidos", f"{cliente[2]} {cliente[3]}"],
        ])

        tabla_albaran.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 2), colors.lightgrey),
            ('BACKGROUND', (2, 0), (-1, 1), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 3), 'Helvetica-Bold')
        ]))
        elementos.append(tabla_albaran)
        elementos.append(Spacer(1, 12))

        # --- Encabezado "Detalle" ---
        elementos.append(Paragraph("<b>DETALLE</b>", styles["Title"]))
        elementos.append(Spacer(1, 12))

        # --- Datos de productos ---
        datos_productos = [["Código Produto", "Descripción", "Cantidade", "Precio Unitario"]]
        for detalle, producto in zip(detalles, productos):
            print(f"Detalle: {detalle}, Producto: {producto}")  # Depuración
            datos_productos.append([producto[0], producto[1], detalle[2], detalle[3]])

        tabla_detalle = Table(datos_productos)

        tabla_detalle.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
        ]))
        elementos.append(tabla_detalle)

        # Guardar el PDF
        doc.build(elementos)
        print(f"Albarán guardado en {nombre_archivo}")

    except Exception as e:
        print(f"Error generando el albarán: {e}")

    finally:
        # Cerrar la conexión a la base de datos
        conexion.pechaBD()


# Ejemplo de uso
generar_albaran_pdf(1, "albaran.pdf")
