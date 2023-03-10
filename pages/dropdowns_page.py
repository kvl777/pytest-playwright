import random

from playwright.sync_api import Page


class DropdownMenu:

    def __init__(self, page: Page):
        self.page = page

        self.__select_value_dropdown = self.page.locator('[id="withOptGroup"]')
        self.__group1_option1_item = self.page.locator('//div[text()="Group 1, option 1"]')
        self.__select_one_dropdown = self.page.locator('[id="selectOne"]')
        self.__select_old_style_dropdown = self.page.locator('select[id="oldSelectMenu"]')
        self.__professor_item = self.page.locator('//div[text()="Prof."]')
        self.__multiselect_dropdown = self.page.locator('(//div[@class=" css-1hwfws3"])[3]')
        self.__volvo_standard_multi_select_item = self.page.locator('option[value="volvo"]')
        self.__audi_standard_multi_select_item = self.page.locator('option[value="audi"]')

    def select_group1_option1_item(self) -> None:
        self.__select_value_dropdown.click()
        self.__group1_option1_item.click()

    def select_professor_item(self) -> None:
        self.__select_one_dropdown.click()
        self.__professor_item.click()

    def select_all_colors_from_multiselect(self, colors) -> None:
        self.__multiselect_dropdown.click()
        for color in colors:
            color_option = self.page.locator(f'//div[text()="{color}"]')
            color_option.click()

    def select_all_cars(self) -> None:
        self.__volvo_standard_multi_select_item.drag_to(self.__audi_standard_multi_select_item)

    def select_color_from_old_dropdown(self) -> None:
        color_option = str(random.randint(1, 10))
        self.__select_old_style_dropdown.select_option(color_option)
