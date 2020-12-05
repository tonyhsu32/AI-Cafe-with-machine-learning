import face_recognition
import cv2

# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Open the input movie file
#input_movie = cv2.VideoCapture("Alec Baldwin returns as Trump.mp4")
input_movie = cv2.VideoCapture(0)
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
output_movie = cv2.VideoWriter('output.avi', fourcc, 29.97, (int(input_movie.get(3)), int(input_movie.get(4))))

#fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#output_movie = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

# Load some sample pictures and learn how to recognize them.
Trump1_image = face_recognition.load_image_file("Trump1.jpg")
Trump1_face_encoding = face_recognition.face_encodings(Trump1_image)[0]

JieweiShi_image = face_recognition.load_image_file("jiewei shi.jpg")
JieweiShi_face_encoding = face_recognition.face_encodings(JieweiShi_image)[0]

AlanChen_image = face_recognition.load_image_file("alan chen.jpg")
AlanChen_face_encoding = face_recognition.face_encodings(AlanChen_image)[0]

known_faces = [
    Trump1_face_encoding,
    JieweiShi_face_encoding,
    AlanChen_face_encoding

]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "Trump1"
        elif match[1]:
            name = "Jiewei Shi"
        elif match[2]:
            name="Alan Chen"

        face_names.append(name)

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

# All done!
output_movie.release()
input_movie.release()
cv2.destroyAllWindows()

