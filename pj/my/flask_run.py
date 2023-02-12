from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/form")

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method=='GET':
        return render_template('form.html')
    name = request.form['name']
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug = True)