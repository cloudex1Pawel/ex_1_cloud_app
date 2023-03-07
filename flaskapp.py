from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
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
