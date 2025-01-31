from flask import Blueprint, render_template
import os
from flask import current_app
from flask import render_template, request, session
from app.form import ImageUploadForm
from werkzeug.utils import secure_filename
from app.functions.funtions2d import change_path, resize_img, loop_compress
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

    return render_template('compress2d/compress2d.html', imagesForm=form)


@compress2D.route('compressing', methods=['POST'])
def Compress2d():
    saved_files = session.get('saved_files')
    show_popup = False

    for file in saved_files:
        full_path = change_path(file)
        get_original_weight, newPath = resize_img(full_path)
        
        if get_original_weight < 300:
            print(f"Original weight less than 300 KB: {get_original_weight}")
            show_popup = True
        
        elif 300 <= get_original_weight <= 3000:
            target_weight = 300
            reduction = 20
            get_original_weight = loop_compress(newPath, get_original_weight, target_weight, reduction)
            if get_original_weight <= target_weight:
                print(f"Final compressed weight: {get_original_weight} KB")
                show_popup = True
        
        elif get_original_weight > 3000:
            print(f"Image greater than 3000 KB: {get_original_weight}")
            target_weight = 600
            reduction = 40
            get_original_weight = loop_compress(newPath, get_original_weight, target_weight, reduction)
            if get_original_weight <= target_weight:
                print(f"Final compressed weight: {get_original_weight} KB")
                show_popup = True

    return jsonify({'show_popup': show_popup})
