## Function to scrape post titles from subreddit

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scrape_subreddit_title(subreddit):
    driver = webdriver.Edge('/Program Files/edgedriver_win64/msedgedriver')
    driver.get(subreddit)
    time.sleep(1)

    posts = driver.find_elements_by_class_name('_eYtD2XCVieq6emjKBH3m')
    comments = driver.find_elements_by_class_name('FHCV02u6Cp2zYL0fhQPsO')
    upvotes = driver.find_elements_by_class_name('_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo')
    
    titles = []
    for post in posts:
        titles.append(post.text)
    return titles

crypto_posts = scrape_subreddit_title(r_cryptocurrency)
pd.DataFrame(crypto_posts)