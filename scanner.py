import cv2 as cv
import face_recognition as fr
import pandas as pd


class Scanner:
    def __init__(self):
        self.cap = cv.VideoCapture(0)  # 0 = default camera
        self.detector = cv.QRCodeDetector()
        self.officers = pd.read_excel("officers.xlsx")

    def scan_qr_code(self) -> bool:
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            data, bbox, _ = self.detector.detectAndDecode(
                frame
            )  # use the data variable to determine the decoded QR code content

            if bbox is not None and data:
                # Draw box around detected QR code
                bbox = bbox.astype(int)
                for i in range(len(bbox[0])):
                    pt1 = tuple(bbox[0][i])
                    pt2 = tuple(bbox[0][(i + 1) % len(bbox[0])])
                    cv.line(frame, pt1, pt2, (0, 255, 0), 2)
                cv.putText(
                    frame, data, (20, 40), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
                )
                print("Decoded:", data)

            cv.imshow("QR Scanner", frame)

            # transpose to if data in sheet[name]: action
            if data in self.officers["NAME"].tolist():
                print(f"{data} is found in the officers list.")
                return True
                # call face recognition

            if cv.waitKey(1) & 0xFF == ord("q"):
                break

    def scan_face(self) -> bool:
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to capture frame from camera. Exiting...")
                break

            subject_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            face_locations = fr.face_locations(subject_frame)

            # face detection and drawing rectangle around the detected face
            for top, right, bottom, left in face_locations:
                cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Display the resulting frame with detected faces
            cv.imshow("Face Detection", frame)

            # Event listener for 'q' key to quit the application
            if cv.waitKey(1) & 0xFF == ord("q"):
                break

    def kill(self):
        self.cap.release()
        cv.destroyAllWindows()
