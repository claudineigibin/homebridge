from flask import Flask


app = Flask(__name__)

@app.route("/")



def hello_world():
    cores = ["amarelo", "azul", "roxo", "verde", "vermelho", "anil"]
    pagina = "Lista de cores:<br>"
    for i in cores:
        pagina += i+","
    return pagina, 200


app.run(port=80, host='3.17.78.188', debug=True, threaded=True)







