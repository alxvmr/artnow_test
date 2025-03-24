Testing of the site [artnow.ru](https://artnow.ru/)

# Setting up the environment
First you need to activate the python environment:
```
.\artnow_venv\Scripts\activate
```
and establish the necessary dependencies:
```
pip install -r requirements.txt
```

# Running tests
Tests can be run in multiple threads, specifying the browser (firefox/chrome) and the directory to save the allure report in:
```
pytest -n4 ./tests --browser=firefox --alluredir=allure_report
```

# Allure report
To display the allure report in a web browser you need to execute the command:
```
allure serve allure_report
```

:link: [Allure for Windows](https://allurereport.org/docs/install-for-windows/)