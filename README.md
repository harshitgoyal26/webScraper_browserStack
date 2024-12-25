# webScraper_browserStack
### Web Scraper using Selenium and test using BrowserStack


## Prerequisites

Make sure you have Python3 and `pip` installed on your system.

## Steps

**1. Open Terminal:**

Navigate to the root directory of your project using the terminal.

**2. Create and Activate Virtual Environment:**

*   **Windows:**

    ```
    python -m venv env
    env\Scripts\activate
    ```

*   **macOS/Linux:**

    ```
    python -m venv env
    source env/bin/activate
    ```

**3. Install Dependencies:**

Install the required libraries from your `requirements.txt` file:

    
    pip install -r requirements.txt
    

**4. Configure API Keys:**

Create a file named `.env` in your project directory and add your API keys:


    TRANSLATION_API_KEY= your_translation_api_key
    BROWSERSTACK_USERNAME= your_browserstack_username
    BROWSERSTACK_ACCESS_KEY= your_access_key
    

**5. Run Script Locally:**

To execute the script on your local machine, run:

    
    python main.py
    

**6. Run Tests on BrowserStack:**

Use the BrowserStack SDK to run automated tests on their platform:

    
    browserstack-sdk python main.py





**Notes:**

*   Replace `YOUR_TRANSLATION_API_KEY`, `YOUR_BROWSERSTACK_USERNAME`, and `YOUR_BROWSERSTACK_ACCESS_KEY` with your actual API keys.
*   Ensure the `requirements.txt` file lists the necessary dependencies for your web scrapper.
