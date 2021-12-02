from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
import pickle


def init_chrome(path="assets/chromedriver.exe", proxy=True, user_agent=None):
    proxy = {"httpProxy": "163.172.35.121:8088",
             "ftpProxy": "163.172.35.121:8088",
             "sslProxy": "163.172.35.121:8088",
             "noProxy"  : [],
             "proxyType": "MANUAL"}
    if proxy is not None:
        DesiredCapabilities.CHROME["proxy"] = proxy
    opts = Options()
    if user_agent is not None:
        opts.add_argument("user-agent=" + user_agent)
    return Chrome(executable_path=path, options=opts)
#automatisation_starts_here

def login(login,password):
    driver = init_chrome()
    try:
        driver.get("https://vk.com/")
        vk_login_input = driver.find_element_by_css_selector("#index_email")
        vk_login_input.click()
        vk_login_input.send_keys(login)

        vk_password_input = driver.find_element_by_css_selector("#index_pass")
        vk_password_input.click()
        vk_password_input.send_keys(password)
        vk_auth_button = driver.find_element_by_css_selector("#index_login_button")
        vk_auth_button.click()
        cookies = driver.get_cookies()
        file_name = f"{login}+{password}.cookie"
        with open(file_name,'wb') as f:
            pickle.dump(cookies,f)

    finally:
        driver.close()