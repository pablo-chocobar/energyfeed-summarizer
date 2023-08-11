# energyfeed-summarizer

The task in hand was to develop a MLAI based summarization and data aggregation for generating insights from Energy Data feeds, i.e., we had to scrape a site, gather its contents and summarize it using ML/AI. 

Our Approach to the problem:
To scrape a site , we felt that BeautifulSoup is a good option as it is really simple to use and enough for the task in hand. But the BeautifulSoup library cannot scrape dynamic JavaScript websites( websites that load data in the client side by using JavaScript), not by itself. That is why we had to use selenium which is an emulator of sort that poses itself as a regular web browser and requests the link from the server. We then use BeautifulSoup to parse the content from the request and get all the text from the html under the \<p\> tags. we're leaving all the pre processing in the summarizer script.

To summarize the scraped content, we rely on a pre-trained transformers model called HuggingFace. The HuggingFace "t5-small" model will tokenize the scraped text, and summarize it. It does so by putting the text through a transformer pipeline which consists of several tasks. 

1)Sentiment Analysis\
 ->Identifies the emotional tone behind the text\
2)Classification\
 ->Classifies the text under different areas like education, business etc. \
3)Text generation\
 ->Generates the summary

For the user interface we've used html and TailwindCSS. To connect all these togther, we've used the Flask framework in python. Upon entering the link, the html will redirect the user to a page and pass the entered url to the Flask server. The Flask server will then pass the link as a parameter to the scraper script which will return the scraped text. this text then will be passed to the summarizer script which will return the summarized content. This content is then passed to the result page, where Flask will replace the placeholder text, and voila the summary is there for the user to read. 

# Requirements to run our implementation: 
1. Python 3.9
2. the python packages transformers, flask, tensorflow, selenium, beautifulsoup4 ( all of which can be installed by running the command pip install package_name)
3. A web browser of your choice. 
4. a ChromeDriver application which can be downloaded from here: (https://chromedriver.chromium.org/downloads). The path to the chromedriver has to be replaced in the scraper.py file (at line 8 in the chrome_driver variable).


## Note 
The Flask server has to be initialized for the app to run.  The user can initialize it by running the python file server.py. then navigate to 127.0.0.1:5000 on your browser to use the site.
