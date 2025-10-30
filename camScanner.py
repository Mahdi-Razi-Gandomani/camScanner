import cv2
import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
image_path = 'images/input.png'
image = Image.open(image_path) 
image = np.array(image)  

# Convert to grayscale and detect edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 200)

# Find and sort contours
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # top-left
    rect[2] = pts[np.argmax(s)]  # bottom-right
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # top-right
    rect[3] = pts[np.argmax(diff)]  # bottom-left
    return rect

# Find the largest contour
largest_contour = max(contours, key=cv2.contourArea)

# Approximate the contour
perimeter = cv2.arcLength(largest_contour, True)
epsilon = 0.02 * perimeter
approx = cv2.approxPolyDP(largest_contour, epsilon, True)

# If not exactly 4 points, use convex hull and approximate again
if len(approx) != 4:
    hull = cv2.convexHull(largest_contour)
    approx = cv2.approxPolyDP(hull, epsilon, True)

# Handle error
if len(approx) != 4:
    raise ValueError("Cannot find a 4-point contour for the paper.")

paper = order_points(approx.reshape(4, 2))


# Draw contour
cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

# Perspective transformation
h, w, _ = image.shape
dst_points = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
matrix = cv2.getPerspectiveTransform(paper, dst_points)
warped = cv2.warpPerspective(image, matrix, (w, h))

# Apply adaptive thresholding
warped_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
thresholded = cv2.adaptiveThreshold(warped_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 12)

# Display results
plt.figure(figsize=(15, 10))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(thresholded, cmap='gray')
plt.title('Processed Image')
plt.axis('off')
plt.show()
