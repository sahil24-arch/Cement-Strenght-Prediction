# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            #
            cement =float(request.form['cement'])
            blast_furnace_slag = float(request.form['blast_furnace_slag'])
            fly_ash = float(request.form['fly_ash'])
            water = float(request.form['water'])
            superplasticizer = float(request.form['superplasticizer'])
            coarse_aggregate = float(request.form['coarse_aggregate'])
            fine_aggregate = float(request.form['fine_aggregate'])
            age = float(request.form['age'])

            filename1 = 'final_model.sav'
            filename2 = 'standart_trans.sav'
            load_model = pickle.load(open(filename1, 'rb')) # loading the model file from the storage
            load_trans = pickle.load(open(filename2, 'rb'))
            # predictions using the loaded model file
            prediction=load_model.predict(load_trans.transform([[cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age]]))
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app