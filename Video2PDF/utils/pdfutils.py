# pdf_splitter.py, pdf_merger2.py : https://www.blog.pythonlibrary.org/2018/04/11/splitting-and-merging-pdfs-with-python/
import os
import glob
import shutil
from PyPDF4 import PdfFileReader, PdfFileWriter, PdfFileMerger

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

def splitter(pdf_filename=None, pages=None):
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
        pages = [i-1 for i in pages]

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

    pdf = PdfFileReader(input_filename, 'rb')
    after_pages = None
    if (pages is not None):
        pages = set_pages(pages)

        for i in range(len(pdf.pages)):
            if i not in pages:
                after_pages = pdf.pages[i]

        splitter(pdf_filename=input_filename, pages=after_pages)
    else:
        pass

def pdf_merge():
    paths = glob.glob('{default_path}{default_split_path}*.pdf'
                      .format(default_path=default_path, default_split_path=default_split_path))
    paths.sort()
    merger(input_paths=paths, merge_filename='{default_path}pdf_merge.pdf'.format(default_path=default_path))


if __name__ == '__main__':
    filename = "꿈 같은 거 없는데요.pdf"
    r_pages = ['1-10', '20', '22-30']
    splitter(pdf_filename=filename, pages=r_pages)

    paths = glob.glob('{default_path}{default_split_path}{filename}'
                      .format(default_path=default_path, default_split_path=default_split_path, filename="*_page_*.pdf"))
    paths.sort()
    merged_filename = filename.split(".pdf")[0]
    merger(input_paths=paths, merge_filename='{default_path}{merged_filename}_merger.pdf'
           .format(default_path=default_path, merged_filename=merged_filename))
