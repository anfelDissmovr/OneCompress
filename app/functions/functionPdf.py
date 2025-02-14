import PyPDF2
import os
from app.config import Config


def dividir_pdf(filepath):
    archivos_generados = [] 

    with open(filepath, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        for i in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])

            output_filename = os.path.join(Config.UPLOAD_FOLDER_PDF, f"page_{i+1}.pdf")

            with open(output_filename, "wb") as output_pdf:
                writer.write(output_pdf)

            archivos_generados.append(output_filename) 
            print(f"✅ Página {i+1} guardada como {output_filename}")

    return archivos_generados