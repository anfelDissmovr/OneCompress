import fitz
import os
from app.config import Config
from app.functions.function2d import resize_img


def convertir_pdf_a_jpg(pdf_path, target_width=2200, target_height=1238):
    FileName = os.path.basename(pdf_path)
    FolderName = os.path.splitext(FileName)[0]
    output_folder = os.path.join(Config.UPLOAD_FOLDER_PDF, FolderName)
    print(output_folder)
    os.makedirs(output_folder, exist_ok=True)

    ListImg = []

    pdf_document = fitz.open(pdf_path)

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        
        page_width = page.rect.width
        page_height = page.rect.height

        zoom_x = target_width / page_width
        zoom_y = target_height / page_height
        mat = fitz.Matrix(zoom_x, zoom_y)

        pix = page.get_pixmap(matrix=mat)

        jpg_name = os.path.join(output_folder, f"pagina{page_number + 1}.jpg")
        pix.save(jpg_name)
        ListImg.append(jpg_name)


    pdf_document.close()
    return ListImg
