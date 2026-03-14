import cv2
import numpy as np

src = cv2.imread("Image/resized_source.jpg")
clone = src.copy()
points = []

def draw_polygon(event, x, y, flags, param):
    global points
    
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(clone, (x, y), 3, (0, 0, 255), -1)

cv2.namedWindow("Select Object")
cv2.setMouseCallback("Select Object", draw_polygon)

while True:
    cv2.imshow("Select Object", clone)
    key = cv2.waitKey(1)
    
    if key == ord("c"):  # Nhấn C để hoàn thành
        break

cv2.destroyAllWindows()

# Tạo mask từ đa giác
mask = np.zeros(src.shape[:2], dtype=np.uint8)
pts = np.array(points, np.int32)
cv2.fillPoly(mask, [pts], 255)

cv2.imwrite("mask.png", mask)