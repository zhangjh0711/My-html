import unittest

from chapter3.city_weather_db import HefengDb


class TestCityWeatherDbCase(unittest.TestCase):
    def test_save(self):
        hefengDb = HefengDb()
        hefengDb.save({"name": "zjh", "class": "net19049"})
        hefengDb.show_all()
        results=hefengDb.find({"name":"zjh"})
        for each in results:
            self.assertEqual("zjh",each['name'])
            self.assertEqual("net19049", each['class'])
        hefengDb.delete()


if __name__ == '__main__':
    unittest.main()
