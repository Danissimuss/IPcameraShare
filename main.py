import cv2 as opencv

cap = opencv.VideoCapture('rtsp://admin:123@192.168.100.4:554')
while(True):
    ret, frame = cap.read()
    opencv.imshow('frame',frame)
    if ret:
        opencv.imwrite('first_frame.jpg', frame)
        print('Первый кадр сохранен как first_frame.jpg')

    if opencv.waitKey(1) & 0xFF == ord('q'):
        opencv.destroyAllWindows()
        break