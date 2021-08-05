# Automatizar

# ¿Cuáles son las responsabilidades/funcionalidades del código?

# 1. Determinar las variables globales

pdf = None
page_width = None
page_height = None
page_inner_width = None
page_inner_height = None

def crearPDF():
    global pdf, page_width, page_inner_width, page_height, page_inner_height

    from fpdf import FPDF

    pdf = FPDF(unit="pt")

    page_width = 595
    page_height = 842

    pdf.add_page()

    left_margin = 24
    right_margin = 24
    top_margin = 24
    bottom_margin = 24

    pdf.set_left_margin(left_margin)
    pdf.set_right_margin(right_margin)
    pdf.set_top_margin(top_margin)

    page_inner_width = page_width - left_margin - right_margin
    page_inner_height = page_height - top_margin - bottom_margin

def guardarPDF():
    global pdf

    pdf.output("reportes/reporte_frutas_auto.pdf")

def crearTitulo():
    global pdf

    pdf.set_font("Times", style="B", size=24)

    pdf.cell(0, h=24, txt="Reporte de Frutas", align="C", ln=1)

    pdf.ln(48)

def crearTabla(frutas):
    global pdf, page_inner_width

    pdf.set_font("Times", style="B", size=12)

    pdf.cell(page_inner_width / 3, h=16, txt="Fruta", align="C", border=1, ln=0)
    pdf.cell(page_inner_width / 3, h=16, txt="Peso", align="C", border=1, ln=0)
    pdf.cell(page_inner_width / 3, h=16, txt="Color", align="C", border=1, ln=1)

    pdf.set_font("Times", style="", size=12)

    for fruta in frutas:
        pdf.cell(page_inner_width / 3, h=16, txt=fruta["nombre"], align="L", border=1, ln=0)
        pdf.cell(page_inner_width / 3, h=16, txt="{}g".format(fruta["peso"]), align="C", border=1, ln=0)
        pdf.cell(page_inner_width / 3, h=16, txt=fruta["color"], align="C", border=1, ln=1)

    pdf.ln(24)

    pdf.cell(page_width - 48, h=1, txt="", align="C", border=1, ln=1)

    pdf.ln(24)

def crearLista(frutas):
    global pdf, page_inner_width

    import requests

    for fruta in frutas:
        url = fruta["url"]
        response = requests.get(url)
        with open("reportes/imagenes/{}.jpg".format(fruta["nombre"].lower()), 'wb') as f:
            f.write(response.content)
            f.close()

            pdf.image("reportes/imagenes/{}.jpg".format(fruta["nombre"].lower()), h=128, x=pdf.get_x(), y=pdf.get_y())

            pdf.set_font("Arial", style="B", size=16)

            pdf.set_y(pdf.get_y() + (128 - 16 * 3) / 2)
            pdf.set_x(page_inner_width / 2)
            pdf.cell(0, h=16, txt="{} {}g".format(fruta["nombre"], fruta["peso"]), align="L", border=0, ln=1)
            pdf.ln(16)
            pdf.set_font("Arial", style="", size=16)
            pdf.set_x(page_inner_width / 2)
            pdf.cell(0, h=16, txt="Descripción: {}".format(fruta["color"]), align="L", border=0, ln=1)
            pdf.set_y(pdf.get_y() + (128 - 16 * 3) / 2)

            pdf.ln(16)
            pdf.cell(page_width - 48, h=1, txt="", align="C", border=1, ln=1)

            pdf.ln(24)

crearPDF()

crearTitulo()

frutas = [
    {
        "nombre": "Manzana",
        "peso": 60,
        "color": "Rojo",
        "url": "https://elegifruta.com.ar/onepage/wp-content/uploads/2017/07/manzana_roja.jpg"
    },
    {
        "nombre": "Mango",
        "peso": 80,
        "color": "Amarillo",
        "url": "https://i.blogs.es/9e2919/platano/450_1000.jpg"
    },
    {
        "nombre": "Pera",
        "peso": 70,
        "color": "Verde",
        "url": "https://i.blogs.es/9e2919/platano/450_1000.jpg"
    },
    {
        "nombre": "Plátano",
        "peso": 65,
        "color": "Amarillo",
        "url": "https://i.blogs.es/9e2919/platano/450_1000.jpg"
    },
]

crearTabla(frutas)

crearLista(frutas)

guardarPDF()