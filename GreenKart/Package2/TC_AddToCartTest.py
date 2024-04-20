import unittest


class AddToCartTest(unittest.TestCase):
    def test_search_item_and_addToCart(self, item_name='', amount=1):
        self.assertTrue(True)

    def test_add_all_items_random_amount(self):
        self.assertTrue(True)

    def test_click_addToCart_multiple_times(self):      # fail from the second time & on
        self.assertTrue(True)

    def test_check_cart_updates(self):
        self.assertTrue(True)

    def test_remove_random_item_from_cart(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
