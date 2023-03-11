# Number Plate detection using build in cascade
import cv2

i=1

while True:

    img = cv2.imread('Resources/p'+str(i)+'.jpg')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(img.shape[:2])

    numberPlateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
    nPlates = numberPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    cv2.imshow("Result", img)

    for (x,y,w,h) in nPlates:
     area = w*h

    if area>500:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,"Number Plate",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

        #crope number plate area
        imgRoi = img[y:y+h,x:x+w]
        cv2.imshow("Plate Number", imgRoi)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/Number_plate_" + str(i) + ".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (img.shape[1], 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Number Plate Saved", (img.shape[1]//4, 270), cv2.FONT_HERSHEY_DUPLEX,
                    1, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        i = i + 1

    if i>3:
        break