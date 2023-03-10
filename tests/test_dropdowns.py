import pytest

from pages.dropdowns_page import DropdownMenu
from utils.test_data import Data


class TestDropdowns:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.menu = DropdownMenu(self.page)

        self.page.goto('https://demoqa.com/select-menu')

    def test_dropdowns(self, test_setup):
        """
        Test to verify the dropdown menus on the page
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.menu.select_group1_option1_item()
        self.menu.select_professor_item()
        self.menu.select_color_from_old_dropdown()
        self.menu.select_all_colors_from_multiselect(Data.colors)
        self.menu.select_all_cars()
