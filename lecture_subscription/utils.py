from django.core.files.storage import FileSystemStorage


# function to save all pdf documents
def save_pdf(pdf_file):
    fs = FileSystemStorage()
    return fs.save(pdf_file.name, pdf_file)