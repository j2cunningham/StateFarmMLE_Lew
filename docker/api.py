from flask import Flask, request, jsonify
from helper_functions import remove_dollar, per_float, \
						     extract_proba_to_dict

import joblib
import json
import pickle

import traceback

import pandas as pd
import numpy  as np

import time

app = Flask(__name__)

# For testing purposes the assumption was that it was a cleaned, nice 
# numerical value.

# Method to predict
@app.route("/predict", methods=['POST'])
def predict():

	'''
	Function to parse, clean, predict and return JSON response 

	Input: A JSON formatted string containing either a single line
           or feature or a batch call with multiple features
           Call can be made cia 'curl'

    Returns:

    JSONified output to terminal and save results to a file in ./output/
    directory

	'''

	if model:
		try:

			# Parse JSON input
			json_ = request.get_json()

			# Make sure it is in a list format
			if type(json_) is not list:
				json_ = [json_]

			# Just a note that all input to the API is a string
			X_features = pd.DataFrame(json_)

			# We need to clean the data before making a prediction
			# First let's fill-in all missing values with 0 as was done in modeling
			# This includes categorical and numerical features
			# This will need to be changed if feature engineering is changed
			X_features.fillna(0,inplace=True)


			# Get uncleaned numerical columns, so far this is x12 and x79
			# Will need to generalize this later
			X_features['x12'] = X_features['x12'].apply(remove_dollar)
			X_features['x79'] = X_features['x79'].apply(per_float)

			# Clean & impute categorical columns
			# This will be a performance hit!!! It needs to be changed
			for map_dict in cat_dict_list:  # Yes, yes, I know two for loops!
				#print(type(item))
				for col,dict_mapper in map_dict.items():
					#print(type(dict_mapper))
					X_features[col].replace(dict_mapper,inplace=True)

			
			# Convert numerical columns that are strings to numerical
			for ncol in num_cols_list:
				X_features[ncol] = X_features[ncol].astype(float)
			

			# Now make the prediction
			try:
				
				y_pred_proba = model.predict_proba(X_features)

			except Exception as e:
				# If it fails, force to an unusual prediction for 
				# later analysis
				y_pred_proba = [[2,0]]


			# Extract results 
			prediction = extract_proba_to_dict(y_pred_proba)
            
            # Dump format in the file based on the requirements
			dump_format = "[" + ",\n ".join([json.dumps(row) for row in prediction ]) + "]"

            # This portion here requires more refinement
            # Current issues: If providing multiple curl calls, this will append
            # but will not put in the next line
            # This needs to be fixed per requirement of spec
			with open('./output/predictions.json','a') as outfile:
				outfile.write(dump_format)
				outfile.write('\n')

            # Returns output to the screen
            # Not sure of two things
            # 1. How to print to the next line
            # 2. How to get rid of the string in the numbers when printing to screen
			return json.dumps(prediction)

		except:

			return jsonify({'trace': traceback.format_exc()})

	else:

		print('No model available. Please load a model.')


#def hello():
#    return "Welcome to machine learning model APIs!"


if __name__ == '__main__':

	# Load trained machine learning model
    model = joblib.load('./models/xgbc_md6.pkl')
    print('**** Machine Learning Model Loaded ****')
    
    # Load categorical columns and dictionary mapping
    with open('./data/cat_dict_list.pkl', 'rb') as fp_cat:
    	cat_dict_list = pickle.load(fp_cat)
    print('**** Loaded categorical dictionary list ****')

    # Load numerical columns
    with open('./data/num_cols_list.pkl', 'rb') as fp_num:
    	num_cols_list = pickle.load(fp_num)
    print('**** Loaded numerical features list ****')

    # Get timing metrics
    start_time = time.time()
    app.run(debug=True,port=5001)
    end_time = time.time()

    print('Time Elapsed: ', end_time - start_time, 'secs')