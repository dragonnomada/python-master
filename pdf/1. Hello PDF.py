# pip install fpdf

from fpdf import FPDF

pdf = FPDF()

pdf.output("reportes/hello.pdf")