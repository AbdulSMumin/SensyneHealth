# This is where the test cases from testSheet.xlsx can be run and recreated 
from apiCalls import *
import unittest

from requests import Response
# Test Cases 1-5 for creating product
class CreatingProducts(unittest.TestCase):
    def test_case_1(self):
        """This test is to verify creation of a product when all conditions are in correct format."""
        print("Creating product with name 'John' and price of '15' ")
        name1 = "John"
        price1 = 15
        test_case_1 = SensyneApi(name1, price1)
        response_code_1 = test_case_1.create_product()
        print(response_code_1)
        assert response_code_1.status_code ==200, "Incorrect Response. Expected response:200, Actual response: " + str(response_code_1.status_code)
        print("Correct Response. Expected response:200, Actual response: " + str(response_code_1.status_code))

    def test_case_2(self):
        """This test verifies that you cannot create a product with incorrect name format"""
        print("Creating product with name '1000' and price of '20'")
        name2 = 1000
        price2 = 20
        test_case_2 = SensyneApi(name2, price2)
        response_code_2 = test_case_2.create_product()
        print(response_code_2)
        assert response_code_2.status_code ==400, "Incorrect Response. Expected response:400, Actual response: " + str(response_code_2.status_code)
        print("Correct response. Expected response:400, Actual response: " + str(response_code_2.status_code))

    def test_case_3(self):
        """This test verifies that you cannot create a product with incorrect price format"""






if __name__ == "__main__":
    unittest.main()


# name = input("Enter Name: ")
# price = input("Enter Price: ")
# si = SensyneApi(name, int(price))
# si.create_product()
# import requests
# import json

# url = "http://localhost:5000/v1/product/17"

# payload = json.dumps({
#    "product_code": 17
# })
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

