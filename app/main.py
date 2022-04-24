from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pathlib


URL = "https://web.whatsapp.com/"
PWD = pathlib.Path().absolute()

# Keep the browser open after GET
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"user-data-dir={PWD}\\cache")

driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
driver.get(URL)