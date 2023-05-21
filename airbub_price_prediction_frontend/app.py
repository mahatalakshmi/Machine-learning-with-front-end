from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('flask_part2\model1.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index2.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output='{}'.format(prediction[0])

    
    return render_template('index2.html',pred='the value of the house is {}'.format(output),bhai="all the best for purchase")
    


if __name__ == '__main__':
    app.run(debug=True)
