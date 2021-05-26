import cv2

def one():
    img = cv2.imread('img\KakaoTalk_20210514_165309223_01.jpg',cv2.IMREAD_REDUCED_COLOR_2)

    cv2.imshow('img',img)
    cv2.waitKey()
    cv2.destroyAllWindows(27)
one()
