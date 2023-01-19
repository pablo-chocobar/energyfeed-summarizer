import sys
def scrape(arg1):
        
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver

    url = arg1
    chrome_driver = r"C:\Users\iampr\Downloads\chromedriver.exe"

    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_driver, options=option)

    driver.get(url) 
    soup = bs(driver.page_source, 'html.parser') 

    p = [z.get_text() for z in soup.find_all("p")]

    return p

if __name__ == "__main__":
    scrape(sys.argv[1])