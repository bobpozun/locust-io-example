## Simple Locust.io load test example

Setup:  

1 `python3 -m pip install --user --upgrade pip`  
2 `python3 -m pip install --user virtualenv`  
3 `python3 -m venv env`  
4 ```Mac/Linux: source env/bin/activate``` ```Windowns: .\env\Scripts\activate```  
5 `pip install -r -requirements.txt`  

To Use:  
* Execute Run command (below)  
* Go to http://localhost:8089/  
* Load test stuff!  


Test Run Command:  
* locust -f TestFiles/auth.py --host=https://restful-booker.herokuapp.com --logfile=auth.log


Locust Docs: https://docs.locust.io/en/stable/index.html   
Restful booker: https://restful-booker.herokuapp.com/apidoc/index.html