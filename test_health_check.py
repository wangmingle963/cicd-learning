import unittest
from health_check import is_healthy


class HealthCheckTests(unittest.TestCase):
    def test_success(self):
        self.assertTrue(is_healthy(200))

    def test_server_error(self):
        self.assertFalse(is_healthy(500))


if __name__ == "__main__":
    unittest.main()
