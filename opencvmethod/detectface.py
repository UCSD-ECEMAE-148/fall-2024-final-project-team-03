def detectface(frame):
    import cv2

    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    if len(faces) == 1:
        face_coords = faces[0]
        xcenter = face_coords[0] + face_coords[2]/2
        ycenter = face_coords[1] + face_coords[3]/2
        return [xcenter,ycenter]
    else:
        return False

