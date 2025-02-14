from app import create_app
from flask import render_template, session
from app.blueprints.compress2D import compress2D
from app.blueprints.compressPdf import compressPdf


app = create_app()

app.register_blueprint(compress2D, url_prefix='/')
app.register_blueprint(compressPdf, url_prefix='/pdfCompress')  


@app.route('/360')
def imagen360():
    return render_template('compress2d/compress360.html')


if __name__ == '__main__':
    app.run(debug=True)