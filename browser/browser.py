from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc
uc.install()


def createBrowser():
    chrome_options = Options()
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument("--headless") #uncomment to disable opening of browser window
    #chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36")
    #chrome_options.add_argument("--load-extension=" + os.getcwd() + "/setupvpn")
    #chrome_options.add_argument("--proxy-server=socks5://{}:{}".format(PROXY_HOST, PROXY_PORT))
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('disable-notifications')
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)
    return driver
