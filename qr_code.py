import cv2 as cv
import pandas as pd

officers = pd.read_excel(
    "officers.xlsx"
)  # spreadsheet file path that contains members' names

cap = cv.VideoCapture(0)  # 0 = default camera
detector = cv.QRCodeDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    data, bbox, _ = detector.detectAndDecode(
        frame
    )  # use the data variable to determine the decoded QR code content

    if bbox is not None and data:
        # Draw box around detected QR code
        bbox = bbox.astype(int)
        for i in range(len(bbox[0])):
            pt1 = tuple(bbox[0][i])
            pt2 = tuple(bbox[0][(i + 1) % len(bbox[0])])
            cv.line(frame, pt1, pt2, (0, 255, 0), 2)
        cv.putText(frame, data, (20, 40), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        print("Decoded:", data)

    cv.imshow("QR Scanner", frame)

    # transpose to if data in sheet[name]: action
    if data in officers["NAME"].tolist():
        print(f"{data} is found in the officers list.")
        break
        # call face recognition

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()