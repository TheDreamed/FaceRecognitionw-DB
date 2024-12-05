import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-66339-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-66339.appspot.com"
})

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    if img is not None:  # Check if the image was loaded correctly
        imgList.append(img)
        studentIds.append(os.path.splitext(path)[0])

        # Upload to Firebase Storage
        fileName = f'{folderPath}/{path}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
    else:
        print(f"Error loading image {path}")

print("Student IDs:", studentIds)

# Function to find encodings
def findEncodings(imagesList):
    encodeList = []
    for idx, img in enumerate(imagesList):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)

        # Check if a face encoding was found
        if len(encodings) > 0:
            encodeList.append(encodings[0])
        else:
            print(f"No face found in image {studentIds[idx]} - Skipping encoding for this image.")

    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
if len(encodeListKnown) == len(studentIds):
    print("All images encoded successfully.")
else:
    print(f"Some images were skipped. Encoded {len(encodeListKnown)} out of {len(studentIds)} images.")

encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# Save the encodings to a pickle file
with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)

print("EncodeFile.p saved successfully")
