import cv2 as cv
import face_recognition as fr

# --- Enrollment: one image per person, done once before the loop ---
known_encodings = []
known_names = []

people = {
    "beverly": "image/Carisma.jpg",
    "meryl": "image/Rapista.png",
    "kenneth": "image/Casaquite.png",
    "cathlene": "image/Araña.png",
}

for name, path in people.items():
    img = fr.load_image_file(path)
    encoding = fr.face_encodings(img)[0]
    known_encodings.append(encoding)
    known_names.append(name)


def recognize_face(face_encoding, tolerance=0.6):
    distances = fr.face_distance(known_encodings, face_encoding)
    best_match_index = distances.argmin()

    if distances[best_match_index] < tolerance:
        return known_names[best_match_index]
    return "Unknown"


def scan_face():
    camera = cv.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture frame from camera. Exiting...")
            break

        subject_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        face_locations = fr.face_locations(subject_frame)
        face_encodings = fr.face_encodings(subject_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings
        ):
            name = recognize_face(face_encoding)

            cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv.putText(
                frame,
                name,
                (left, top - 10),
                cv.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

        cv.imshow("Face Detection", frame)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv.destroyAllWindows()


scan_face()


# Use pandas to reuse the names. Store the names inside the known_names list.
# Add a column on the excel file that contains the image path of the person.
