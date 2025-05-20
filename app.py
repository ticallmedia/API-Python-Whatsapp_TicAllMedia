from flask import Flask, json, jsonify, render_template

#_______________________________________________________________________________________
"""
Descripción: Primer Bot de Whatsapp para la empresa TicAll Media, 
con descarga en Google Sheet de Conversaciones


"""
#_______________________________________________________________________________________
app = Flask(__name__)

#_______________________________________________________________________________________
#Ejecucion del Programa
@app.route('/')

#_______________________________________________________________________________________
#Funciones
def index():
    return render_template('index.html')

#_______________________________________________________________________________________

if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
#_______________________________________________________________________________________


