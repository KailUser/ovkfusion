import unittest
from ovkfusion.auth import Auth

class TestAuth(unittest.TestCase):
    def test_login(self):
        auth = Auth("USER", "#############")
        assert auth.get_token()

if __name__ == "__main__":
    unittest.main()