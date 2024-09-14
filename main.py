from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com/")

# Wait until the search bar element is loaded
wait = WebDriverWait(driver, 10)
input_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

# Clear any pre-filled text in the search bar
input_element.clear()

# Type in the search query and hit Enter
input_element.send_keys("BLSITALY Pakistan" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Welcome to BLS Italy").click()

# Optional: Add a wait to observe the search results
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
