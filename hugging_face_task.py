from flask import Flask
from flask import request
from flask import jsonify
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        text = request.form.get('text')
        generator = pipeline('text-generation',model='distilgpt2')
        return jsonify(generator(text, max_length=20))
    return '''
        <form method="post">
            Text: <input type="text" name="text">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)