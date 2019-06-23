from pages.base_page import BasePage


class OzonMainPage(BasePage):

    SEARCH_BUTTON = '//div[contains(@class, "search-button")]'
    INPUT_SEARCH = '//input[contains(@class, "search-input")]'
    CATALOG_BUTTON = '//div[@class="catalog-button"]'
    CATALOG_ELECTRONICS = '//*[@data-test-category-name="Электроника"]'
    SECTION_BUTTON = '//*[@data-test-category-name="{section_name}"]'
