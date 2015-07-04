from .base import FunctionalTest
from unittest import skip


class LayoutAndStylingTest(FunctionalTest):
    @skip
    def test_layout_and_styling(self):
        # User goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # User should notice the input box is centered on the page
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5)
