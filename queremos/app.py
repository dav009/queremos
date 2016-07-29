from queremos import create_mock_letter, generate_base_letter
from flask import current_app, Flask, request, Response, render_template, Markup
import mimerender
from weasyprint import HTML, CSS
import json
import time

mimerender.register_mime('pdf', ('application/pdf',))
mimerender = mimerender.FlaskMimeRender(global_charset='UTF-8')

app = Flask(__name__)

def render_pdf(html):
    page_settings = [CSS(string='@page { size: A4; margin: 1cm }')]
    pdf = HTML(string=html).write_pdf(stylesheets=page_settings)
    return pdf



@app.route('/generar_solicitar', methods=['POST'])
@mimerender(default='pdf', pdf=render_pdf)
def generar_solicitud():
    answers = {}
    if "json" in request.content_type:
        answers = request.json
    elif request.form:
        serialized_form = request.form
        answers = {
           "fecha": time.strftime("%d/%m/%Y"),

           "solicitante": {
             "nombre": serialized_form['solicitante_nombre'],
             "apellido1": serialized_form['solicitante_apellido1'],
             "apellido2": serialized_form['solicitante_apellido2'],
             "tipo_identificacion": serialized_form['solicitante_tipo_id'],
             "identificacion": serialized_form['solicitante_identificacion'],
             "email":serialized_form['solicitante_email'],
             "telefono": serialized_form['solicitante_telefono'],
             "direccion": serialized_form['solicitante_direccion']
           },

           "institucion": {
             "nombre": serialized_form['entidad_nombre'],
             "ciudad": serialized_form['entidad_ciudad'],
             "direccion": serialized_form['entidad_direccion'],
             "telefono": serialized_form['entidad_telefono']
           },

           "funcionario": {
             "nombre": serialized_form['funcionario_nombre'],
             "apellido1": serialized_form['funcionario_apellido1'],
             "apellido2": serialized_form['funcionario_apellido2'],
             "cargo": serialized_form['funcionario_cargo']
           },    

           "dataset": {
             "descripcion": serialized_form['dataset_descripcion'],
             "campos": serialized_form['dataset_campos'],
             "fecha_inicial": "",
             "fecha_final": ""
           },

           "privacidad": {
            "privacidad_vulnera_flag": "",
            "privacidad_campos_vulnerables": ["", ""]
           },

           "clasificacion": {
              "datos_flag":  'clasificacion_datos_flag' in serialized_form,
              "antiguedad_mayor_a_15_anios_flag":  'clasificacion_antiguedad_mayor_a_15_anios_flag' in serialized_form
           },

           "restriccion": {
             "datos_industriales_flag":  'datos_industriales_flag' in serialized_form,
             "seguridad_nacional_flag":  'seguridad_nacional_flag' in serialized_form,
             "relaciones_internacionales_flag": "",
             "investigaciones_en_curso_flag":  'investigaciones_en_curso_flag' in serialized_form
           }

        }


    html = render_template('solicitud.html', solicitud=generate_base_letter(answers))
    return { 'html': html }

@app.route('/', methods=['GET'])
def formulario():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)