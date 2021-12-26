from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import datetime

# The app request travel time data in every 15 minutes from waze.com, and save them to a text file. (It works 24 hours.)
def web_scraping():
    count = 0
    os.environ['PATH'] += r"C:/SeleniumDrivers"
    while count < 96:
        driver = webdriver.Chrome()
        driver.get('https://www.waze.com/en/live-map/directions/tokol-magyarorszag?utm_source=website&utm_medium=\
        homepage&utm_campaign=iframe+module&to=place.ChIJHaMnPRvlQUcR8CYeDCnEAAQ&from=place.ChIJC0BjZOzdQUcR4NUeDCnEAAU')
        time.sleep(8)  # 4 is enough on my pc, and connection, but I set 8 to be sure.
        my_element = driver.find_element(By.CSS_SELECTOR, ".wm-routes-item-desktop.is-active")
        my_class = my_element.find_element(By.CLASS_NAME, "wm-routes-item-desktop__header")
        my_path = my_class.find_elements(By.XPATH, "./span")
        my_span = my_path[1].find_elements(By.XPATH, "./span")
        result = my_span[0].get_attribute('innerHTML')  # divben 'text', spanben 'innerHTML'
        res_time = datetime.datetime.now().time()
        print(result)
        file_name = r'D:\my_text\my_text.txt'
        with open(file_name, 'a') as x_file:
            x_file.write(str(res_time) + ' ')
            x_file.write(result + '\n')
        count += 1
        driver.close()
        time.sleep(900)



def main():
    web_scraping()



if __name__ == "__main__":
    main()