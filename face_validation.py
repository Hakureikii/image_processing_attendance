import cv2 as cv
import face_recognition as fr

def scan_face():
   camera = cv.VideoCapture(0)
   while True:
      ret, frame = camera.read()
      if not ret:
         print("Failed to capture frame from camera. Exiting...")
         break

      subject_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
      face_locations = fr.face_locations(subject_frame)

      # face detection and drawing rectangle around the detected face
      for (top, right, bottom, left) in face_locations:
         cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

      # Display the resulting frame with detected faces
      cv.imshow('Face Detection', frame)

      # Event listener for 'q' key to quit the application
      if cv.waitKey(1) & 0xFF == ord('q'):
         break


scan_face()