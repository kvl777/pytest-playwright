import pytest

from pages.checkboxes_page import Checkbox


class TestCheckboxes:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.checkbox = Checkbox(self.page)

        self.page.goto('https://demoqa.com/checkbox', wait_until='domcontentloaded')

    def test_checkboxes(self, test_setup):
        """
        Test to verify the checkboxes on the page
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.checkbox.expand_home_directory()

        self.checkbox.select_checkbox('Downloads')
        self.checkbox.check_results('Downloads')

        self.checkbox.select_checkbox('documents')
        self.checkbox.check_results('documents')

        self.checkbox.select_checkbox('desktop')
        self.checkbox.check_results('desktop')
