from queremos import create_mock_letter
from flask import current_app, Flask, request, Response, render_template, Markup
import mimerender
from weasyprint import HTML

mimerender.register_mime('pdf', ('application/pdf',))
mimerender = mimerender.FlaskMimeRender(global_charset='UTF-8')

app = Flask(__name__)

def render_pdf(html):
    pdf = HTML(string=html).write_pdf()
    return pdf

@app.route('/generar_solicitar', methods=['GET'])
@mimerender(default='pdf', pdf=render_pdf)
def generar():
    html = render_template('solicitud.html', content=Markup(create_mock_letter()))
    return { 'html': html } # mimerender requires a dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)