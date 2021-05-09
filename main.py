import pdfkit
import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("template.html")

teacher = input("Ingresa el nombre de docente: ")
activity = input("Ingresa el nombre de la actividad: ")
date = input("Ingresa la fecha de actividad: ")

blanca = {
    'activity' : activity,
    'teacher' : 'Blanca Aide Ramos Ramirez',
    'course' : 'Bases de datos',
    'name' : 'Omar Rodriguez de Luna',
    'career' : 'TIDSM 2A',
    'date' : date
}
nereida = {
    'activity' : activity,
    'teacher' : 'Nereida Monserrat Terrones García',
    'course' : 'Metodologías y modelado de desarrollo de software',
    'name' : 'Omar Rodriguez de Luna',
    'career' : 'TIDSM 2A',
    'date' : date
}
gustavo = {
    'activity' : activity,
    'teacher' : 'Gustavo Adolfo Urrutia López',
    'course' : 'Interconexión de redes',
    'name' : 'Omar Rodriguez de Luna',
    'career' : 'TIDSM 2A',
    'date' : date
}
daritza = {
    'activity' : activity,
    'teacher' : 'Daritza Vianney Macías Ortiz',
    'course' : 'Bases de datos',
    'name' : 'Omar Rodriguez de Luna',
    'career' : 'TIDSM 2A',
    'date' : date
}
rocio = {
    'activity' : activity,
    'teacher' : 'Ma. del Rocio Martínez Hernández',
    'course' : 'Programación orientada a objetos',
    'name' : 'Omar Rodriguez de Luna',
    'career' : 'TIDSM 2A',
    'date' : date
}
angelica = {
    'activity' : activity,
    'teacher' : 'Rosario Angélica Rivera Bolaños',
    'course' : 'Funciones matemáticas',
    'name' : 'Omar Rodriguez de Luna',
    'career' : 'TIDSM 2A',
    'date' : date
}
virginia = {
    'activity' : activity,
    'teacher' : 'Virginia Delgado Ruiz Esparza',
    'course' : 'Formación sociocultural II',
    'name' : 'Omar Rodriguez de Luna',
    'career' : 'TIDSM 2A',
    'date' : date
}

if teacher == 'blanca':
    teacher = blanca
elif teacher == 'nereida':
    teacher = nereida
elif teacher == 'gustavo':
    teacher = gustavo
elif teacher == 'daritza':
    teacher = daritza
elif teacher == 'rocio':
    teacher = rocio
elif teacher == 'angelica':
    teacher = angelica
elif teacher == 'viginia':
    teacher = virginia
else:
    print('Docente no válido')

html = template.render(teacher)
f = open("portada.html", "w")
f.write(html)
f.close()

options = {
    'page-size' : 'A4',
    'margin-top' : '2.5cm',
    'margin-bottom' : '2.5cm',
    'margin-right' : '3cm',
    'margin-left' : '3cm',
    "enable-local-file-access": None
}

pdfkit.from_file('portada.html', 'pdf_portada.pdf', options=options)
os.remove('portada.html')
