from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        # User should not be able to accidentally add an empty list item
        self.fail('write me!')
