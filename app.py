import sys
from flask import Flask, render_template, request

from src.logger import Logger
from src.exception import CustomException
from src.pipeline.predict_pipeline import PredictPipeline

_logger_obj = Logger('app.py')
logger= _logger_obj.get_logger()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods= ['POST'])
def predict():
    """
    Receives form data, runs prediction,
    renders result page.
    """
    try:
        logger.info('Prediction Request received')
        
        #Step1: ccollect formdata into a dictionary
        input_data= {
            "age": int(request.form.get("age")),
            "gender": request.form.get("gender"),
            "location": request.form.get("location"),
            "contract_type": request.form.get("contract_type"),
            "monthly_charges": float(request.form.get("monthly_charges")),
            "total_charges": float(request.form.get("total_charges")),
            "data_usage_gb": float(request.form.get("data_usage_gb")),
            "call_minutes": int(request.form.get("call_minutes")),
            "num_complaints": int(request.form.get("num_complaints")),
            "issues_resolved": int(request.form.get("issues_resolved")),
            "satisfaction_score": int(request.form.get("satisfaction_score")),
        }
        
        logger.info('Input received ')
        
        # Step 2 : predict using pipeline
        pipeline = PredictPipeline()
        result = pipeline.predict(input_data)
        
        
        #step 3: convert result to readable text 
        churn_result = "Likely to Churn" if result[0] == 1 else "Not Likely to Churn"
        
        logger.info(f'Prediction {churn_result}')
        
        return render_template('result.html',prediction = churn_result)
    except Exception as e:
        raise CustomException(e,sys)

if __name__ =="__main__":
    app.run(debug= True)
        