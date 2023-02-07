import time
from clear_screen import clear

def oxygen():
    clear()
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait as WDW
    from selenium.webdriver.chrome.service import Service as ChromeService 
    from webdriver_manager.chrome import ChromeDriverManager

    delay = int(input('Delay: '))
    username = input('Username: ')
    amount = int(input('Amount: '))

    options = webdriver.ChromeOptions() 
    options.add_argument("--headless")
    options.add_argument("--silent")
    

    with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: 
        github_profile = f'https://github.com/{username}'

        driver.get(github_profile)
        print('Driver has started')

        WDW(driver, 5).until(EC.presence_of_all_elements_located)
        for _ in range(amount):

            driver.refresh()
            print(f'Sent 1 view to github.com/{username}')
            print(f'Sleeping for {delay} seconds\n')
            time.sleep(delay)


if __name__ == '__main__':
    from threading import Thread
    thread_workers = []
    t = Thread(target=oxygen)
    thread_workers.append(t)
    t.start()

    for t in thread_workers:
        t.join()