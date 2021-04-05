from keras.models import load_model
from flask import Flask,render_template,request,redirect

app = Flask("diabetic_app")
m = load_model('heart.h5')

@app.route("/")
def slash():
        return ("Hello")
params = {}

@app.route("/home",methods=['POST', 'GET'])
def Home():
        if request.method == "POST":
                print('post')
                global params
                params['FULL NAME'] = request.form["FULL NAME"]
                params['MOBILE NUMBER'] = request.form["MOBILE NUMBER"]
                params['EMAIL ADDRESS'] = request.form["EMAIL ADDRESS"]
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
                params['Age'] = request.form['Age']
                params['Anaemia'] = request.form['Anaemia']
                params['Creatinine_Phosphokinase'] = request.form['Creatinine_Phosphokinase']
                params['Diabetes'] = request.form['Diabetes']
                params['Ejection_Fraction'] = request.form['Ejection_Fraction']
                params['High_Blood_Pressure'] = request.form['High_Blood_Pressure']
                params['Platelets'] = request.form['Platelets']
                params['Serum_Creatinine'] = request.form['Serum_Creatinine']
                params['serum_sodium'] = request.form['serum_sodium']
                params['Gender'] = request.form['Gender']
                params['Smoking'] = request.form['Smoking']
                params['Time'] = request.form['Time']
                

                output = m.predict([[ int(params['Age']) , int(params['Anaemia']) , int(params['Creatinine_Phosphokinase']) , int(params['Diabetes']) , int(params['Ejection_Fraction']) ,int(params['High_Blood_Pressure']) , int(params['Platelets']),float(params['Serum_Creatinine']),int(params['serum_sodium']),int(params['Gender']) ,int(params['Smoking']),int(params['Time'])]])
                print(output)
                print(int(params['Age']) , int(params['Anaemia']) , int(params['Creatinine_Phosphokinase']) , int(params['Diabetes']) , int(params['Ejection_Fraction']) ,int(params['High_Blood_Pressure']) , int(params['Platelets']),float(params['Serum_Creatinine']),int(params['serum_sodium']),int(params['Gender']),int(params['Smoking']),int(params['Time']))
                print(output[0][0])
                if (str(output[0][0])) <= '0.16':
                        params['output'] =  'Death Possibility is lower'
                else:
                        params['output'] =  'Death Possibility is higher'

                print(params)
                print("data saved success now make a report of it")

                return render_template('report.html',params=params)
        else:
                print('get')
        return render_template("form.html")

@app.route('/output')
def output():
        output = m.predict([[53,0,63,1,60,0,368000,0.8,135,1,0,22]])
        print(str(output[0][0]))
        return (str(output[0][0]))

if__name__ =='__main__':app.run()
        app.run(host="0.0.0.0" , port="81")
