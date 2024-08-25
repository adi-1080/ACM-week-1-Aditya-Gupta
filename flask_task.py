from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/user/<name>') # A route with a dynamic URL parameter
def user(name):
    return f"Hello, {name}!"

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Form submitted! Hello, {name}!"
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit">
        </form>
    '''
    
# write a simple 'index.html' file in a 'templates' folder
@app.route('/template')
def template():
    return render_template('index.html')

@app.route('/data')
def data():
    response_data = {'name': 'Alice', 'age': 24, 'city': 'New York'}
    return jsonify(response_data)

@app.route('/api/user/<int:id>', methods=['GET'])
def get_user(id):
    users = {1: 'Alice', 2: 'Bob', 3: 'Charlie'}
    user = users.get(id, 'User not found')
    return jsonify({'id': id, 'name': user})

if __name__ == "__main__":
    app.run(debug=True)