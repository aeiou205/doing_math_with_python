import cv2
import numpy as np
import math
capture = cv2.VideoCapture(0)
import math
from PIL import Image, ImageDraw
import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow

#triangulo
#pendiente dereivada

i = 0 
while(capture.isOpened()):

    ret, frame = capture.read()
    height, width = frame.shape[:2]

    if( cv2.waitKey(20)==ord('q') ):
        break

    qrDetector = cv2.QRCodeDetector()
    # data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)

    roi = frame[0:height//2, 0:width//2] 

    dim = (width, height)
    # resize image
    resized = cv2.resize(roi, dim, interpolation = cv2.INTER_LANCZOS4)

    retval, decoded_info, points, straight_qrcode = qrDetector.detectAndDecodeMulti(resized)

    if retval:
        i = i+1
        print( i )
        print(decoded_info)

        img = cv2.polylines(resized, points.astype(int), True, (0, 255, 0), 3)

        for s, p in zip(decoded_info, points):
            # print(s)
            print(p)
            for pp in p:
                cv2.circle(frame, (pp[0].astype(int)//2, pp[1].astype(int)//2), 10, (255, 120, 255), 3 )
        

            if len(p) == 4:
                print(p[1][1])
                print("x0",p[0].astype(int)[0]//2)
                print("y0",p[0].astype(int)[1]//2) 

                print("x1",p[3].astype(int)[0]//2)
                print("y1",p[3].astype(int)[1]//2)


                cv2.line(frame, (p[0].astype(int)[0]//2, p[0].astype(int)[1]//2),
                                (p[3].astype(int)[0]//2, p[3].astype(int)[1]//2),
                                (255, 120, 80),3 )

                cv2.circle(frame, (p[0].astype(int)[0]//2, p[0].astype(int)[1]//2), 10, (55, 120, 155), -3 )
                cv2.circle(frame, (p[3].astype(int)[0]//2, p[0].astype(int)[1]//2), 10, (55, 120, 155), -3 )

                dx1 = (p[0].astype(int)[0]//2 - p[3].astype(int)[0]//2 )
                dy1 = (p[0].astype(int)[1]//2 - p[3].astype(int)[1]//2 )

                cv2.line(frame, (p[0].astype(int)[0]//2, p[0].astype(int)[1]//2),
                                (p[0].astype(int)[0]//2 - 5*dx1, p[0].astype(int)[1]//2 - 5*dy1 ),
                                (55, 25, 155),3 )

                cv2.line(frame, (p[0].astype(int)[0]//2, p[0].astype(int)[1]//2),
                                (p[0].astype(int)[0]//2 + 5*dx1, p[0].astype(int)[1]//2 + 5*dy1 ),
                                (55, 25, 155),3 )


                cv2.circle(frame, (p[1].astype(int)[0]//2, p[1].astype(int)[1]//2), 10, (55, 20, 155), -3 )
                cv2.circle(frame, (p[2].astype(int)[0]//2, p[1].astype(int)[1]//2), 10, (55, 120, 155), -3 )

                dx2 = (p[1].astype(int)[0]//2 - p[2].astype(int)[0]//2 )
                dy2 = (p[1].astype(int)[1]//2 - p[2].astype(int)[1]//2 )

                cv2.line(frame, (p[1].astype(int)[0]//2, p[1].astype(int)[1]//2),
                                (p[1].astype(int)[0]//2 - 5*dx2, p[1].astype(int)[1]//2 - 5*dy2 ),
                                (55, 25, 155),3 )

                cv2.line(frame, (p[1].astype(int)[0]//2, p[1].astype(int)[1]//2),
                                (p[1].astype(int)[0]//2 + 5*dx2, p[1].astype(int)[1]//2 + 5*dy2 ),
                                (55, 25, 155), 3 )


                print("dy1 dy2 : ", dy1, dy2)
                print("dx1 dx2 : ", dx1, dx2)
                
                


            img = cv2.putText(img, s, p[0].astype(int),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    cv2.circle(frame, (width//2, height//2), 10, (55, 250, 90), -3 )


    cv2.imshow('webCam', resized)
    cv2.imshow('raw', frame)

    
capture.release()
cv2.destroyAllWindows()
