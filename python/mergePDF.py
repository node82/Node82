import PyPDF2
# open two pdfs
pdf1File = open('example.pdf', 'rb')
pdf2File = open('example2.pdf', 'rb')
# read first pdf
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# read second pdf
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
# for writing in new pdf file
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
# create new pdf 'example3.pdf' 
pdfOutputFile = open('example3.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close(
