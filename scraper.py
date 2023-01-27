import sys
def scrape(url):
    
    min_length = 400
        
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver

    chrome_driver = r"C:\Users\iampr\Downloads\chromedriver.exe"

    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_driver, options=option)

    driver.get(url) 
    soup = bs(driver.page_source, 'html.parser') 
    [tag.extract() for tag in soup.find_all(
    ["script", "img", "ol", "ul", "time", "h1", "h2", "h3", "iframe", "style", "form", "footer", "figcaption"])]

    noisy_names = ["image", "img", "video", "subheadline", "editor", "fondea", "resumen", "tags", "sidebar", "comment",
                   "entry-title", "breaking_content", "pie", "tract", "caption", "tweet", "expert", "previous", "next",
                   "compartir", "rightbar", "mas", "copyright", "instagram-media", "cookie", "paywall", "mainlist", "sitelist"]

    article_body = ""
    for tag in soup.find_all("div"):

        try:
            tag_id = tag["id"].lower()

            for item in noisy_names:
                if item in tag_id:
                    tag.extract()
        except:
            pass
    
    for article_tag in soup.find_all("article"):

        if len(article_tag.text) >= len(article_body):
            article_body = article_tag.text
    
    if len(article_body) <= min_length:

        for tag in soup.find_all(["div", "section"]):
            try:
                if len(tag.text) >= len(article_body):
                    article_body = tag.text
            except:
                pass

    return article_body

if __name__ == "__main__":
    scrape(sys.argv[1])
