from flask import Flask,current_app,g, request,make_response,jsonify
import requests
from library import library_bp
from flask_cors import CORS



app = Flask(__name__)
app.register_blueprint(library_bp,url_prefix='/library')
CORS(app)

@app.route('/home')
def home():
    resp = make_response("<h1>Hello There Oman</h1>",201,{'token':'FGHHG67GJHFZ'})
    return resp

@app.route('/about')
def about():
    return {"name":"Flask Application", "version":1.0}

# Retrieving Kelvin's grades

@app.route('/grades/<string:student_name>')
def grades(student_name):
    return f"Retrieving {student_name}'s grades"

@app.route('/quotes/<int:quote_id>')
def quotes(quote_id):
   api_resp = requests.get('https://dummyjson.com/quotes')

   quotes = api_resp.json().get('quotes')
   resp = make_response(quotes,200,{"status":"Success"})
   return resp


if __name__ == '__main__':
    app.run(debug=True)

