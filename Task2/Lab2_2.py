import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread("Image/resized_source_black-house-spider_src-1.jpg")
h, w = img.shape[:2]

#Translation (Tịnh tiến)
tx, ty = 100, 50
M_translation = np.float32([[1, 0, tx],
                            [0, 1, ty]])

translated = cv2.warpAffine(img, M_translation, (w, h))

#Rotation (Xoay)
angle = 30
scale = 1.0
center = (w//2, h//2)

M_rotation = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(img, M_rotation, (w, h))

#Scaling (Phóng to/thu nhỏ)
scaled = cv2.resize(img, None, fx=0.5, fy=0.5)


#Affine Transformation

pts1 = np.float32([[50,50],
                   [200,50],
                   [50,200]])

pts2 = np.float32([[10,100],
                   [200,50],
                   [100,250]])

M_affine = cv2.getAffineTransform(pts1, pts2)
affine = cv2.warpAffine(img, M_affine, (w, h))


#Projective (Homography)


pts1_h = np.float32([[50,50],
                     [w-50,50],
                     [w-50,h-50],
                     [50,h-50]])

pts2_h = np.float32([[10,100],
                     [w-100,50],
                     [w-50,h-50],
                     [100,h-100]])

H = cv2.getPerspectiveTransform(pts1_h, pts2_h)
projective = cv2.warpPerspective(img, H, (w, h))


# Hiển thị kết quả


cv2.imshow("Original", img)
cv2.imshow("Translation", translated)
cv2.imshow("Rotation", rotated)
cv2.imshow("Scaling", scaled)
cv2.imshow("Affine", affine)
cv2.imshow("Projective", projective)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Result/Task2_translated.jpg",translated)
cv2.imwrite("Result/Task2_rotated.jpg",rotated)
cv2.imwrite("Result/Task2_scaled.jpg",scaled)
cv2.imwrite("Result/Task2_affine.jpg",affine)
cv2.imwrite("Result/Task2_projective.jpg",projective)