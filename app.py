import PyPDF2

## Copy pdf to another with rotate
with open("coloringBook.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("rotated1.pdf", "wb") as output:
        writer.write(output)

## Merge two PDF files in one
merger = PyPDF2.PdfMerger()
file_names = ["coloringBook.pdf", "rotated.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")
