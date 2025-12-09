# 🛡️ Shield: OCR & PII Redaction Pipeline

> **Automated privacy protection for handwritten documents.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv&logoColor=white)
![EasyOCR](https://img.shields.io/badge/EasyOCR-Handwriting%20Recognition-yellow?style=for-the-badge)
![Spacy](https://img.shields.io/badge/SpaCy-NLP-red?style=for-the-badge&logo=spacy&logoColor=white)

---

## 📖 Overview

**Shield** is a robust pipeline designed to digitize and sanitize handwritten medical documents. In an era where data privacy is paramount, this tool automates the extraction of text from raw images and intelligently identifies and redacts Personally Identifiable Information (PII) such as names, dates, and phone numbers.

It bridges the gap between physical paper trails and secure digital records, ensuring compliance and privacy without manual intervention.

## ✨ Key Features

-   **🖼️ Intelligent Pre-processing**: Automatically corrects image orientation and enhances contrast to prepare noisy handwritten scans for OCR.
-   **✍️ Handwriting Recognition**: Powered by **EasyOCR**, capable of reading diverse handwriting styles with high accuracy.
-   **🕵️ Context-Aware PII Detection**: Utilizes **Microsoft Presidio** and **SpaCy** NLP models to understand context and identify sensitive entities (Names, Dates, Phones).
-   **🔒 Automatic Redaction**: Precisely maps detected entities back to image coordinates to obscure sensitive data permanently.

## 🛠️ Tech Stack

-   **Core Logic**: Python
-   **Computer Vision**: OpenCV (Image processing, Geometry)
-   **OCR Engine**: EasyOCR (Deep Learning based text recognition)
-   **NLP & NER**: Microsoft Presidio, SpaCy (Entity Recognition)
-   **Data Handling**: NumPy

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed.

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/shield-ocr-pii.git
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_lg
    ```

## 💻 Usage

Run the pipeline on any handwritten image:

```bash
python pipeline.py --input samples/your_document.jpg --output result.jpg
```

### Example

**Input Command:**
```bash
python pipeline.py --input samples/dummy.jpg
```

**Console Output:**
```text
Processing samples/dummy.jpg...
Running OCR...
Extracted Text: Patient Name: John Doe Date: 12/05/2023 Diagnosis: Common Cold Phone: 555-0199
Redacting: John
Redacting: Date: 12/05/2023
Saved redacted image to output.jpg
```


## 🔮 Future Improvements

-   [ ] **Deep Learning De-noising**: Implement GANs for cleaning heavily soiled documents.
-   [ ] **Custom NER Models**: Fine-tune SpaCy models specifically for medical forms.
-   [ ] **Layout Analysis**: Use LayoutLM to understand form structures better.
-   [ ] **API Wrapper**: Wrap the pipeline in a FastAPI service for real-time processing.

---

*Built with ❤️ by AMIT KUSHWAHA.*
