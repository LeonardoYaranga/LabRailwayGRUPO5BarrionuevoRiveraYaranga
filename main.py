from flask import Flask, jsonify,render_template,request
import os

app = Flask(__name__)

@app.route('/')
def index():
    ####Only to show a jsonify message
    #my_set = {"Hello World, our names are Dome, Alesso and Leo!"}
    #return jsonify(list(my_set))
    ###Show a template
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/api')
def get_data():
    data = {
        "names": ["Dome", "Alesso", "Leo"]
    }
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit():
    name= request.form['name']

    return jsonify({"name":name})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))