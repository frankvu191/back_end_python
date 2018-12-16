# Backend Test
1. System Requirement  
Python must be installed  
'pip' must be installed  
allure-report should be installed. Follow this link for instruction https://docs.qameta.io/allure/#_installing_a_commandline  
  
  
2. Install Required Libraries  
From project root folder run command [pip install -r requirements.txt]   


3. Running Test  
a. Running Behave test  
From project root folder run command [behave -f allure_behave.formatter:AllureFormatter -o allure-result]  
b. Running Python script  
From project root folder run command [python city_location_api_test.py]  


4. Viewing Report  
a. Run [allure serve allure-result] to view Allure report  
b. Screen capture for run test in local and in Jenkins(open the link by browser has flash installed) 
https://screencast.com/t/5QgUwjgCOC  
https://screencast.com/t/TnJIyJJuMBhN  
https://screencast.com/t/1chewX4AtnCk