import os
from PyPDF2 import PdfFileReader

path = "c:/Users/Marc/downloads/"
infile = input("Enter a PDF file name: ")

if len(infile) > 0:
    input_file_name = os.path.join(path, infile)
else:
    input_file_name = os.path.join(path, "Backupify-Office-365-User-Guide.pdf")

input_file = PdfFileReader(open(input_file_name, "rb"))

output_file_name = os.path.join(path, "Output_365_Guide.txt")
output_file = open(output_file_name, "w")


title = input_file.getDocumentInfo().title
total_pages = input_file.getNumPages()
if title != None :
    output_file.write(title + "\n")

output_file.write("Number of Page: {} \n\n".format(total_pages))


for page_num in range(0, total_pages):
    text = input_file.getPage(page_num).extractText()
    text = text.replace("  ", "\n")
    output_file.write(text)

output_file.close()


