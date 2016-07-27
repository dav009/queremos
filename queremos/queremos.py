import codecs
import yaml

def base_answers():
  answers = {
           "fecha": "octubre 15 2016",

           "solicitante": {
             "nombre": "solicitante nombre",
             "apellido1": "apellido1 ",
             "apellido2": "apellido2",
             "tipo_identificacion": "identificacion",
             "identificacion": "c.c 123",
             "email": "solicitante@gmail.com",
             "telefono": "123",
             "direccion": "calle a # 23 -78, tulua"
           },

           "institucion": {
             "nombre": "nombre institucion",
             "ciudad": "Bogota",
             "direccion": "calle institucion # AB",
             "telefono": "456",
           },

           "funcionario": {
             "nombre": "funcionario nombre",
             "apellido1": "apellido1",
             "apellido2": "apellido2",
             "cargo": "cargo funcionario"
           },    

           "dataset": {
             "descripcion": "dataset de asistencia de congresistas a sesiones del senado",
             "campos": ["nombre congresista", "fecha sesion", "firma asistencia"],
             "fecha_inicial": "octubre 10",
             "fecha_final": "noveimbre 20"
           },

           "privacidad": {
            "privacidad_vulnera_flag": "true/false",
            "privacidad_campos_vulnerables": ["", ""]
           },

           "clasificacion": {
              "datos_flag": "",
              "antiguedad_mayor_a_15_anios_flag": ""
           },

           "restriccion": {
             "datos_industriales_flag": "true/false",
             "seguridad_nacional_flag": "true/false",
             "relaciones_internacionales_flag": "true/false",
             "investigaciones_en_curso_flag": "true/false"
           }

        }
  return answers

def load_extras():
    with open('templates/extras.yaml') as f:
        return yaml.load(f)

SALVAVIDAS = load_extras()['salvavidas']

def generate_base_letter(answers):
    salvavidas_reserva = ""
    salvavidas_reserva_antiguedad = ""

    if answers['clasificacion']['datos_flag']:
        salvavidas_reserva = SALVAVIDAS['reserva']
    if answers['clasificacion']['antiguedad_mayor_a_15_anios_flag']:
        salvavidas_reserva_antiguedad = SALVAVIDAS['reserva_expirada']


    salvavidas = {"salvavidas_reserva": salvavidas_reserva,
                  "salvavidas_reserva_antiguedad": salvavidas_reserva_antiguedad}

    answers_con_salvavidas = dict()
    answers_con_salvavidas.update(answers)
    answers_con_salvavidas.update(salvavidas)
    return answers_con_salvavidas


def create_mock_letter():
  return generate_base_letter(base_answers())


