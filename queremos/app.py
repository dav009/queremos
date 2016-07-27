from queremos import create_mock_letter
from flask import current_app, Flask, request, Response, render_template, Markup
import mimerender
from weasyprint import HTML, CSS

mimerender.register_mime('pdf', ('application/pdf',))
mimerender = mimerender.FlaskMimeRender(global_charset='UTF-8')

app = Flask(__name__)

def render_pdf(html):
    page_settings = [CSS(string='@page { size: A4; margin: 1cm }')]
    pdf = HTML(string=html).write_pdf(stylesheets=page_settings)
    return pdf

@app.route('/generar_solicitar', methods=['GET'])
@mimerender(default='pdf', pdf=render_pdf)
def generar_solicitud():
    html = render_template('solicitud.html', solicitud=create_mock_letter())
    return { 'html': html }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)