# This file contains all the API calls and tests created to be run in test framework, the 'create_product' function will be run in the file 'createProduct.py' initially and as the framework is built other functions will be run in files relating to their function.

import requests
import json

class SensyneApi:
    def __init__(self, name, price, special_char):
        self.name = name
        self.price = price
        self.special_char = special_char
    

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
        

        
    