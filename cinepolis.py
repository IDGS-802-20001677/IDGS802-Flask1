from flask import Flask, render_template
from flask import request
app = Flask(__name__)
@app.route("/")
def iniciar():
    return render_template("cinepolis.html")
@app.route("/layout")
def cargar():
    return render_template("cinepolisTemplate.html")
@app.route("/resultado", methods=["POST"])
def resultado():
    cantBol = int(request.form.get("cantBol"))
    cantComp = int(request.form.get("cantComp"))
    persona=str(request.form.get("txtNombre"))
    rbt = request.form.get("rbt")
    res = 0
    desc=0
    if(cantBol < 8):
        if(rbt == 'radioS'):
            if(cantBol > 5):
                desc=0.25
                res = (12*cantBol)-(12*cantBol)*desc
            elif(cantBol > 2):
                desc=0.20
                res = (12*cantBol)-(12*cantBol)*desc
            elif(cantBol <= 2):
                desc=0.10
                res = (12*cantBol)-(12*cantBol)*desc
        else:
            if(cantBol > 5):
                desc=0.15
                res = (12*cantBol)-(12*cantBol)*desc
            elif(cantBol > 2):
                desc=0.10
                res = (12*cantBol)-(12*cantBol)*desc
            elif(cantBol <= 2):
                res = 12*cantBol
        res = res * cantComp

    else:
        res = "No puedes comprar más de 7 boletos" + ' ' + persona

    return render_template("/cinepolis.html", res = res, cantComp = cantComp,  cantBol = cantBol, persona=persona,desc=desc)

if __name__ =="__main__":
    app.run(debug=True, port=3000)