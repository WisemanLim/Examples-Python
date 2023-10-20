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
    watermark_string = "{owner}{timestamp}".format(owner="Wise", timestamp=datetime.fromtimestamp(time.time()))
    width = ca._pagesize[0]
    height = ca._pagesize[1]
    ca.setFillColor(colors.grey, alpha=0.6)
    ca.setFont('Helvetica', 30)
    ca.rotate(45)
    print(width, height)
    # ca.drawRightString(width - 25, height - 25, watermark_string)
    ca.drawCentredString((width - (width/3)), height - (height/3), watermark_string)
    return ca

def make_watermark(pdf_filename=None):
    # Init - Create the watermark files
    ca_portrait = Canvas('tmp-portrait.pdf', pagesize=A4)
    ca_landscape = Canvas('tmp-landscape.pdf', pagesize=landscape(A4))

    draw_string(ca_portrait).save()
    draw_string(ca_landscape).save()
    
    #### Use the created watermarks to watermark a file
    source_pdf = PdfFileReader(pdf_filename)
    
    landscape_file = open('tmp-landscape.pdf', 'rb')
    watermark_landscape = PdfFileReader(landscape_file)
    portrait_file = open('tmp-portrait.pdf', 'rb')
    watermark_portrait = PdfFileReader(portrait_file)
    output = PdfFileWriter()
    
    page = source_pdf.getPage(0).mediaBox
    print(page[2], page[3])
    
    for page in source_pdf.pages:
        # Check rotation
        if page.mediaBox.width < page.mediaBox.height:
            page.merge_page(watermark_portrait.pages[0])
        else:
            page.merge_page(watermark_landscape.pages[0])
        output.add_page(page)
    
    watermark_filename = pdf_filename.split('.pdf')[0] + '-watermarked.pdf'
    with open(watermark_filename, 'wb') as file:
        output.write(file)
        
    landscape_file.close()
    portrait_file.close()
    os.remove('tmp-portrait.pdf')
    os.remove('tmp-landscape.pdf')
    
    with open(watermark_filename, "rb") as f: data = f.read()
    f = open(watermark_filename + ".hash", "w")
    f.write("MD5 : {value}".format(value=hashlib.md5(data).hexdigest()))
    f.write("SHA-1 : {value}".format(value=hashlib.sha1(data).hexdigest()))
    f.write("SHA-224 : {value}".format(value=hashlib.sha224(data).hexdigest()))
    f.write("SHA-256 : {value}".format(value=hashlib.sha256(data).hexdigest()))
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
