import json
import time

from flask import current_app, Flask, request, Response, render_template, Markup
from weasyprint import HTML, CSS
import mimerender

from queremos import generate_base_letter


mimerender.register_mime('pdf', ('application/pdf',))
mimerender = mimerender.FlaskMimeRender(global_charset='UTF-8')

app = Flask(__name__)

def render_pdf(html):
    page_settings = [CSS(string='@page { size: A4; margin: 1cm }')]
    pdf = HTML(string=html).write_pdf(stylesheets=page_settings)
    return pdf

def form_to_json_request(form_answers):
    answers = {
           "fecha": time.strftime("%d/%m/%Y"),

           "solicitante": {
             "nombre": form_answers['solicitante_nombre'],
             "apellido1": form_answers['solicitante_apellido1'],
             "apellido2": form_answers['solicitante_apellido2'],
             "tipo_identificacion": form_answers['solicitante_tipo_id'],
             "identificacion": form_answers['solicitante_identificacion'],
             "email":form_answers['solicitante_email'],
             "telefono": form_answers['solicitante_telefono'],
             "direccion": form_answers['solicitante_direccion']
           },

           "institucion": {
             "nombre": form_answers['entidad_nombre'],
             "ciudad": form_answers['entidad_ciudad'],
             "direccion": form_answers['entidad_direccion'],
             "telefono": form_answers['entidad_telefono']
           },

           "funcionario": {
             "nombre": form_answers['funcionario_nombre'],
             "apellido1": form_answers['funcionario_apellido1'],
             "apellido2": form_answers['funcionario_apellido2'],
             "cargo": form_answers['funcionario_cargo']
           },    

           "dataset": {
             "descripcion": form_answers['dataset_descripcion'],
             "campos": [c.strip() for c in form_answers['dataset_campos'].split(",")],
             "fecha_inicial": "",
             "fecha_final": ""
           },

           "privacidad": {
            "privacidad_vulnera_flag": "",
            "privacidad_campos_vulnerables": ["", ""]
           },

           "clasificacion": {
              "datos_flag":  'clasificacion_datos_flag' in form_answers,
              "antiguedad_mayor_a_15_anios_flag":  'clasificacion_antiguedad_mayor_a_15_anios_flag' in form_answers
           },

           "restriccion": {
             "datos_industriales_flag":  'datos_industriales_flag' in form_answers,
             "seguridad_nacional_flag":  'seguridad_nacional_flag' in form_answers,
             "relaciones_internacionales_flag": "",
             "investigaciones_en_curso_flag":  'investigaciones_en_curso_flag' in form_answers
           }

        }
    return answers



@app.route('/generar_solicitar', methods=['POST'])
@mimerender(default='pdf', pdf=render_pdf)
def generar_solicitud():
    answers = {}
    if "json" in request.content_type:
        answers = request.json
    elif request.form:
        answers = form_to_json_request(request.form)

    html = render_template('solicitud.html', solicitud=generate_base_letter(answers))
    return { 'html': html }

@app.route('/', methods=['GET'])
def formulario():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
