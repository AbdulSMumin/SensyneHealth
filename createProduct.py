# This is where the test cases from testSheet.xlsx can be run and recreated 
from apiCalls import *
import unittest

# Test Cases 1-4 for creating product

class CreatingProducts(unittest.TestCase):
    def test_case_1(self):
        """This test is to verify creation of a product when all conditions are in correct format."""
        print("Test Case 1 - Creating product with name 'John' and price of '15'")
        name1 = "John"
        price1 = 15
        special_char1 = None
        test_case_1 = SensyneApi(name1, price1, special_char1)
        response_code_1 = test_case_1.create_product()
        print(response_code_1)
        assert response_code_1.status_code ==200, "Incorrect Response. Expected response:200, Actual response: " + str(response_code_1.status_code)
        print("Correct Response. Expected response:200, Actual response: " + str(response_code_1.status_code))

    def test_case_2(self):
        """This test verifies that you cannot create a product with incorrect name format"""
        print("Test Case 2 - Creating product with name '1000' and price of '20'")
        name2 = 1000
        price2 = 20
        special_char2 = None
        test_case_2 = SensyneApi(name2, price2, special_char2)
        response_code_2 = test_case_2.create_product()
        print(response_code_2)
        assert response_code_2.status_code ==400, "Incorrect Response. Expected response:400, Actual response: " + str(response_code_2.status_code)
        print("Correct response. Expected response:400, Actual response: " + str(response_code_2.status_code))

    def test_case_3(self):
        """This test verifies that you cannot create a product with incorrect price format"""
        print("Test Case 3 - Creating a product with name 'Harry' and price of '@!!' ")
        name3 = "Harry"
        price3 = None
        special_char3 = "@!!"
        test_case_3 = SensyneApi(name3, price3, special_char3)
        response_code_3 = test_case_3.create_product()
        print(response_code_3)
        assert response_code_3.status_code ==400, "Incorrect Response. Expected response:400, Actual response: " + str(response_code_3.status_code)
        print("Correct response. Expected response:400, Actual response: " + str(response_code_3.status_code))

    def test_case_4(self):
        """This test verifies that you cannot create a product with incorrect name and price format"""
        print("Test Case 4 - Creating a product with name '0.56' and price '@!!'")
        name4 = 0.56
        price4 = None
        special_char4 = "@!!"
        test_case_4 = SensyneApi(name4, price4, special_char4)
        response_code_4 = test_case_4.create_product()
        print(response_code_4)
        assert response_code_4.status_code ==400, "Incorrect Response. Expected response:400, Actual response: " + str(response_code_3.status_code)
        print("Correct response. Expected response:400, Actual response: " + str(response_code_4.status_code))



if __name__ == "__main__":
    unittest.main()


