import cv2
import numpy as np

def create_dummy_image(output_path):
    # Create a white image
    image = np.ones((500, 800, 3), dtype=np.uint8) * 255
    
    # Define text
    text_lines = [
        "Patient Name: John Doe",
        "Date: 12/05/2023",
        "Diagnosis: Common Cold",
        "Phone: 555-0199"
    ]
    
    # Add text to image (simulating handwriting with a simple font for now)
    # Hershey fonts in OpenCV look a bit like handwriting
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    y = 100
    for line in text_lines:
        cv2.putText(image, line, (50, y), font, 1.5, (0, 0, 0), 2)
        y += 60
        
    # Add some noise/tilt to simulate handwritten document
    # Rotate slightly
    center = (400, 250)
    M = cv2.getRotationMatrix2D(center, 2, 1.0)
    image = cv2.warpAffine(image, M, (800, 500), borderValue=(255, 255, 255))
    
    cv2.imwrite(output_path, image)
    print(f"Created dummy image at {output_path}")

if __name__ == "__main__":
    create_dummy_image("samples/dummy.jpg")
