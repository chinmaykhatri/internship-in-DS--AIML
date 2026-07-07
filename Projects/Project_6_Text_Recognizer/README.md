# 👁️ Project 6: Optical Character Recognition (OCR) Engine

<p align="left">
  <img src="https://img.shields.io/badge/AI-Computer%20Vision-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Engine-Tesseract%20OCR-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Library-OpenCV-red?style=for-the-badge" />
</p>

## 📋 Executive Overview
The **Optical Character Recognition (OCR) Engine** is an automated computer vision application designed to digitize physical documents, receipts, and natural scene text. Combining **OpenCV** image pre-processing pipelines with **Google's Tesseract OCR engine**, this tool extracts machine-readable text from noisy, skewed, or low-contrast images with high accuracy.

---

## 🗂️ Directory Architecture
```
Project_6_Text_Recognizer/
├── ocr_engine.py              # Main OCR processing pipeline script
├── sample_images/             # Test documents, receipts, and signs
├── output_texts/              # Extracted digital text files (.txt)
├── requirements.txt           # Python dependency list
└── README.md                  # Project documentation
```

---

## ⚙️ Computer Vision Pipeline (OpenCV)
To maximize Tesseract's character recognition accuracy, images undergo a 4-step preprocessing enhancement pipeline:
1. **Grayscale Conversion**: Eliminates color channel noise ($RGB ightarrow Gray$).
2. **Gaussian Blurring**: Smoothens high-frequency background artifacts.
3. **Adaptive Thresholding (Otsu's Binarization)**: Converts grayscale images to binary black-and-white foregrounds even under uneven lighting conditions.
4. **Morphological Transformations**: Applies dilation and erosion to connect broken character strokes and remove speckles.

---

## 💻 How to Run Locally

### 1. Install System Prerequisites (Tesseract OCR)
* **Windows**: Download and install from [UBMannheim Tesseract Installer](https://github.com/UB-Mannheim/tesseract/wiki). Add `C:\Program Files\Tesseract-OCR` to your system PATH.
* **Linux / Ubuntu**: `sudo apt-get install tesseract-ocr`
* **macOS**: `brew install tesseract`

### 2. Install Python Packages
```bash
pip install opencv-python pytesseract pillow numpy matplotlib
```

### 3. Run the OCR Extractor
```bash
python ocr_engine.py --image sample_images/invoice_sample.jpg --output output_texts/result.txt
```
