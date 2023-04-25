"""

A tester

"""

import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite("resources/output/image/webcam/image_buffer.png", frame)
        break

vid.release()
cv2.destroyAllWindows()
