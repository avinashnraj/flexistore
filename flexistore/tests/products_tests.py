import unittest
import json
import requests


class ProductTest(unittest.TestCase):

    def test_get_products(self):
        response = requests.get('http://localhost:8000/products/')
        if response:
            self.assertEqual(200, response.status_code)
            with open("resources/products.json") as f:
                self.assertEqual(json.load(f), response.json())

    def test_post_product(self):
        data = {
            "name": "mbnkj",
            "uom_id": 1,
            "price_per_unit": 45
        }
        response = requests.post('http://localhost:8000/products/', data=data)
        if response:
            self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
