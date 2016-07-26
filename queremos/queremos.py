

'''
answer is a json dict following this shape

{
   "fecha": "",
    
   "solicitante": {
      "nombre": "",
      "apellido1": "",
      "apellido2": "",
      "email": "",
      "telefono": "",
      "direccion": ""
   },

   "institucion": {
     "nombre": "",
     "ciudad": "",
     "direccion": "",
     "telefono": ""
   },

   "funcionario": {
     "nombre": "",
     "apellido1": "",
     "apellido2": "",
     "cargo": ""
   },

   "dataset": {
      "descripcion": "",
      "campos": ["", ""..],
      fecha_inicial: "",
      fecha_final: ""
   },

   "privacidad": {
      "vulnera": "true/false",
      "campos_vulnerables": ["", ""]
   },

   "clasificacion": {
     "datos_clasificados": "true/false",
     "antiguedad_mayor_a_30_anios": "true/false"
   },

   "otras_restricciones": {
      "datos_industriales": "true/false",
      "seguridad_nacional": "true/false",
      "relaciones_internacionales": "true/false",
      "investigaciones_en_curso": "true/false"
   }

      
}
'''

import codecs

TEMPLATE_BASE = "templates/basico"
TEMPLATE_RECTIFICACION = ""

def load_text(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        lines = [line for line in f]
        return "\n".join(lines)

def get_template_text():
    pass

def generate_base_letter(answers):
    pass

def generate_reposicion(answers):
    pass

def generate_letter(answers):
    pass

print(load_text(TEMPLATE_BASE).format(tipoIdentificacion="cc", identificacion="11",apellido= "lala",nombre="DAVID", ciudad="something", direccion="",fecha="", cargo="", entidad="",informacion="",
salvavidasReserva="",
salvavidasReservaAntigua="",
salvavidasProcesable="",
salvavidasFormateDeseable="",
salvavidasNoDiscriminacion=""
))
