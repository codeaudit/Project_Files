import os
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
pdfPath= '/home/achndrs4/neh/Extracted_Texts/'
fileNames= os.listdir(pdfPath)
for fil in fileNames:
    if fil.endswith(".pdf"):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(pdfPath+fil, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
            text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.seek(0)
        newfile = open(pdfPath+fil[:-4]+".txt", "w+")
        newfile.write(text)

print('Done')






