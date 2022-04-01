#cara menghitung berat badan ideal pria
import os
from flask import Flask,jsonify,request

app = Flask(__name__)
@app.route("/quiz", methods=["POST"])
def kuis():
    Tinggi =(float) (request.form['Tinggi'])
    Berat =(float) (request.form['Berat'])

    ideal = (float)(Berat / (Tinggi/100)*(10/100))
    if ideal <= 18.4:
        return(f"berat badan ideal anda : {ideal} "+"Kamu Kurus.")
    elif ideal <= 24.9:
        return(f"berat badan ideal anda : {ideal} "+"Kamu Sehat")
    elif ideal <= 29.9:
        return(f"berat badan ideal anda : {ideal} "+"kamu  kelebihan berat badan.")
    elif ideal <= 34.9:
        return(f"berat badan ideal anda : {ideal} "+"kamu sangat kelebihan berat badan.")
    elif ideal <= 39.9:
        return(f"berat badan ideal anda : {ideal} "+"kamu gemuk.")
    else:
        return(f"berat badan ideal anda : {ideal} "+"kamu sangat gemuk.")
    
        
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True, port=4000)