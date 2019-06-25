from pages.base_page import BasePage


class OzonMainPage(BasePage):

    SEARCH_BUTTON = '//div[contains(@class, "search-button")]'
    INPUT_SEARCH = '//input[contains(@class, "search-input")]'
    CATALOG_BUTTON = '//div[@class="catalog-button"]'
    CATALOG_SECTION = '//*[@data-test-category-name="{section_name}"]'
    CATALOG_SECTION_BUTTON = '//*[@data-test-category-name="{section_button_name}"]'

    """Brand-Filters"""
    FILTER_BLOCK_BRAND = '//div[@data-test-id="filter-block-brand"]'
    CHECKBOX_BRAND_NAME = '//*[contains(text(), "{brand_name}")]/preceding-sibling::span[@class="checkmark"]'
    SHOW_ALL_BRANDS = '//*[@data-test-id="filter-block-brand-show-all"]'
    SEARCH_BRAND_INPUT = '//div[@data-test-id="filter-block-brand"]//input[@type="text"][@class="input"]'
    """Brand-Filters"""

    """Sorting"""
    SORTING_SELECT = '//div[@class="select sorting-select"]'
    SORTING_BY_NAME = '//*[contains(text(), "{sorting_method}")][@role="option"]'
    """Sorting"""
