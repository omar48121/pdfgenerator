from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("template.html")

usuario = {
    'activity' : 'Mapa mental',
    'teacher' : 'Blanca Aide',
    'course' : 'Bases de datos',
    'name' : 'Omar Rodriguez de Luna',
    'career' : 'TIDSM 2A',
    'date' : '19 - Enero - 2021'
}

html = template.render(usuario)
f = open("portada.html", "w")
f.write(html)
f.close()