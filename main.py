from PyPDF2 import PdfFileReader, PdfFileWriter
import math
import os


def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print(number_of_pages)
    print(info)

    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title


if __name__ == '__main__':
    path = r'C:\Users\suhorukov.iv\Desktop\test'
    full_name = r'test.pdf'
    # get_info(path)
    file_name = full_name[:full_name.rfind('.')]
    file_type = full_name[full_name.rfind('.') + 1:]

    page_in_result_file = 4

    input_PDF = PdfFileReader(open(f'{path}\\{full_name}', 'rb'))

    output = PdfFileWriter()
    for i in range(input_PDF.getNumPages()):
        new_File_PDF = input_PDF.getPage(i)
        output.addPage(new_File_PDF)

        if i % page_in_result_file == 0 or i + 1 == input_PDF.getNumPages():
            output_Name_File = f'{file_name}_{math.ceil((i + 1) / page_in_result_file)}.{file_type}'
            outputStream = open(f'{path}\\{output_Name_File}', 'wb')
            output.write(outputStream)
            outputStream.close()

            output = PdfFileWriter()
