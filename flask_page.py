from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def mainpage():
    # var1 = [1,2,3,4,5]
    # pups = ['jinja','rufus']
    return render_template('home.html')

@app.route('/puppy/<name>')
def pupp(name):
    return render_template('puppy.html',name=name)
if __name__ == '__main__':
    app.run(debug=True)