from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4')
def eight_by_four():
    return render_template('eight_by_four.html')

@app.route('/<int:num1>/<int:num2>')
def x_by_y(num1, num2):
    yaxis=num1
    xaxis=num2
    return render_template('x_by_y.html', yaxis=yaxis, xaxis=xaxis)

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def numnumcolorcolor(num1, num2, color1,color2):
    yaxis=num1
    xaxis=num2
    return render_template('numnumcolorcolor.html', yaxis=yaxis, xaxis=xaxis, color1=color1, color2=color2)


if __name__=="__main__":   
    app.run(debug=True) 

