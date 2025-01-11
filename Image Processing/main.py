import pypdf
from pypdf import PdfWriter
from pypdf.annotations import FreeText


def merge(file1, file2):
    """
    Merge two files (or combine).
    :param file1: First file to merge.
    :param file2: Second file to merge.
    :return:
    """
    text = ''
    writer = pypdf.PdfWriter()
    for file in (file1, file2):
        reader = pypdf.PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)
    with open("new.pdf", 'wb') as new_file:
        writer.write(new_file)


def file_watermark(watermark_file, file):
    """
    Watermarks a file.
    :param watermark_file: The file containing the watermark.
    :param file: The file to add the watermark to.
    :return:
    """
    writer = pypdf.PdfWriter()
    reader = pypdf.PdfReader(file)
    for page in reader.pages:
        writer.add_page(page)
    reader = pypdf.PdfReader(watermark_file)
    for page in writer.pages:
        page.merge_page(reader.pages[0], over=False)
    with open("watermarked.pdf", 'wb') as new_file:
        writer.write(new_file)

if __name__ == '__main__':
    file_watermark('wtr.pdf', 'twopage.pdf')