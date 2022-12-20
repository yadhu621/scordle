import pathlib
import traceback
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class WhatsApp ():
    """
    Class to interact with Whatsapp

    Provides the below methods:
    scrape() - returns raw data as a list
    """

    def scrape(self):
        """
        Scrape whatsapp and return data as a list

        Returns: A list of string containing Wordle score info and user name
        rtype: List

        Example output:
            [
            "All new messages will disappear from this chat 7 days after they're sent.",
            'You:',
            'Wordle 317 5/6\n\n\n\n\n\n',
            'Wordle 317 5/6\n\n\n\n\n\n',
            ' Read ',
            'Manohar Nanaba:',
            'You:',
            ' Read ',
            'Manohar Nanaba:',
            'Wordle 318 4/6\n\n\n\n\n',
            'Wordle 318 4/6\n\n\n\n\n',
            'You:',
            'Wordle 318 5/6\n\n\n\n\n\n',
            'Wordle 318 5/6\n\n\n\n\n\n',
            ]
        """
        url = "https://web.whatsapp.com/"
        pwd = pathlib.Path().absolute()

        # Keep the browser open after GET
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("window-size=1200x600")
        chrome_options.add_argument(f"user-data-dir={pwd}\\cache")

        driver = webdriver.Chrome(
                    service=Service(ChromeDriverManager().install()),
                    options=chrome_options
                )
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"pane-side")))

            mn_chat_pane_css_selector = "#pane-side > div:nth-child(3) > div > div > div:nth-child(8)"
            mn_chat_pane = driver.find_element(By.CSS_SELECTOR, value = mn_chat_pane_css_selector)
            mn_chat_pane.click()

            time.sleep(2)

            # Get page source
            html_source = driver.page_source
            soup = BeautifulSoup(html_source)

            span_tags = soup.find_all('span')

            # Filter span tags
            raw_data = []
            for span_tag in span_tags:
                if span_tag.has_attr('aria-label'):
                    raw_data.append(span_tag['aria-label'])
                if "Wordle" in span_tag.text:
                    raw_data.append(span_tag.text)


        except Exception:
            traceback.print_exc()

        return raw_data
