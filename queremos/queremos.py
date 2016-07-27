import codecs
import yaml

def base_answers():
  answers = {
           "fecha": "octubre 15 2016",
           "solicitante_nombre": "solicitante nombre",
           "solicitante_apellido1": "apellido1 ",
           "solicitante_apellido2": "apellido2",
           "solicitante_tipo_identificacion": "identificacion",
           "solicitante_identificacion": "c.c 123",
           "solicitante_email": "solicitante@gmail.com",
           "solicitante_telefono": "123",
           "solicitante_direccion": "calle a # 23 -78, tulua",

           "institucion_nombre": "nombre institucion",
           "institucion_ciudad": "Bogota",
           "institucion_direccion": "calle institucion # AB",
           "institucion_telefono": "456",

           "funcionario_nombre": "funcionario nombre",
           "funcionario_apellido1": "apellido1",
           "funcionario_apellido2": "apellido2",
           "funcionario_cargo": "cargo funcionario",

            "dataset_descripcion": "dataset de asistencia de congresistas a sesiones del senado",
            "dataset_campos": ["nombre congresista", "fecha sesion", "firma asistencia"],
            "dataset_fecha_inicial": "octubre 10",
            "dataset_fecha_final": "noveimbre 20",

            "privacidad_vulnera_flag": "true/false",
            "privacidad_campos_vulnerables": ["", ""],

            "clasificacion_datos_flag": "true/false",
            "clasificacion_antiguedad_mayor_a_15_anios_flag": "true/false",

            "restriccion_datos_industriales_flag": "true/false",
            "restriccion_seguridad_nacional_flag": "true/false",
            "restriccion_relaciones_internacionales_flag": "true/false",
            "restriccion_investigaciones_en_curso_flag": "true/false"
        }
  return answers


TEMPLATE_BASE = "templates/basico"

def load_extras():
    with open('extras.yaml') as f:
        return yaml.load(f)


def load_text(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        lines = [line for line in f]
        return "\n".join(lines)

def format_text(text, fields):
    return text.format(**fields)

def generate_base_letter(answers):
    base_template_text = load_text(TEMPLATE_BASE)

    if answers['clasificacion_datos_flag']:
        salvavidas_reserva = "algo"
    if answers['clasificacion_antiguedad_mayor_a_15_anios_flag']:
        salvavidas_reserva_antiguedad = "algo"


    salvavidas = {"salvavidas_reserva": salvavidas_reserva,
                  "salvavidas_reserva_antiguedad": salvavidas_reserva_antiguedad}

    answers_con_salvavidas = dict()
    answers_con_salvavidas.update(answers)
    answers_con_salvavidas.update(salvavidas)

    formated_text = format_text(base_template_text, answers_con_salvavidas)


    return formated_text

def generate_reposicion(answers):
    pass

def generate_letter(answers):
    pass

def create_mock_letter():
  return generate_base_letter(base_answers())


