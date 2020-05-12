import pymongo

class HefengDb():
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.book_weather=self.client['weather']
        self.sheet_weather=self.book_weather['sheet_weather_3']

    def save(self, param):
        pass


def save(self,data):
    self.sheet_weather.insert_one(data)
def 


if __name__=="__main__":
    # client=pymongo.MongoClient('localhost',27017)
    # book_weather=client['weather']
    # sheet_weather=book_weather['sheet_weather_3']
    # print(sheet_weather)
    # sheet_weather.insert_one({"name":"zjh","class":"19049"})
    hefengDb=HefengDb()
    hefengDb.save({"name":"zjh","class":"net19049"})