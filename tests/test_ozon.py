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
    page = OzonMainPage(driver=driver)

    # Открыть каталок
    page.click(xpath=page.CATALOG_BUTTON)

    # В Разделах выбрать Электроника -> Смартфоны
    page.navigation_selection(section_name='Электроника', section_button_name='Смартфоны')

    # Установить фильтр по производителю
    page.select_checkbox_brand_name(brand_name='Samsung')

    # Сортировать по цене
    page.sorting_by_name('Сначала дорогие')

    page.add_to_cart(value='0')
    page.go_to_cart()
    time.sleep(10)
    page.total_amount()
    page.comparison_price_and_total_amount()
    time.sleep(15)
