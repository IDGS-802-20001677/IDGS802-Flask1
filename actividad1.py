from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operasBas",methods=["GET","POST"])
def operasBas():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        option=request.form.get("opera")

        if(option == "suma"):
            return "<h2> La suma es: {}".format(str(int(num1)+int(num2)))
        elif(option == "resta"):
            return "<h2> La resta es: {}".format(str(int(num1)-int(num2)))
        elif(option == "multiplicacion"):
            return "<h2> La multiplicación es: {}".format(str(int(num1)*int(num2)))
        elif(option == "division"):
            return "<h2> La división es: {}".format(str(int(num1)/int(num2)))
        
        
    else:
        return '''
        <form action = "/operasBas" method = "POST">
        <label> N1: </label>
        <input type = "text" name = "num1" /> </br> </br>
        <label> N2: </label>
        <input type = "text" name = "num2" /> </br> </br>
        
        <input type="radio" id="suma" name="opera" value="suma">
        <label for="suma">Suma</label><br>
        <input type="radio" id="resta" name="opera" value="resta">
        <label for="resta">Resta</label><br>
        <input type="radio" id="division" name="opera" value="division">
        <label for="division">División</label><br>
        <input type="radio" id="multiplicacion" name="opera" value="multiplicacion">
        <label for="multiplicacion">Multiplicación</label><br>
        <input type = "submit" value = "calcular" /> </br> </br>

        

        </form>
        '''


if __name__=="__main__":
    app.run(debug=True, port=3000)