from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, xpath: str):
        """Метод получения вэб элемента по xpath

        Args:
            xpath: xpath

        Returns:
            element: вэб-элемент
        """
        try:
            element = WebDriverWait(driver=self.driver, timeout=20).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            element = self.driver.find_element(By.XPATH, xpath)
        return element

    def wait_clickable_element(self, xpath: str):
        """Метод проверки элемента на кликабильность

        :param xpath: xpath
        """
        element = WebDriverWait(driver=self.driver, timeout=20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

        return element

    def click(self, xpath):
        """Метод нажатия на элемент

        :param xpath: xpath
        """
        element = self.get_element(xpath=xpath)
        element.click()

    def fill_input(self, xpath, value):
        """Метод заполняет поле

        Args:
            xpath: xpath
            value: значение которым заполняется

        Returns:

        """
        element = self.get_element(xpath=xpath)
        element.send_keys(value)

    def clear_input(self, xpath):
        """Метод очистки поля ввода

        :param xpath: xpath
        """
        cleaner = self.get_element(xpath=xpath)
        cleaner.clear()

    def element_hover(self, xpath):
        """Метод наведения курсора мыши элемент

        :param xpath: xpath
        """

        element = self.wait_clickable_element(xpath=xpath)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).click().perform()

    def click_section_by_name(self, section_name: str):
        """Метод нажатия кнопки на сайте, с определенным текстом

        :param button_name: Текст на кнопке
        """
        xpath = self.SECTION_BUTTON.format(section_name=section_name)
        self.get_element(xpath=xpath)
        self.click(xpath=xpath)

    def quit_browser(self):
        """Метод закрытия браузера

        """
        self.driver.quit()

    def time_sleeper(self, value: int):
        """Вспомогательный таймер для написания тестов (Не использовать в готовом коде!!!)

        :param value: секунд
        """
        time.sleep(value)

    def navigation_selection(self, section_name, section_button_name):

        xpath_menu = self.CATALOG_SECTION.format(section_name=section_name)
        xpath_button = self.CATALOG_SECTION_BUTTON.format(section_button_name=section_button_name)
        add = self.driver.find_element(By.XPATH, xpath_menu)
        hover = ActionChains(self.driver).move_to_element(add)
        hover.perform()
        section_button = self.driver.find_element(By.XPATH, xpath_button)
        section_button.click()

    def select_checkbox_brand_name(self, brand_name):
        xpath = self.CHECKBOX_BRAND_NAME.format(brand_name=brand_name)
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
