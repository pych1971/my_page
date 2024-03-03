from django.test import TestCase
from horoscope.views import zodiac_dict


# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      response.content.decode())

    def test_signs(self):
        for sign in zodiac_dict:
            response = self.client.get(f'/horoscope/{sign}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(zodiac_dict[sign], response.content.decode())

    def test_libra_redirect(self):
        response = self.client.get('/horoscope/7')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra')
