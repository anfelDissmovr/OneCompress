import os
from flask import render_template, request, session,current_app,Blueprint,render_template,flash
from app.form import ImageUploadForm
from werkzeug.utils import secure_filename
from app.functions.function2d import change_path, resize_img, loop_compress
from flask import jsonify

compress2D = Blueprint('Compress2D', __name__)

@compress2D.route('', methods=['GET', 'POST'])
def index():
    form = ImageUploadForm()

    if form.validate_on_submit():
        images = request.files.getlist('images')
        quality = form.Quality.data
        session['quality'] = quality
        
        weight = form.Weight.data
        session['weight'] = weight
        
        width = form.Width.data
        session['width'] = width
        
        height = form.Height.data
        session['height'] = height
        
        if images:
            saved_files = []
            
            for image in images:
                filename = secure_filename(image.filename)
                filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                image.save(filepath)
                
                relative_path = os.path.relpath(filepath, os.path.join(os.getcwd(), 'app/static'))
                filename_without_extension = os.path.splitext(filename)[0]
                
                saved_files.append((relative_path, filename_without_extension))
            
            session['saved_files'] = saved_files
            print(f"Files saved in session: {saved_files}")  
            img_show = session.get('saved_files')  
            return render_template('compress2d/compress2d.html', imagesForm=form, saved_files=img_show)

    return render_template('compress2d/compress2d.html', imagesForm=form, titulo="Compress 2D Img")


@compress2D.route('compressing', methods=['POST'])
def Compress2d():
    saved_files = session.get('saved_files')
    quality = session.get('quality')
    weight = session.get('weight')
    width = session.get('width')
    show_popup = False
    message = ""

    for file in saved_files:
        full_path = change_path(file)
        get_original_weight, newPath = resize_img(full_path)

        if get_original_weight < weight:
            message = "Images Successfully Compressed!"
            show_popup = True

        elif weight <= get_original_weight <= 4000:
            target_weight = weight
            reduction = quality
            get_original_weight = loop_compress(newPath, get_original_weight, target_weight, reduction)
            if get_original_weight <= target_weight:
                message = "Images Successfully Compressed!"
                show_popup = True

        elif get_original_weight > 4000 and quality == 40: 
            target_weight = 600
            reduction = quality
            get_original_weight = loop_compress(newPath, get_original_weight, target_weight, reduction)
            if get_original_weight <= target_weight:
                message = "Images Successfully Compressed!"
                show_popup = True

        elif get_original_weight > 4000 and quality != 40:
            filename = os.path.basename(full_path)
            imgName = os.path.splitext(filename)[0]
            message = f"Oops! The image {imgName} is too large. To avoid quality issues, please re-upload images larger than 4000 KB, set 'Quality' to 40."
            show_popup = True

    return jsonify({'show_popup': show_popup, 'message': message})


