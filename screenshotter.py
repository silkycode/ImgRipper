import sys
from PyPDF2.merger import PdfFileMerger
import mouse
import time
from PIL import ImageGrab

def clickGrab(n):
    page = 1
    pdfs = []
    for i in range(n):
        pagename = str(page) + ".pdf"
        pdfs.append(pagename)
        time.sleep(0.5)
        im = ImageGrab.grab()
        im.save(pagename)
        im.close()
        page += 1
        mouse.move(1882, 1043, absolute=True, duration=0)
        mouse.click(button='left')
    return pdfs

def pdfMerge(list):
    merger = PdfFileMerger()
    for pdf in list:
        merger.append(pdf)
    merger.write("product.pdf")
    merger.close()

pdfMerge(clickGrab(int(sys.argv[1])))
