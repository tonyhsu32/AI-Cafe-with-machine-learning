# Importing the libraries
import cv2
import socket
import numpy as np
import adafruit_mod as mod

# -------------------------------------------
# Doing some Face Recognition with the webcam
# video 1
video_capture = cv2.VideoCapture(0)
video_capture.set(3, 320) #weight
video_capture.set(4, 240) #height

# -------------------------------------------

# -------------------------------------------
# 1 camera 1
TCP_IP = ""
print(TCP_IP)
TCP_PORT = 6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)

# -------------------------------------------

# -------------------------------------------
# accept client
conn, addr = s.accept()

# -------------------------------------------

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

while True:
    # -------------------------------------------
    # get frame
    _, frame = video_capture.read()
    
    # -------------------------------------------

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # -------------------------------------------
    # socket video 1
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = np.array(imgencode)
    stringData = data.tostring()

    #print(str(len(stringData)).ljust(16))
    conn.send(str(len(stringData)).ljust(16).encode(encoding='utf_8', errors='strict'))
    conn.send(stringData)

    # -------------------------------------------
    # socket sensor
    #dis = mod.sendSonic()
    #conn4.send(dis)
    # -------------------------------------------

    ret, frame = video_capture.read()
    decimg=cv2.imdecode(data,1)
    #cv2.imshow('SERVER2',decimg)    
    #cv2.imshow('Video', decimg)
    
    # receive socket msg
    res = conn.recv(1024)
    if res is "":
        print('Not get')
    elif res == b'Robo come':
        mod.go_stop()
        print(res)
    elif res == b'a cup of coffee ,please':
        mod.go_stop()
        print(res)
    elif res == b'13':
        mod.go_stop()
        print(res)
    elif res == b'6':
        mod.go_stop()
        print(res)
    elif res == b'Pay':
        mod.go_stop()
        print(res)
    # receive socket msg
    #traffic sign use (Peter
    #elif res == b'sf60':
        #mod.SP_60()
        #print(res)
    #elif res == b'sf30':
        #mod.SP_30()
        #print(res)
    #elif res == b'sr60':
        #mod.SP_60R()
        #print(res)
    #elif res == b'sr30':
        #mod.SP_30R()
        #print(res)
    #elif res == b'sl60':
        #mod.SP_60L()
        #print(res)
    #elif res == b'sl30':
        #mod.SP_30L()
    # elif res == b'stop':
        # mod.stop()
        # print(res)
#traffic sign use (Peter
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
#video_capture2.release()
#video_capture3.release()
cv2.destroyAllWindows()
