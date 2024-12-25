from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
import requests
from config import IMAGE_SAVE_PATH,BASE_URL

def setup_driver():
    driver = webdriver.Chrome()  
    return driver

def scrape_articles(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(20)
    

    try:
        accept_button = driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button")
        driver.execute_script("arguments[0].click();", accept_button)
        print("Accepted cookies using JavaScript")
    except Exception as e:
        print(f"Cookie banner not found: {e}")
   

    driver.implicitly_wait(10)
    articles = driver.find_elements(By.CSS_SELECTOR, ".c.c-d")[:5]
    scraped_data = []
    i = 0
    for article in articles:
        header =article.find_element(By.CSS_SELECTOR, ".c_h")
        h2 = header.find_element(By.CSS_SELECTOR, ".c_t ")
        title = h2.find_element(By.TAG_NAME, "a").text

        content = article.find_element(By.CSS_SELECTOR, ".c_d").text
        img_name="No Image Found!"
        try:
            figure1 = article.find_element(By.CSS_SELECTOR, ".c_m")

            if article.find_element(By.CSS_SELECTOR, ".c_m"):
                figure1= article.find_element(By.CSS_SELECTOR, ".c_m")
                anchor = figure1.find_element(By.CSS_SELECTOR, ".c_m_c")
                image= anchor.find_element(By.CSS_SELECTOR, ".c_m_e")
            # Save image locally
                if image:
                    img_url = image.get_attribute("src")
                    if img_url:
                        img_data = requests.get(img_url).content
                        img_name = os.path.join(IMAGE_SAVE_PATH, f"{i}_{title.replace(' ', '_')}.jpg")

                        with open(img_name, 'wb') as f:
                            f.write(img_data)


        except NoSuchElementException:
            print("No figure element found with the class '.c_m'")

        i=i+1
        scraped_data.append({"title": title, "content": content, "image": img_name})

    return scraped_data