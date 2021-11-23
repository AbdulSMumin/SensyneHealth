# SensyneHealth

- There are 2 files being used for this test framework. file1 = apiCalls.py , file2 = createProduct.py
- There is a document called testSheet.xlsx where the test cases and bugs are being logged manually as a report and where the test cases in the framework come from.

- For this task I have only created "PUSH" requests for creating products as it will show my thinking of how I would build the start of a framework. As I should only take 1-2 hours for the task, if I were to build on top of that I would create more functions in the apiCalls.py in the SensyneApi() class, for now I have created the function 'create_product' and if I were building on the framework I would add the following functions into the SensyneApi() class on apiCalls.py:            
    ->'delete_product' - "DELETE" request
    ->'get_product' (This would be for a single product) - "GET" request
    ->'update_product' - "PUT" request
    ->'get_products_list' (This would be for all products as list) - "GET" request

I would then create different files for each function and then include them in unittest test cases based on test scenarios/cases I will have input into the excel sheet testSheet.xlsx . For example for 'get_product' and 'get_products_list' I would create the 2 functions within the class SensyneApi() on apiCalls.py for the 2 get requests, then create a file called 'productInformation.py' this would contain the class GetProduct(Unittest.TestCase) and create test cases in the form of functions within that for both getting a single product and getting a list of products


Instructions on how to run tests on createProduct.py

-> Open a terminal in the correct directory of SensyneHealth
-> Run following command:
    python createProduct.py


The following should map to the results found on the file testSheet.xlsx