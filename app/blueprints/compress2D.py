import os
import requests
from flask import render_template, request, session, current_app, Blueprint, jsonify
from werkzeug.utils import secure_filename
from app.form import ImageUploadForm, FormStorage
from app.functions.function2d import change_path, resize_img, loop_compress

compress2D = Blueprint('Compress2D', __name__)

@compress2D.route('', methods=['GET', 'POST'])
def index():
    form = ImageUploadForm()
    formStorage = FormStorage()

    if form.validate_on_submit():
        images = request.files.getlist('images')
        quality = form.Quality.data
        session['quality'] = quality
        session['weight'] = form.Weight.data
        session['width'] = form.Width.data
        session['height'] = form.Height.data

        if images:
            saved_files = []

            # Ruta carpeta "originales"
            originals_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'originales')
            os.makedirs(originals_folder, exist_ok=True)

            for image in images:
                filename = secure_filename(image.filename)
                filepath = os.path.join(originals_folder, filename)
                image.save(filepath)
                relative_path = os.path.relpath(filepath, os.path.join(os.getcwd(), 'app/static'))
                filename_without_extension = os.path.splitext(filename)[0]
                saved_files.append((relative_path, filename_without_extension))

            session['saved_files'] = saved_files
            return render_template('compress2d/compress2d.html', formStorage=formStorage, imagesForm=form, saved_files=saved_files)

    return render_template('compress2d/compress2d.html', imagesForm=form, formStorage=formStorage, titulo="Compress 2D Img")


@compress2D.route('compressing', methods=['POST'])
def Compress2d():
    saved_files = session.get('saved_files')
    quality = session.get('quality')
    weight = session.get('weight')
    show_popup = False
    message = ""
    ImgConverted = 0
    total_images = len(saved_files)

    for file in saved_files:
        full_path = change_path(file)
        get_original_weight, newPath = resize_img(full_path)

        if get_original_weight < weight:
            ImgConverted += 1
            message = "Images Successfully Compressed!"
            show_popup = True

        elif weight <= get_original_weight <= 4000:
            get_original_weight = loop_compress(newPath, get_original_weight, weight, quality)
            if get_original_weight <= weight:
                ImgConverted += 1
                message = "Images Successfully Compressed!"
                show_popup = True

        elif get_original_weight > 4000 and quality == 40:
            get_original_weight = loop_compress(newPath, get_original_weight, 600, quality)
            if get_original_weight <= 600:
                ImgConverted += 1
                message = "Images Successfully Compressed!"
                show_popup = True

        elif get_original_weight > 4000 and quality != 40:
            filename = os.path.basename(full_path)
            imgName = os.path.splitext(filename)[0]
            message = f"Oops! The image {imgName} is too large. To avoid quality issues, please re-upload images larger than 4000 KB, set 'Quality' to 40."
            show_popup = True
    
    return jsonify({'show_popup': show_popup, 'message': message, })

@compress2D.route('uploadStorage', methods=['POST'])
def formStorage():
    formStorage = FormStorage()

    if formStorage.validate_on_submit():
        idproject = formStorage.idproject.data
        iduser = formStorage.idUser.data
        ownership = formStorage.rol.data
        folder = formStorage.folder.data

        file_data = session.get('saved_files', [])
        base_path = os.path.join(os.getcwd(), 'app/static/upload/2d/compressed')

        for relative_path, filename in file_data:
            safe_filename = secure_filename(filename + '.jpg')
            full_path = os.path.join(base_path, safe_filename)

            if not os.path.exists(full_path):
                print(f"⚠️ Archivo no encontrado: {full_path}")
                continue

            with open(full_path, 'rb') as f:
                files = {
                    'files[]': (safe_filename, f, 'application/octet-stream')
                }
                data = {
                    'idproject': idproject,
                    'iduser': iduser,
                    'ownership': ownership,
                    'folder': folder
                }
                response = requests.post('https://onelinkapps.com/api/uploads', files=files, data=data)

                if response.status_code == 200:
                    StorageResponse = True
                    message = "Upload complete!"
                else:
                    StorageResponse = False
                    message = f"Error uploading {safe_filename}: {response.status_code}"
                    break  

    return jsonify({'StorageResponse': StorageResponse, 'message': message})

