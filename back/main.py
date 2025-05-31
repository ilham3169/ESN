from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import logging, time

logging.getLogger('tensorflow').setLevel(logging.ERROR)
logging.getLogger('selenium').setLevel(logging.ERROR)

options = Options()
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=C:/ChromeDebugProfile")
options.add_argument("--log-level=3")
service = Service(log_path='NUL')
driver = webdriver.Chrome(service=service, options=options)

numbers = ["+994559667744", "+994 70 412 45 35"]

def sending_message(driver, phone_number, message):
    try:
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
        print(f"Trying to send a message to {phone_number}")
        driver.get(url)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-tab='10']"))
        )
        time.sleep(1)
        msg_box = driver.find_element(By.XPATH, "//div[@data-tab='10']")
        msg_box.send_keys(Keys.ENTER)
        print("Message sent successfully")
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")

try:
    print("Redirecting to WhatsApp Web")
    driver.get("https://web.whatsapp.com")
    driver.execute_script("document.documentElement.requestFullscreen();")
    input("If you scanned your QR code, press any key to continue...")
    time.sleep(3)

    print("################# WE ARE IN MAIN MENU #################")
    for number in numbers:
        sending_message(driver, number, "Hello from Selenium!")

    input("Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")
    input("Press Enter to close the browser...")

finally:
    driver.quit()
    print("Browser closed.")
