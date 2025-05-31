from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import logging, time
from urllib.parse import quote  
import os

os.system("cls")

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

logging.getLogger('tensorflow').setLevel(logging.ERROR)
logging.getLogger('selenium').setLevel(logging.ERROR)

options = Options()
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=C:/ChromeDebugProfile")
options.add_argument("--log-level=3")
service = Service(log_path='NUL')
driver = webdriver.Chrome(service=service, options=options)

def sending_message(driver, phone_number, message):
    try:
        encoded_message = quote(message, safe='')
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
        print(f"{CYAN}Attempting to send message to {phone_number}{RESET}")
        driver.get(url)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-tab='10']"))
        )
        time.sleep(1)
        msg_box = driver.find_element(By.XPATH, "//div[@data-tab='10']")
        msg_box.send_keys(Keys.ENTER)
        print(f"{GREEN}Message sent successfully{RESET}")
        time.sleep(7)
        print(f"{YELLOW}Waiting to avoid spam detection{RESET}")
    except Exception as e:
        print(f"{RED}Error sending message: {e}{RESET}")

file = open('numbers.txt', 'r')
numbers = file.readlines()

message = """Dear participant

Congratulations!
You have been shortlisted for the upcoming Ultimate Farewell Party organized by ESN Azerbaijan on May 24 at Pablo RestorBar.

To confirm your spot, please complete your payment as soon as possible, as spaces are limited and will be secured on a first-paid, first-confirmed basis.

Ticket Prices:
- 13 AZN (ESNcard holders)
- 20 AZN (Standard entry)

Payment Details:
Card Number: 4098 5844 7140 1784

After payment, reply to this email with:
1. A screenshot or photo of your payment receipt
2. Your full name

Event Info Recap:
Date: May 24
Time: 18:00
Location: Pablo RestorBar
Includes a FREE welcome shot on arrival!

Dress Code: Black & White – bold, classy, or chic, just stay monochrome!

If you have any questions, feel free to reach out

Looking forward to celebrating together!"""

try:
    print(f"{CYAN}Redirecting to WhatsApp Web{RESET}")
    driver.get("https://web.whatsapp.com")
    driver.execute_script("document.documentElement.requestFullscreen();")
    input(f"{YELLOW}Scan QR code and press any key to continue when the chats are shown...{RESET}")
    time.sleep(10)

    try:
        print(f"{CYAN}Attempting to click 'Continue'{RESET}")
        driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div/button').click()
        print(f"{GREEN}Successfully clicked 'Continue'{RESET}")
    except:
        print(f"{RED}Couldn't find the 'Close' button{RESET}")

    print(f"{BOLD}{CYAN}WELCOME TO MAIN MENU{RESET}")
    for number in numbers:
        sending_message(driver, number.strip(), message)

    input(f"{YELLOW}Press Enter to close the browser...{RESET}")

except Exception as e:
    print(f"{RED}Fatal error: {e}{RESET}")
    input(f"{YELLOW}Press Enter to close the browser...{RESET}")

finally:
    driver.quit()
    print(f"{GREEN}Browser closed.{RESET}")