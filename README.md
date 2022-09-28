# igel-no-code-ml

A quick showcase of the no code ML tool [igel](https://github.com/nidhaloff/igel) on the [kaggle churn prediction dataset](https://www.kaggle.com/code/ahmetcankaraolan/churn-prediction-using-machine-learning/data).


To run this repository from scratch download the data from [kaggle](https://www.kaggle.com/code/ahmetcankaraolan/churn-prediction-using-machine-learning/data) and save it as `raw.csv`. The files `train.csv` and `test.csv` have been created by running that `preprocess.py` script. The easiest way to run igel is by using it's docker image `nidhaloff/igel`.

```
docker pull nidhaloff/igel
```

## Initialisation and training

The following section provides the commands to run igel from scratch. These commands will initialise the [igel.yaml](igel.yaml) and run the training.
```
docker run -it --rm -v $(pwd):/data nidhaloff/igel init
docker run -it --rm -v $(pwd):/data nidhaloff/igel fit -yml 'igel.yaml' -dp 'data/train.csv'
```
## Serving

For serving run the following script
```
docker run -it --rm -v $(pwd):/data nidhaloff/igel igel serve --model_results_dir "model_results/" --host "0.0.0.0" -port 8888
 ```

Testing works with:
```
curl -X POST localhost:8080/predict --header "Content-Type:application/json" -d '{"CreditScore" :596, "Age" :32, "Tenure" :3, "Balance" :96709.07, "NumOfProducts" :2, "HasCrCard" :0, "IsActiveMember" :0, "EstimatedSalary" :41788.37}'
``
