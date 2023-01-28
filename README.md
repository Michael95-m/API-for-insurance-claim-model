# API-for-insurance-claim-model

## Intro

I used **fastapi** for the purpose of API. For the prediction case, the [**python package**](https://pypi.org/project/insurance-claim-model) built from that [repository](https://github.com/Michael95-m/packaging-insurance-claim-model). So, I can use the **prediction function** and **schemas of the data** from that package without repeating the code.

## Launching API

```bash
uvicorn  app.main:app --host 0.0.0.0 --port 8001 --reload --reload-dir app ## for development case
gunicorn -c app/gunicorn.py -k uvicorn.workers.UvicornWorker app.main:app ## for production
```

If you want to manage multiple uviconr workers to enable parallelism, **gunicorn** server in conjunction with **Uvicorn** must be used. 

## Requests

There are two main endpoints:

- Endpoint for API Information -> http://0.0.0.0:8001/api/v1/info 
- Endpoint for Prediction service -> http://0.0.0.0:8001/api/v1/predict

You can access the point by the following ways:

- Visit the endpoint on browser at http://localhost:8001/
- cURL

```bash
 curl -X 'GET'   'http://0.0.0.0:8001/api/v1/info'
```
- Access endpoints via code by using **requests** library in Python.

For API information,
```Python
import requests

response = requests.get('http://0.0.0.0:8001/api/v1/info')
```

For Prediction service,
```Python
import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = {
    'inputs': [
        {
            'index': 1023,
            'PatientID': 1024,
            'age': 51,
            'gender': 'female',
            'bmi': 41.3,
            'bloodpressure': 98,
            'diabetic': 'No',
            'children': 0,
            'smoker': 'No',
            'region': 'northeast',
        },
    ],
}

response = requests.post('http://0.0.0.0:8001/api/v1/predict', headers=headers, json=json_data)
```

- Postman can also be used.

## Documentation

The documentation about API can be accessed via http://0.0.0.0:8001/docs.