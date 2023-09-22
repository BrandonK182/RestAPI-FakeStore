import requests
import json

parameters = {"limit":1}

response = requests.get("https://fakestoreapi.com/products/1", params = parameters)

JSONresponse = response.json()

print("product title" + str(JSONresponse["title"]))
print("price" + str(JSONresponse["price"]))