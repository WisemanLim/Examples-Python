# pdf_splitter.py, pdf_merger2.py : https://www.blog.pythonlibrary.org/2018/04/11/splitting-and-merging-pdfs-with-python/
import os
import glob
import shutil
from PyPDF4 import PdfFileReader, PdfFileWriter, PdfFileMerger
# Watermark : https://www.makeuseof.com/python-pdf-text-watermark-add/, https://github.com/jonasmalm/pdf-watermarker/blob/main/watermark.py
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
# Watermark string, timestamp : https://inma.tistory.com/96
from datetime import datetime
import time
# Make hash info after watermark : https://sens.tistory.com/536
import hashlib

default_path = "./pdf/"
default_split_path = "split/"

def set_pages(pages=None):
    out_pages = []
    for o in pages:
        if (o.find("-") > 0):
            pages = o.split("-")
            for i in range(int(pages[0]), int(pages[1])+1):
                out_pages.append(i)
        else:
            out_pages.append(int(o))

    return out_pages

def splitter(pdf_filename=None, pages=None, delete=False):
    outfile = os.path.splitext(os.path.basename(pdf_filename))[0]
    split_path = "{default_path}{default_split_path}".format(default_path=default_path, default_split_path=default_split_path)

    try:
        shutil.rmtree(split_path)
        os.makedirs(split_path)
    except Exception as error:
        print(error)

    pdf = PdfFileReader(pdf_filename)
    if (pages is None):
        pages = []
        for page in range(pdf.getNumPages()):
            pages.append(page)
    else:
        if (delete != True):
            pages = [i-1 for i in pages]
        else:
            after_pages = []
            for page in range(pdf.getNumPages()):
                if (page+1) not in pages:
                    after_pages.append(page)
            pages = after_pages

    for page in pages:
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{default_path}{default_split_path}{outfile}_page_{page}.pdf'\
            .format(default_path=default_path, default_split_path=default_split_path, outfile=outfile, page=str(page + 1).zfill(5))

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        # print('Created: {output_filename}'.format(output_filename=output_filename))

def merger(input_paths=None, merge_filename=None):
    pdf_merger = PdfFileMerger()

    for path in input_paths:
        pdf_merger.append(path)

    with open(merge_filename, 'wb') as fileobj:
        pdf_merger.write(fileobj)

def pdf_split(pdf_filename=None, pages=None):
    # filename = "꿈 같은 거 없는데요.pdf"
    input_filename = '{default_path}{filename}'.format(default_path=default_path, filename=pdf_filename)
    if (pages is not None):
        pages = set_pages(pages)
        splitter(pdf_filename=input_filename, pages=pages)
    else:
        splitter(pdf_filename=input_filename)

def pdf_delete(pdf_filename=None, pages=None):
    # filename = "꿈 같은 거 없는데요.pdf"
    input_filename = '{default_path}{filename}'.format(default_path=default_path, filename=pdf_filename)
    if (pages is not None):
        pages = set_pages(pages)
        splitter(pdf_filename=input_filename, pages=pages, delete=True)
    else:
        splitter(pdf_filename=input_filename)

def pdf_merge():
    paths = glob.glob('{default_path}{default_split_path}*.pdf'
                      .format(default_path=default_path, default_split_path=default_split_path))
    paths.sort()
    merger(input_paths=paths, merge_filename='{default_path}pdf_merge.pdf'.format(default_path=default_path))

def draw_string(ca=None, watermark_string=None):
    width = ca._pagesize[0]
    height = ca._pagesize[1]
    ca.setFillColor(colors.grey, alpha=0.6)
    ca.setFont('Helvetica', 50)
    ca.rotate(45)
    # print(int(width) - int(width/8), int(height/13))
    # ca.drawRightString(width - 25, height - 25, watermark_string)
    if (watermark_string == None):
        ca.drawCentredString(int(width) - int(width/8), int(height/13)+50, "{owner}".format(owner="Wise"))
        ca.drawCentredString(int(width) - int(width/8), int(height/13),
                             "{timestamp}".format(timestamp=datetime.fromtimestamp(time.time())))
    else:
        ca.drawCentredString(int(width) - int(width/8), int(height/13), "{watermark_string}".format(watermark_string=watermark_string))
    return ca

def make_watermark(pdf_filename=None):
    # Use the created watermarks to watermark a file
    source_pdf = PdfFileReader(pdf_filename)
    page = source_pdf.getPage(0).mediaBox
    width = page[2]
    height = page[3]

    # Init - Create the watermark files
    wm_filename = 'tmp-wartermark.pdf'
    ca = Canvas(wm_filename, pagesize=(width, height))
    draw_string(ca).save()
    ca_filename = open(wm_filename, 'rb')
    watermark_pdf = PdfFileReader(ca_filename)
    output = PdfFileWriter()

    for i in range(source_pdf.getNumPages()):
        pdf_page = source_pdf.getPage(i)
        pdf_page.mergePage(watermark_pdf.pages[0])
        output.addPage(pdf_page)
    
    watermark_filename = pdf_filename.split('.pdf')[0] + '-watermarked.pdf'
    with open(watermark_filename, 'wb') as file:
        output.write(file)
        
    ca_filename.close()
    os.remove(wm_filename)
    
    with open(watermark_filename, "rb") as f: data = f.read()
    f = open(watermark_filename + ".hash", "w")
    f.write("MD5 : {value}\n".format(value=hashlib.md5(data).hexdigest()))
    f.write("SHA-1 : {value}\n".format(value=hashlib.sha1(data).hexdigest()))
    f.write("SHA-224 : {value}\n".format(value=hashlib.sha224(data).hexdigest()))
    f.write("SHA-256 : {value}\n".format(value=hashlib.sha256(data).hexdigest()))
    f.close()

if __name__ == '__main__':
    filename = "../in/꿈 같은 거 없는데요.pdf"
    # r_pages = ['1-10', '20', '22-30']
    # splitter(pdf_filename=filename, pages=r_pages)
    #
    # paths = glob.glob('{default_path}{default_split_path}{filename}'
    #                   .format(default_path=default_path, default_split_path=default_split_path, filename="*_page_*.pdf"))
    # paths.sort()
    # merged_filename = filename.split(".pdf")[0]
    # merger(input_paths=paths, merge_filename='{default_path}{merged_filename}_merger.pdf'
    #        .format(default_path=default_path, merged_filename=merged_filename))
    # Test watermark
    make_watermark(pdf_filename=filename)
