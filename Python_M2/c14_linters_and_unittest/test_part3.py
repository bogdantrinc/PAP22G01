import json
import unittest
from file2 import time_getter
from unittest.mock import patch, MagicMock

output = ['Europe/Amsterdam', 'Europe/Andorra']


class TestTimeGetter(unittest.TestCase):
    # @patch('c14_linters_and_unittest.file2.requests.get')
    # def test_response(self, get_mock: MagicMock):
    #     get_mock.return_value = MagicMock(text=json.dumps([output]))
    #     self.assertEqual(time_getter('Europe'), output)

    # @patch('c14_linters_and_unittest.file2.requests.get')
    # def test_response_2(self, get_mock: MagicMock):
    #     get_mock.return_value = json.dumps(output)
    #     self.assertEqual(time_getter('Europe'), output)

    @patch('c14_linters_and_unittest.file2.requests.get')
    def test_response(self, get_mock: MagicMock):
        get_mock.return_value = MagicMock(text=MagicMock(abcd=json.dumps(output)))
        self.assertEqual(time_getter('Europe'), output)


if __name__ == "__main__":
    unittest.main()
