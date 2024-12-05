import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-66339-default-rtdb.firebaseio.com/"
})

ref = db.reference('Employees')

data = {
    "321654":
        {
            "name": "Mark Jordan",
            "department": "AI Labs",
            "starting_year": 2024,
            "total_attendance": 3,
            "year": 1,
            "last_attendance_time": "2024-10-05 00:54:34"
        },
    "852741":
        {
            "name": "Peter Thiel",
            "department": "AI Labs",
            "starting_year": 2022,
            "total_attendance": 33,
            "year": 2,
            "last_attendance_time": "2024-09-22 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "department": "AI Labs",
            "starting_year": 2024,
            "total_attendance": 7,
            "year": 2,
            "last_attendance_time": "2024-08-23 00:54:34"
        },
    "999333":
        {
            "name": "Mrs Jordan",
            "department": "My Heart Department ngi",
            "starting_year": 2024,
            "total_attendance": 999,
            "year": 1,
            "last_attendance_time": "2024-08-23 00:54:34"
        },
            "10000":
        {
            "name": "Bryan",
            "department": "AI LABS",
            "starting_year": 2024,
            "total_attendance": 12,
            "year": 1,
            "last_attendance_time": "2024-08-23 00:54:34"
        },
            "10001":
        {
            "name": "Jahn",
            "department": "AI LABS",
            "starting_year": 2024,
            "total_attendance": 4,
            "year": 1,
            "last_attendance_time": "2024-08-23 00:54:34"
        },
            "666666":
        {
            "name": "FritzyZestyBOy",
            "department": "NiggaLabs",
            "starting_year": 2024,
            "total_attendance": 4,
            "year": 1,
            "last_attendance_time": "2024-08-23 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)