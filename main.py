# This is a PDF generator

from datetime import date
from pdfreport import PdfReport, FileSharer
from product import Invoice, Product

# Take user inputs and create instances
customer_name = (input("What is the customer's name? Enter: "))
name1 = input("Name of purchased product? Enter: ")
price1 = int(input(f"Price of {name1}? Enter: "))
name2 = input("Name of purchased product? Enter: ")
price2 = int(input(f"Price of {name2}? Enter: "))
name3 = input("Name of purchased product? Enter: ")
price3 = int(input(f"Price of {name3}? Enter: "))
total = price1+price2+price3

# Create instances of objects
the_invoice = Invoice(date= date.today(), name=customer_name, total=total)
product1 = Product(name=name1, price= price1)
product2 = Product(name=name2, price= price2)
product3 = Product(name=name3, price= price3)

# Generate PDF
pdf_report = PdfReport(filename=f"Invoice_{the_invoice.date}_{the_invoice.name}.pdf")
pdf_report.generate(product1=product1, product2=product2,product3 = product3, invoice=the_invoice)

# Share file on Cloud
file_sharer = FileSharer(filepath = pdf_report.filename)
print(file_sharer.share())
