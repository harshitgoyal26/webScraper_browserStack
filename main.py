from modules.scraper import setup_driver, scrape_articles
from modules.translator import translate_titles
from modules.analyzer import analyze_headers

def main():
    driver = setup_driver()
    try:
        # Scrape Articles
        articles = scrape_articles(driver)
        titles = [article["title"] for article in articles]
        content = [article["content"] for article in articles]

        # Translate Titles
        translated_titles = translate_titles(titles)

        # Analyze Headers
        repeated_words = analyze_headers(translated_titles)

        # Output Results
        print("Titles:", titles)
        print("Content:", content)
        print("Translated Titles:", translated_titles)
        print("Repeated Words:", repeated_words)

    finally:
        driver.quit()




if __name__ == "__main__":
    main()