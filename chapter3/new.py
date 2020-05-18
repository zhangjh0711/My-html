import pymongo

class HefengDb():
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.book_weather = self.client['weather']
        self.sheet_weather = self.book_weather['sheet_weather_3']

    def save(self,data):
        self.sheet_weather.insert_one(data)

    def show_all(self):
        all=self.sheet_weather.find()
        for each in all:
            print(each)

    def find(self,condition):
        return self.sheet_weather.find(condition)
    def delete(self):
        self.sheet_weather.dete_many({})


if __name__=="__main__":
    hefengDb=HefengDb()
    hefengDb.save({"name":"wangjiayi","class":"net19049"})
    hefengDb.show_all()


class TestCityWeatherDBCase(unittest.TestCase):

    def test_save(self):
        hefengDb = HefengDb()
        hefengDb.save({"name": "wangjiayi", "class": "net19049"})
        hefengDb.show_all()
        results=hefengDb.find({"name": "wangjiayi"})
        for each in results:
            self.assertEqual("wangjiayi",each['name'])
            self.assertEqual("net19049", each['class'])
        hefengDb.delete()

if __name__ == '__main__':
    unittest.main()