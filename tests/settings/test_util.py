from unittest import TestCase

from kition_djangodefaults.settings.util import convert_http_header_to_django


class TestUtil(TestCase):
    def test_accept(self):
        self.assertEqual("ACCEPT", convert_http_header_to_django("Accept"))

    def test_x_example(self):
        self.assertEqual("HTTP_X_EXAMPLE", convert_http_header_to_django("X-Example"))

    def test_x_example__lowercase(self):
        self.assertEqual("HTTP_X_EXAMPLE", convert_http_header_to_django("x-example"))

    def test_x_forwarded_proto(self):
        self.assertEqual(
            "HTTP_X_FORWARDED_PROTO", convert_http_header_to_django("X-Forwarded-Proto")
        )
