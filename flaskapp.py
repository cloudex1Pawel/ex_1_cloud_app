"""
Flask application for greeting users
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
     """
    Displays a form to enter name and greets user with entered name after submitting the form.
    
    Returns:
        str: Greeting message with user's name.
    """
    if request.method == "POST":
        name = request.form['name']
        return f"Hello, {name}!"
    return '''
        <form method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
