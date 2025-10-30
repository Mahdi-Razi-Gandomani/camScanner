# Document Scanning and Preprocessing

This project demonstrates how to scan and preprocess a document image using OpenCV. The script detects the edges of a document, performs perspective transformation to correct the document's orientation, and applies adaptive thresholding to enhance the text.

---

### Demo

![Original](images/output.png)

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

## Usage

1. Place your input image in the `images/` directory (default filename: `input.png`).

2. Run the script:

```bash
python document_scanner.py
```

---

## Results

After running the script, you should see two images:

- **Original Image**: The input image with the detected document contour highlighted in green.
- **Processed Image**: The warped, perspective-corrected, and thresholded output.
