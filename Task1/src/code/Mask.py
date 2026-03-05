import cv2
import numpy as np

def blur(img, blur_size=(5,5)):
    return cv2.GaussianBlur(img, blur_size, 0)

def get_edge(img, kernel_size=3):
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=kernel_size)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=kernel_size)

    magnitude = cv2.magnitude(sobel_x, sobel_y)

    return np.uint8(np.absolute(magnitude))



def get_mask(img_path, thredsold=40):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = blur(gray)

    magnitude = get_edge(blurred)

    _, edge_mask = cv2.threshold(magnitude, thredsold, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(edge_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    final_mask = np.zeros_like(gray)

    cv2.drawContours(final_mask, contours, -1, 255, thickness=cv2.FILLED)


    return final_mask