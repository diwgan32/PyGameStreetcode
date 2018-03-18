from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import glob
import hashlib

for f in glob.glob('*.pdf'):
    inputpdf = PdfFileReader(open(f, "rb"))
    a = hashlib.md5(open(fyle, 'rb').read()).hexdigest()

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(a + "Pg%s" % i + f, "wb") as outputStream:
            output.write(outputStream)
