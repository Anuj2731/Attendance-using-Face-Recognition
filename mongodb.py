import pymongo
from datetime import date



def UploadingAttendance(name, login, logout):
    cluster = pymongo.MongoClient("mongodb+srv://Milan945:milan945jsk@cluster0.1plce.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Attendance"]

    today = date.today()
    collection = db[str(today)]

    data = {"Name" : name, "Login Time": login, "Logout Time": logout}

    collection.insert_one(data)