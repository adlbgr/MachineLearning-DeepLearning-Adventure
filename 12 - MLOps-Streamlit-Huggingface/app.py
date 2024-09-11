from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('guess_salary.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    experience = int(request.form.get('experience'))
    test_score = int(request.form.get('test_score'))
    interview_score = int(request.form.get('interview_score'))
    prediction = model.predict([[experience, test_score, interview_score]])
    return render_template('index.html', prediction='Employee Salary should be $ {}'.format(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
