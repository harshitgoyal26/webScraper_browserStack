from modules.scraper import setup_driver, scrape_articles

def main():
    driver = setup_driver()
    try:
        # Scrape Articles
        articles = scrape_articles(driver)
        titles = [article["title"] for article in articles]
        content = [article["content"] for article in articles]

    finally:
        driver.quit()




if __name__ == "__main__":
    main()