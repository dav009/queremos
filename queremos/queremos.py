import codecs
import yaml

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

