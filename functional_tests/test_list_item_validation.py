from .base import FunctionalTest
from lists.forms import DUPLICATE_ITEM_ERROR, EMPTY_ITEM_ERROR


class ItemValidationTest(FunctionalTest):
    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # User should not be able to accidentally add an empty list item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The page should refresh and display an error message saying
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, EMPTY_ITEM_ERROR)

        # User should be able to try again and enter text for the item
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # User again accidentally enter a blank item
        self.get_item_input_box().send_keys('\n')

        # User should get another error message
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, EMPTY_ITEM_ERROR)

        # User can once again correct the error by entering text for the item
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # User goes to home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # User accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')

        # User should receive an error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, DUPLICATE_ITEM_ERROR)
