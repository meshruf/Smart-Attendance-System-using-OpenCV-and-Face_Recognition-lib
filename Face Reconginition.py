import cv2
import numpy as np
import face_recognition

imgTom= face_recognition.load_image_file('F:\My Projects\Face Recognition and smart Attendence system\Data\Tom_C.jpg')
imgTom=cv2.cvtColor(imgTom,cv2.COLOR_BGR2RGB)
imgTest= face_recognition.load_image_file('F:\My Projects\Face Recognition and smart Attendence system\Data\Tom_CT.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLocation=face_recognition.face_locations(imgTom)[0]
encodeTom=face_recognition.face_encodings(imgTom)[0]
cv2.rectangle(imgTom,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,0),2)


faceLocationTest=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocationTest[3],faceLocationTest[0]),(faceLocationTest[1],faceLocationTest[2]),(255,0,0),2)


results= face_recognition.compare_faces([encodeTom],encodeTest)
faceDistance=face_recognition.face_distance([encodeTom],encodeTest)
print(results, faceDistance)
cv2.putText(imgTest, f'{results} {round(faceDistance[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow("Tom_Cr", imgTom)
cv2.imshow("Tom_Test", imgTest)
cv2.waitKey(0)
