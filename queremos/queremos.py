import codecs

def base_answers():
  answers = {
           "fecha": "",
           "solicitante_nombre": "",
           "solicitante_apellido1": "",
           "solicitante_apellido2": "",
           "solicitante_tipo_identificacion": "",
           "solicitante_identificacion": "",
           "solicitante_email": "",
           "solicitante_telefono": "",
           "solicitante_direccion": "",

           "institucion_nombre": "",
           "institucion_ciudad": "",
           "institucion_direccion": "",
           "institucion_telefono": "",

           "funcionario_nombre": "",
           "funcionario_apellido1": "",
           "funcionario_apellido2": "",
           "funcionario_cargo": "",

            "dataset_descripcion": "",
            "dataset_campos": ["", ""],
            "dataset_fecha_inicial": "",
            "dataset_fecha_final": "",
            "dataset_formato": "",

            "privacidad_vulnera_flag": "true/false",
            "privacidad_campos_vulnerables": ["", ""],

            "clasificacion_datos_flag": "true/false",
            "clasificacion_antiguedad_mayor_a_30_anios_flag": "true/false",

            "restriccion_datos_industriales_flag": "true/false",
            "restriccion_seguridad_nacional_flag": "true/false",
            "restriccion_relaciones_internacionales_flag": "true/false",
            "restriccion_investigaciones_en_curso_flag": "true/false"
        }
  return answers


TEMPLATE_BASE = "templates/basico"
SALVAVIDAS_FORMATO = "templates/salvavidas_formato"
TEMPLATE_RECTIFICACION = ""


def load_text(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        lines = [line for line in f]
        return "\n".join(lines)

def format_text(text, fields):
    return text.format(**fields)

def salvavidas_formato(formato_deseado):
    return load_text(SALVAVIDAS_FORMATO).format(dataset_formato=formato_deseado)

def generate_base_letter(answers):
    base_template_text = load_text(TEMPLATE_BASE)

    salvavidas = {"salvavidas_reserva":"",
                  "salvavidas_reserva_antiguedad":"",
                  "salvavidas_procesable":"",
                  "salvavidas_formato_deseable":"",
                  "salvavidas_no_discriminacion":""}

    answers_con_salvavidas = dict()
    answers_con_salvavidas.update(answers)
    answers_con_salvavidas.update(salvavidas)

    formated_text = format_text(base_template_text, answers_con_salvavidas)


    return formated_text

def generate_reposicion(answers):
    pass

def generate_letter(answers):
    pass

print(generate_base_letter(base_answers()))

