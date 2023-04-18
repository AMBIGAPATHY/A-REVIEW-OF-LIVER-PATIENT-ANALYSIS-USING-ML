from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/predict',  methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    else:
        age1 = request.form['age']
        gender1 = request.form['gender']
        tb1 = request.form['tb']
        db1 = request.form['db']
        ap1 = request.form['ap']
        aa11 = request.form['aa1']
        aa21 = request.form['aa2']
        tp1 = request.form['tp']
        a1 = request.form['a']
        agr1 = request.form['agr']

        data = [[float(age1), float(gender1), float(tb1), float(db1), float(ap1),
             float(aa11), float(aa21), float(tp1), float(a1), float(agr1)]]
        t = age1
        model1 = pickle.load(open('ETC(4).pk1', 'rb'))
        prediction = model1.prediction(data)[0]
        if prediction == 1:
            t = 'You have a liver disease problem, you must consult a doctor'
        else:
            t = 'You dont have a liver disease problem.'
        return render_template('submit.html', output=t)


if __name__ == '__main__':
    app.run()

