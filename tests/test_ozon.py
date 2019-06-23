import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.ozon_page import OzonMainPage


def test_ozon():

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(
        executable_path='C:/Python/webdrivers/chromedriver.exe',
        chrome_options=chrome_options)
    driver.maximize_window()

    driver.get('https://ozon.ru')

    # Заполнить поле поиска
    page = OzonMainPage(driver=driver)
    page.fill_input(xpath=page.INPUT_SEARCH, value='Xiaomi')

    # Кликнуть кнопку найти
    page.click(xpath=page.SEARCH_BUTTON)

    # Открыть каталок
    page.click(xpath=page.CATALOG_BUTTON)

    # Выбрать Электроника
    page.click(xpath=page.click_section_by_name(section_name='Книги'))

    time.sleep(10)

    print()
