import PyPDF2 as pdf

# To open a file
path = r'C:\Users\abhay\Desktop\TSQL_concepts.pdf'
file = open(path, 'rb')

# To read the file and create an object
pdf_reader = pdf.PdfFileReader(file)

# To read the data
print("The data is in", pdf_reader)

# To count the number of pages
print(pdf_reader.getNumPages())

# To get the information from the PDF at page 1, therefore we use index 0
page1 = pdf_reader.getPage(0)

# To print the data
print(page1)

# To extract the text
print(page1.extractText())

# Similarly for extracting page1
page2 = pdf_reader.getPage(1)

print(page2.extractText())
