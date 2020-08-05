# README

This is a temporary repository for a fictitious problem facing a Machine Learning Engineer. The MLE is to create a model and deploy it into production. Below are the keypoints:

- Read the `instructions.txt` file first as that file contains the questions pertaining to this work

- There is a file called `SummaryReport.pdf` that gives a brief report


## Instructions

Briefly, the model is wrapped in Flask. Original data is not included. Below are the bare minimum steps to run this via Flask

1. Execute `python api.py` in a terminal
2. In another terminal you can run `sh run_pred_200_times.sh`. This calls the API 200 times and feeds the API with data and makes a prediction.

The model Flask API was then wrapped in Docker. You can find this is Docker directory. First make sure you have Docker running in the background. In a terminal, simply run the `run_api.sh` file.

**CAUTION!!!!** If you currently have Docker images that your Docker server and want to keep them, simply remove the `docker system prune -a` line from the `run_api.sh` file. 

I am unable to get a prediction from the Docker image when using 

`curl --request POST --url http://localhost:5001/predict --header 'content-type: application/json' --data <input_data>`

I get the response

`curl: (52) Empty reply from server`

Hence, I have not figured out yet what I missing here.


## Next Steps

1. Fix Docker problem
2. Add section on Unit Testing. Before deploying anything, one has to unit test your application
3. Large scale deployment via Kubernetes
4. Test it with a large load of data, i.e. thousands of calls a minute.