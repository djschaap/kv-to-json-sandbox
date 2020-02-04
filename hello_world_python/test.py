import unittest

from hello_world_python import lambda_function

class TestHelloWorld(unittest.TestCase):
    def test_lambda_handler(self):
        data = {
            "key1": "v1",
            "key2": "v2",
            "key3": "v3",
        }
        result = lambda_function.lambda_handler(data, None)
        self.assertEqual(result, "v1")

if __name__ == '__main__':
    unittest.main()
