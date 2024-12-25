# webScrapper_browserStack
Web Scrapper using Selenium and test using BrowserStack


Step1: Open a terminal at root level of project directory

Step2: Create and activate a virtual environment:
        python3 -m venv env
        env\Scripts\activate  # On Windows
        # OR
        source env/bin/activate  # On macOS/Linux

Step3: Install dependencies:
        pip install -r requirements.txt

Step4: Configure API keys in .env file:
        TRANSLATION_API_KEY = 
        BROWSERSTACK_USERNAME = 
        BROWSERSTACK_ACCESS_KEY = 

Step5: to run the script locally:
        python main.py

Step6: To run automated tests on BrowserStack:
        browserstack-sdk python main.py
