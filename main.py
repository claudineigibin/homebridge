from flask import Flask

app = Flask(__name__)

@app.route("/")



def hello_world():
    cores = ["amarelo", "azul", "roxo", "verde", "vermelho", "anil"]
    pagina = "Lista de cores:<br>"
    for i in cores:
        pagina += i+","
    return pagina, 200


app.run()







