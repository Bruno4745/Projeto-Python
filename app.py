from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src")

@app.route("/", methods=["GET", "POST"])
def home():

    if(request.method == "GET"):
        return render_template("index.html")

    else:
        if (request.form["num1"] !="" and request.form["num2"] !=""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            
            if (request.form["opc"] == "somar"):
                soma = float(num1) + float(num2)
                return {
                    f"Resultado de {num1}+{num2}": f"{soma:.2f}"
                }

            elif (request.form["opc"] == "subtrair"):
                subtracao = float(num1) - float(num2)
                return {
                    f"Resultado de {num1}-{num2}": f"{subtracao:.2f}"
                }
            
            elif (request.form["opc"] == "multiplicar"):
                multiplicacao = float(num1) * float(num2)
                return {
                    f"Resultado de {num1}*{num2}": f"{multiplicacao:.2f}"
                }

            else:
                divisao = float(num1) / float(num2)
                return {
                    f"Resultado de {num1}/{num2}": f"{divisao:.2f}"
                }
        else:
            return render_template("mensagem.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=3700, debug=True)