import cv2

def load_image(path_img):
    return cv2.imread(path_img)


def main():
    path_img = "images/IMG_21.jpeg"
    img = load_image(path_img)

    # resize to scale 0.2 (di perkecil) soalnya kalo tidak di resize layarnya tidak cukup
    imgResize = cv2.resize(img, None, fx=1, fy=1)

    # apply guassian blur on src image
    imgBlur = cv2.GaussianBlur(imgResize,(5,5),cv2.BORDER_DEFAULT)

    #menampilkan pada window
    cv2.imshow("Hasil", imgBlur)
    cv2.imshow("Source", imgResize)
    
    cv2.imwrite("hasil/hasil.jpeg", imgBlur)


main()
cv2.waitKey(0)