import webbrowser
import os
from fpdf import FPDF
from filestack import Client

class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename) -> object:
        self.filename = filename

    def generate(self, product1, product2, product3, invoice):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Image
        #pdf.image("files\___.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Invoice", border=0, align='C', ln=1)

        # Insert Date
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Date: ", border=0)
        pdf.cell(w=150, h=40, txt=str(invoice.date), border=0, ln=1)

        # Insert Customer Name
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Customer: ", border=0)
        pdf.cell(w=150, h=40, txt=str(invoice.name), border=0, ln=1)

        # Insert Product Name and Price
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=str(product1.name), border=0)
        pdf.cell(w=25, h=25, txt=str(product1.price), border=0, ln=1)

        # Insert Product Name and Price
        pdf.cell(w=100, h=25, txt=str(product2.name), border=0)
        pdf.cell(w=25, h=25, txt=str(product2.price), border=0, ln=1)

        # Insert Product Name and Price
        pdf.cell(w=100, h=25, txt=str(product3.name), border=0)
        pdf.cell(w=25, h=25, txt=str(product3.price), border=0, ln=1)

        # Insert Total Price
        pdf.cell(w=100, h=40, txt="Total = ",  border="T", align="R")
        pdf.cell(w=25, h=40, txt=str(invoice.total), border="T")

        # Change directory
        os.chdir("pdfs")
        # Ouput PDF
        pdf.output(self.filename)
        # Auto open in windows
        webbrowser.open(self.filename)
        
class FileSharer:

    def __init__(self, filepath, api_key='AViVqp7suSQWWEdrl6hf9z'):
        self.api_key = api_key
        self.filepath = filepath
    # Uploads File and outputs URL link
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
