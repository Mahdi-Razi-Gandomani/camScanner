# Document Scanning and Preprocessing

This project demonstrates how to scan and preprocess a document image using OpenCV. The script detects the edges of a document, performs perspective transformation to correct the document's orientation, and applies adaptive thresholding to enhance the text.

---

## Features

- **Edge Detection**:
  - Uses the Canny edge detector to identify the edges of the document.

- **Contour Detection**:
  - Finds and sorts contours to detect the outline of the document.

- **Perspective Transformation**:
  - Corrects the document's orientation by transforming it to a top-down view.

- **Adaptive Thresholding**:
  - Enhances the document's text using adaptive thresholding.

- **Visualization**:
  - Displays the original and processed images side by side.

---

## Requirements

To run this code, you need the following Python libraries:

- `opencv-python`
- `numpy`
- `matplotlib`
- `Pillow`
- `requests`
