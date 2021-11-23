# This file contains all the API calls and tests created to be run in test framework, the information on how to 

import requests
import json

class SensyneApi:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    

    def create_product(self):
        post_url = "http://localhost:5000/v1/product"
        payload = json.dumps({
            "name":self.name,
            "price":self.price
        })
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", post_url, headers=headers, data=payload)
        return response
        

        
    