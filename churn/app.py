from keras.models import load_model
from flask import Flask,render_template,request,redirect

app = Flask("diabetic_app")
m = load_model('churn.h5')

@app.route("/")
def slash():
        return ("Hello")
params = {}

@app.route("/home",methods=['POST', 'GET'])
def Home():
        if request.method == "POST":
                print('post')
                global params
                params['FULL_NAME'] = request.form["FULL_NAME"]
                params['MOBILE_NUMBER'] = request.form["MOBILE_NUMBER"]
                params['EMAIL_ADDRESS'] = request.form["EMAIL_ADDRESS"]
                print(params)
                return redirect('/form')
        else:
                print('get')
        return render_template("home.html")

@app.route("/form",methods=['POST', 'GET'])
def Form():
        if request.method == "POST":
                global params
                print('post',params)
                params['Credit_score'] = request.form['Credit_score']
                params['Age'] = request.form['Age']
                params['tenure'] = request.form['tenure']
                params['Balance'] = request.form['Balance']
                params['NumofProducts'] = request.form['NumofProducts']
                params['Estimated_salary'] = request.form['Estimated_salary']
                params['Is_Active_member'] = request.form['Is_Active_member']
                params['Gender'] = request.form['Gender']
                params['Country'] = request.form['Country']
                params['Has_Credit_Card'] = request.form['Has_Credit_Card']
                if params['Gender']  ==  'male':
                        x8 = '1'
                else:
                        x8 = '0'
                if params['Country'] ==  'Germany':
                        x9 = '1'
                        x10 = '0'
                elif params['Country'] == 'Spain':
                        x9 = '0'
                        x10 = '1'
                else:
                        x9 = '0'
                        x10 = '0'

                output = m.predict([[ int(params['Credit_score']) , int(params['Age']) , int(params['tenure']) , float(params['Balance']) , int(params['NumofProducts']) , float(params['Estimated_salary']) ,int(params['Is_Active_member']) , int(x8),int(x9),int(x10),int(params['Has_Credit_Card']) ]])
                print(output)
                print(int(params['Credit_score']) , int(params['Age']) , int(params['tenure']) , float(params['Balance']) , int(params['NumofProducts']) , float(params['Estimated_salary']) ,int(params['Is_Active_member']) , int(x8),int(x9),int(x10),int(params['Has_Credit_Card']))
                print(str(round(output[0][0])))
                if (str(round(output[0][0]))) == '1':
                        params['output'] =  'Job excited'
                else:
                        params['output'] =  'Job not excited'

                print(params)
                print("data saved success now make a report of it")

                return render_template('report.html',params=params)
        else:
                print('get')
        return render_template("form.html")

@app.route('/output')
def output():
        output = m.predict([[653,58,1,132602.88,1,5097.67,0,1,1,0,1]])
        print(str(round(output[0][0])))
        return (str(round(output[0][0])))

app.run(host="0.0.0.0" , port="81")