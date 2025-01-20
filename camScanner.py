import cv2
import requests
import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# Load image from URL
url = ''
response = requests.get(url)
image = Image.open(BytesIO(response.content))
image = np.array(image)

# Convert to grayscale and detect edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 200)

# Find and sort contours
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

# Detect the outline of the paper
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    if len(approx) == 4:
        paper = approx
        break

# Draw contour and reshape
cv2.drawContours(image, [paper], -1, (0, 255, 0), 2)
paper_points = np.reshape(paper, (4, 2))

# Perspective transformation
h, w, _ = image.shape
src_points = np.float32(paper_points)
dst_points = np.float32([[0, 0], [0, h], [w, h], [w, 0]])
matrix = cv2.getPerspectiveTransform(src_points, dst_points)
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
