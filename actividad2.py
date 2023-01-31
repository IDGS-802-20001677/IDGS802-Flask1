from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/operasBas", methods=["GET"])
def operasBas():
    return render_template("operasbas.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    n1=request.form.get("txtNum1")
    n2=request.form.get("txtNum2")
    res=int(n1)*int(n2)

    x=0
    suma=0
    impresion=""

    while x < int(n2):
        suma=suma + int(n1)
        if impresion=="":
            impresion=impresion+n1
        else:
            impresion=impresion +"+"+n1
        x +=1

    return render_template("resultado.html", res=res,suma=suma,impresion=impresion)

if __name__=="__main__":
    app.run(debug=True, port=3000)