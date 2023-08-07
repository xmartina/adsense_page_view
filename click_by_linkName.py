from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()

CHROME_USER_DIR = "C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data"
options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
options.add_argument("profile-directory=Default")

service = Service(executable_path="C:/chromedriver")
# initialize web driver

# navigate to the url

opts = uc.ChromeOptions()

opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
# opts.add_argument(f"user-data-dir={CHROME_USER_DIR}")
# opts.add_argument("profile-directory=Default")
uc.Chrome(user_data_dir="C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
opts.add_argument("profile-directory=Default")
opts.add_argument(f'--proxy-server=socks5://51.83.116.5:29269')
driver = uc.Chrome(options=opts)
driver.get('https://www.google.com/search?q=my+book&oq=my+&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyCQgCEAAYQxiKBTIJCAMQABhDGIoFMgkIBBAAGEMYigUyCQgFEC4YQxiKBTIHCAYQABiABDINCAcQABiDARixAxiABDINCAgQABiDARixAxiABDIKCAkQABixAxiABNIBCDE2MTFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8')
# find element by partial link text
myLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'My Book')
myLink.click()
