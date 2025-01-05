import os
from pypdf import PdfReader, PdfWriter

def compress_pdf(input_pdf):
    # Baca PDF asal
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

   
    for page in reader.pages:
        writer.add_page(page)

    # Tetapkan nama fail output
    base_name, ext = os.path.splitext(input_pdf)
    output_pdf = f"{base_name}_compressed{ext}"

    # Simpan fail output
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    print(f"PDF has been successfully compressed and saved as '{output_pdf}'.")

if __name__ == "__main__":
   
    input_pdf = input("Enter the path and name of the PDF file:").strip()

    
    if os.path.isfile(input_pdf):
        compress_pdf(input_pdf)
    else:
        print(f"File '{input_pdf}' does not exist. Please check the path and try again.")
