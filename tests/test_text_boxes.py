import pytest

from pages.text_boxes_page import TextBox
from utils.test_data import Data


class TestTextBoxes:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.text_box = TextBox(self.page)

        self.page.goto('https://demoqa.com/text-box')

    def test_text_boxes(self, test_setup):
        """
        Test to verify the text boxes on the page
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        # fill the form
        self.text_box.set_user_name(Data.user_name)
        self.text_box.set_email(Data.email)
        self.text_box.set_current_address(Data.current_address)
        self.text_box.set_permanent_address(Data.permanent_address)
        self.text_box.submit_form()
        # check the result
        self.text_box.check_output_form(Data.user_name, Data.email, Data.current_address, Data.permanent_address)


