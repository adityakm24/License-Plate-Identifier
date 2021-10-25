import cv2
import numpy as np
import easyocr
import imutils

def detect(image):

    reader = easyocr.Reader(['en'])

    img = cv2.imread(image)

    if img.shape[0] > 620 and img.shape[1] > 480:              # Resizing if image is too large
        img = cv2.resize(img, (620,480))

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)          # Converting image to black and white

    filtered_img = cv2.bilateralFilter(gray_img, 11, 17, 17)   # Smoothing and reducing noise
    edge_map = cv2.Canny(filtered_img, 30, 200)                         # Applying edge detection

    # Finding contours
    cnts = cv2.findContours(edge_map.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts= sorted(cnts, key=cv2.contourArea, reverse=True)[:10] # Sorting the contours from big to small(top 10)

    # Finding our number plate from the contours
    plate = None
    for cnt in cnts:
        # Approximating the contour
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.018 * perimeter, True)

        # Checking if the approximated contour has 4 vetices(lisence plate)
        if len(approx) == 4:
            plate = approx
            break


    # Mask other parts of the image except the lisence plate
    mask = np.zeros(gray_img.shape, np.uint8)
    new_img = cv2.drawContours(mask, [plate], 0, 255, -1)
    new_img = cv2.bitwise_and(img, img, mask=mask)

    # Cropping the lisence plate
    # (x, y) = np.where(mask == 255)
    # (topx, topy) = (np.min(x), np.min(y))
    # (bottomx, bottomy) = (np.max(x), np.max(y))
    # crop_img = gray_img[topx: bottomx+1, topy: bottomy+1]

    # Reading the number plate
    text = reader.readtext(new_img)

    print(text[0][1])

    cv2.imshow("Number_Plate", new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
