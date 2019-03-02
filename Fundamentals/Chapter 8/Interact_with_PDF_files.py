# -------------------------------
# Example 1 - Reading basic PDF data
# -------------------------------

# PyPDF2 uses a separate reading(PDFFileReader) and writing(PDFileWriter) process  
import os
import PyPDF2

# find path of script file to allow for use of relative paths
path = os.path.dirname(__file__)

input_file_name = os.path.join(path, "examplefiles\pride.pdf")
# rb must be used to open the file in binary mode rather than text mode as we are working with a PDF
input_file = PyPDF2.pdf.PdfFileReader(open(input_file_name, "rb"))

# get methods can be used to get data out of the loaded pdf
# The examples below collect metadata from the PDF
print("Number of pages:", input_file.getNumPages())
print("Title:", input_file.getDocumentInfo().title)
print(input_file.getDocumentInfo())

# we can get data from a specific page of the PDF
pagetext = input_file.getPage(0).extractText()
print(pagetext) 


# -------------------------------
# Example 2 - Variable PDF Formating
# -------------------------------

# PDF formating is highly variable so it's important to know what kind of PDF you're working with
# in the example above the text does not use /n for newlines instead using a bunch of space so in
# order to write the text out to a .txt document we we need to reformat it.

output_file_name = os.path.join(path, "examplefiles\Pride and Prejudice.txt")
with open(output_file_name, "w") as output_file:
    title = input_file.getDocumentInfo().title # get PDF title
    total_pages = input_file.getNumPages() # get the total page count

    output_file.write(title + "\n")
    output_file.write("Number of pages: {}\n\n".format(total_pages))

    for page_num in range(0, total_pages):
        text = input_file.getPage(page_num).extractText()
        text = text.replace("   ", "\n")
        output_file.write(text)


# -------------------------------
# Example 3 - Modifying a PDF
# -------------------------------
# program to copy the first 3 pages of a PDF into a new file
output_PDF = PyPDF2.pdf.PdfFileWriter()

for page_num in range(1, 4):
    output_PDF.addPage(input_file.getPage(page_num))

output_file_name = os.path.join(path, "output\portion.pdf")
with open(output_file_name, "wb") as output_file:
    output_PDF.write(output_file)


# *******************************
# Exercises
# *******************************

# 1. Write a script that opens the file named The Whistling Gypsy.pdf from the Chapter
# 11 practice files, then displays the title, author, and total number of pages in the file
import os
import PyPDF2

path = os.path.dirname(__file__)
input_file_name = os.path.join(path, "examplefiles\The Whistling Gypsy.pdf")

input_file = PyPDF2.pdf.PdfFileReader(open(input_file_name, "rb"))
print("Title:", input_file.getDocumentInfo().title)
print("Author:", input_file.getDocumentInfo().author)
print("Total Pages:", input_file.getNumPages())


# 2. Extract the full contents of The Whistling Gypsy.pdf into a .TXT file
with open("Gypsy.txt", "w") as output_file:
    for page_num in range(0, input_file.getNumPages()):
        text = input_file.getPage(page_num).extractText()
        text = text.encode("utf-8")
        output_file.write(str(text))
