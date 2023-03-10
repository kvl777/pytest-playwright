from playwright.sync_api import Page


class RadioButton:

    def __init__(self, page: Page):
        self.page = page

        self.__result = self.page.locator('[class="text-success"]')

    def radio_button(self, name):
        return self.page.locator(f'input[id="{name.lower()}Radio"]')

    def select_radio_button(self, name) -> None:
        self.radio_button(name).check(force=True)

    def check_results(self, name) -> None:
        self.__result.wait_for(state='visible')
        assert self.__result.text_content() == name, f'Expected "{name}", got "{self.__result.text_content()}" instead'
        assert self.radio_button(name).is_checked(), f'Expected "{name}" radio is checked, but it is not'

    def check_previous_radio_unchecked(self, name) -> None:
        assert not self.radio_button(name).is_checked(), f'Expected "{name}" radio is not checked, but it is'


