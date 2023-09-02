from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open("C:/Users/Admin/Ml_project/model/xgb_model.pickle", "rb"))
app=Flask(__name__)

@app.route('/')
# def hello():
#     return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_vehicle_insurance():
    gender=int(request.form.get('gender'))
    age=int(request.form.get('age'))
    driving_license=int(request.form.get('driving_license'))
    region_code=int(request.form.get('region_code'))
    previously_insured=int(request.form.get('previously_insured'))
    vehicle_age=int(request.form.get('vehicle_age'))
    vehicle_damage=int(request.form.get('vehicle_damage'))
    annual_premium=request.form.get('annual_premium')
    policy_sales_channel=int(request.form.get('policy_sales_channel'))
    vintage=int(request.form.get('vintage'))

    #prediction
    result=model.predict(np.array([[gender,age,driving_license,region_code,previously_insured,vehicle_age,vehicle_damage,annual_premium,policy_sales_channel,vintage]]))

    if result[0]==1:
        result='Customer is Interested for Vehicle Insurance'
    else:
        result='Customer is not Interested for Vehicle Insurance'


    return render_template('index.html',result=result)


if __name__=='__main__':
    app.run(debug=True)