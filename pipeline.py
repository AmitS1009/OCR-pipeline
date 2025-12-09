import cv2
import easyocr
import numpy as np
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import spacy
import os

class OCRPipeline:
    def __init__(self):
        print("Initializing OCR Pipeline...")
        # Initialize EasyOCR reader
        self.reader = easyocr.Reader(['en'])
        
        # Initialize Presidio Analyzer and Anonymizer
        # We can use the default configuration which uses spaCy
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
        print("Pipeline Initialized.")

    def preprocess(self, image_path):
        """
        Loads image, converts to grayscale, and handles basic de-skewing if needed.
        """
        print(f"Processing {image_path}...")
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load image at {image_path}")
        
        # Convert to RGB for EasyOCR (it expects RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image, image_rgb

    def ocr(self, image_rgb):
        """
        Performs OCR on the image.
        Returns raw results from EasyOCR.
        """
        print("Running OCR...")
        # detail=1 returns bounding box, text, and confidence
        results = self.reader.readtext(image_rgb)
        return results

    def detect_pii(self, text):
        """
        Detects PII in the given text using Presidio.
        """
        results = self.analyzer.analyze(text=text, entities=[], language='en')
        return results

    def redact(self, image, ocr_results, pii_entities):
        """
        Redacts PII from the image based on OCR bounding boxes and PII detection.
        """
        # This is the tricky part: mapping PII back to bounding boxes.
        # For a simple approach, we will iterate through OCR results, 
        # check if the text in the segment contains PII, and redact the whole segment.
        # A more advanced approach would be to map character indices, but let's start simple.
        
        output_image = image.copy()
        
        for (bbox, text, prob) in ocr_results:
            # Check if this text segment contains PII
            pii_results = self.analyzer.analyze(text=text, entities=[], language='en')
            
            if pii_results:
                print(f"Redacting: {text}")
                # bbox is a list of 4 points: top-left, top-right, bottom-right, bottom-left
                top_left = tuple(map(int, bbox[0]))
                bottom_right = tuple(map(int, bbox[2]))
                
                # Draw a black rectangle
                cv2.rectangle(output_image, top_left, bottom_right, (0, 0, 0), -1)
        
        return output_image

    def run(self, image_path, output_path=None):
        try:
            original_image, image_rgb = self.preprocess(image_path)
            ocr_results = self.ocr(image_rgb)
            
            # Combine all text for a full document PII check (optional, for context)
            full_text = " ".join([res[1] for res in ocr_results])
            print(f"Extracted Text: {full_text}")
            
            # Redact
            # We pass ocr_results directly to redact to handle segment-wise redaction
            redacted_image = self.redact(original_image, ocr_results, None)
            
            if output_path:
                cv2.imwrite(output_path, redacted_image)
                print(f"Saved redacted image to {output_path}")
            
            return full_text, redacted_image
        except Exception as e:
            print(f"Error: {e}")
            return None, None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="OCR + PII Extraction Pipeline")
    parser.add_argument("--input", help="Path to input image", required=True)
    parser.add_argument("--output", help="Path to output image", default="output.jpg")
    
    args = parser.parse_args()
    
    pipeline = OCRPipeline()
    pipeline.run(args.input, args.output)
