from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle 
import time


def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)

options = Options()
options.add_argument("--user-data-dir=chrome-data")

options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

# load cookies
cookie_path = "C:\\Users\\Sen\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"
load_cookie(driver, cookie_path)

# Navigate to url
driver.get("https://www.sharestates.com/pipeline/loan_pipeline")

search_thing = driver.find_element(By.ID, "search-input")

search_thing.send_keys("BC2016-00419")

#driver.quit()

