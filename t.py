import requests
import numpy
from scipy import stats
data = {
    "Data": [785, 700, 295, 625, 692, 420, 240, 588, 859, 286, 245, 923, 865, 869], "Secret": "AV8ROX"}

url = 'https://dev-api.healthrx.co.in/campus-hiring/submit?email=tanishka.kohli00@gmail.com'

r = requests.post(url, json={
    "Size": 14,
    "Mean": 599.42,
    "Median": 658.5,
    "Mode": 240,
    "Min": 240,
    "Max": 923,
    "Secret": "AV8ROX",
})

print(r.text)
