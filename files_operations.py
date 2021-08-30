from PyPDF2 import PdfFileReader, PdfFileWriter


def merger(files, output):

    """for merging"""
    writes = PdfFileWriter()
    # merge = PyPDF2.PdfFileMerger()
    for file in files:
        read = PdfFileReader(file)
        for page in range(read.getNumPages()):
            # Add each page to the writer object
            writes.addPage(read.getPage(page))
    # Write out the merged PDF
    with open(output, 'wb') as out:
        writes.write(out)
    # print(read)
    # with open(output, 'wb') as f:
    #     merge.write(f)
    # # with open(output,'wb') as f:


files = ['Python-OOP.pdf', 'Python-OOP 11.pdf']
output = 'merge.pdf'
merger(files, output)
