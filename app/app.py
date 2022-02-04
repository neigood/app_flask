from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "!neifer! changes in debug"
    cursos = ['PHP', 'python', 'java', 'kottlin', 'Dart', 'java']
    data = {
        'titulo': 'index123',
        'bienvenida': '!saludos!',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)


@app.route('/contacto/<nombre>')
def contacto(nombre):
    data = {
        'titulo': 'contacto',
        'nombre': nombre
    }
    return render_template('contacto.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
