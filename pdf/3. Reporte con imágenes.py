# pip install fpdf

from fpdf import FPDF

pdf = FPDF(unit="pt")

pdf.add_page()

pdf.set_font("Times", style="B", size=24)

pdf.cell(0, 24, txt="Reporte con Imágenes", align="C", ln=1)

page_size = 595 # A4: 595pt x 842pt (en modo vertical)

pdf.image("reportes/graficas/g2.png", x = page_size / 4, w = page_size / 2)

pdf.set_font("Arial", style="I", size=10)

pdf.cell(0, 10, txt="Histograma de edades", align="C", ln=1)

pdf.output("reportes/reporte_con_imagenes.pdf")