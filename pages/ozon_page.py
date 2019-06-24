from pages.base_page import BasePage


class OzonMainPage(BasePage):

    SEARCH_BUTTON = '//div[contains(@class, "search-button")]'
    INPUT_SEARCH = '//input[contains(@class, "search-input")]'
    CATALOG_BUTTON = '//div[@class="catalog-button"]'
    CATALOG_SECTION = '//*[@data-test-category-name="{section_name}"]'
    CATALOG_SECTION_BUTTON = '//*[@data-test-category-name="{section_button_name}"]'
    CHECKBOX_BRAND_NAME = '//*[contains(text(), "{brand_name}")]/ancestor::label[contains(@data-test-id, "filter-block-brand-item")]'
    SHOW_ALL_BRANDS = '//*[contains(text(), "Посмотреть все")][@data-test-id="filter-block-brand-show-all"]/..'

    SAMSUNG_CHECKBOX = '//*[contains(text(), "Samsung")]/ancestor::label[contains(@data-test-id, "filter-block-brand-item")]//input'
    CATALOG_ELECTRONICS = '//*[@data-test-category-name="Электроника"]'
    SECTION_BUTTON_BOOK = '//*[@data-test-category-name="Книги"]'
    SECTION_MOBILE_PHONES = '//*[@data-test-category-name="Смартфоны"]'

