
from PIL import Image, ImageDraw
import face_recognition

##Find faces in pictures
#image = face_recognition.load_image_file("johnsnow_test1.jpg")
#face_locations = face_recognition.face_locations(image)
#print(face_locations)

#Find and manipulate facial features in pictures
image = face_recognition.load_image_file("johnsnow_test1.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)

for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')

    # Make the eyebrows into a nightmare
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Sparkle the eyes
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

    pil_image.show()

##Identify faces in pictures
#known_image = face_recognition.load_image_file("biden.jpg")
#unknown_image = face_recognition.load_image_file("unknown.jpg")

#biden_encoding = face_recognition.face_encodings(known_image)[0]
#unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

#results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
#print(results)