from app import create_app
from flask import render_template, session
from app.blueprints.compress2D import compress2D
# from app.blueprints.Compresspdf import Compresspdf
# from app.blueprints.CompressSlider import CompressSlider


app = create_app()

app.register_blueprint(compress2D, url_prefix='/')
# app.register_blueprint(Compresspdf, url_prefix='/pdfCompress')
# app.register_blueprint(CompressSlider, url_prefix='/sliderCompress')


@app.route('/360')
def imagen360():
    return render_template('compress2d/compress360.html')

# @app.route('/showImgenes')
# def showImgenes():
#     saved_files = session.get('saved_files')
#     for file in saved_files:
#         full_path = change_path(file)
#         show_img(full_path) 
    
#     session['saved_files'] = []
#     show_popup = False
#     return  jsonify({'show_popup': show_popup})

if __name__ == '__main__':
    app.run(debug=True)