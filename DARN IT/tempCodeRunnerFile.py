import sys
import cv2
import pytesseract
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QInputDialog
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from joblib import load
from PyQt5.QtGui import QImage
class ImageUploader(QWidget):
    def __init__(self):
        super().__init__()
        # Set window properties
        self.setWindowTitle('Image Uploader')
        self.setGeometry(200, 200, 500, 600)
        # Create UI elements
        self.image_label = QLabel('No Image Selected')
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFont(QFont('Arial', 16))
        self.upload_button = QPushButton('Upload Image')
        self.upload_button.setFont(QFont('Arial', 14))
        self.upload_button.clicked.connect(self.show_file_dialog)
        self.process_button = QPushButton('Process Image')
        self.process_button.setFont(QFont('Arial', 14))
        self.process_button.clicked.connect(self.process_image)
        self.category_label = QLabel()
        self.category_label.setFont(QFont('Arial', 14))
        self.text_label = QLabel()
        self.text_label.setWordWrap(True)
        self.text_label.setFont(QFont('Arial', 18, weight=QFont.Bold)) # larger font for extracted text
        self.select_area_button = QPushButton('Select Area')
        self.select_area_button.setFont(QFont('Arial', 14))
        self.select_area_button.clicked.connect(self.select_area)
        self.text_input_button = QPushButton('Input Text')
        self.text_input_button.setFont(QFont('Arial', 14))
        self.text_input_button.clicked.connect(self.input_text)
        self.process_text_button = QPushButton('Process Text')
        self.process_text_button.setFont(QFont('Arial', 14))
        self.process_text_button.clicked.connect(self.process_text)
        # Create layout and add UI elements
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.process_button)
        layout.addWidget(self.category_label)
        layout.addWidget(self.text_label)
        layout.addWidget(self.select_area_button)
        layout.addWidget(self.text_input_button)
        layout.addWidget(self.process_text_button)
        # Set the layout for the window
        self.setLayout(layout)

    def input_text(self):
     text, ok = QInputDialog.getText(self, 'Input Text', 'Enter text:')
     if ok:
        self.entered_text = text
        self.text_label.setText(f"Entered Text: {text}")
        self.image_label.setText('') # clear the image label if there was any image previously selected)
    def show_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image files (*.png *.jpg *.jpeg)')
        if file_name:
            self.image_file = file_name
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(QSize(400, 400), Qt.KeepAspectRatio))
            self.image_label.setMinimumSize(1, 1)
    def select_area(self):
     if not hasattr(self, 'image_file'):
        return
     img = cv2.imread(self.image_file)
     while True:
        x, y, w, h = cv2.selectROI('Select Area', img, fromCenter=False, showCrosshair=True)
        if w and h:
            self.selected_img = img[y:y+h, x:x+w]
            pixmap = QPixmap.fromImage(QImage(self.selected_img.tobytes(), self.selected_img.shape[1], self.selected_img.shape[0], QImage.Format_RGB888))
            self.image_label.setPixmap(pixmap.scaled(QSize(400, 400), Qt.KeepAspectRatio))
            self.image_label.setMinimumSize(1, 1)
            # close the crop window and update the image label
            cv2.destroyWindow('Select Area')
            self.show()
            break
        else:
            # cancel selection and reset the image label
            cv2.destroyWindow('Select Area')
            self.image_label.setPixmap(QPixmap())
            self.image_label.setText('No Image Selected')
            self.category_label.setText('')
            self.text_label.setText('')
            # exit the loop if the user presses the cross button
            if cv2.waitKey(0) == 27:
                break

    def process_image(self):
        if hasattr(self, 'image_file'):
         img = cv2.imread(self.image_file)
         if hasattr(self, 'selected_img'):
            img = self.selected_img
        else:
         return
    # Convert RGB image to BGR format
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply thresholding to preprocess the image
        threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # Perform OCR on the thresholded image or use entered text
        if hasattr(self, 'entered_text') and self.entered_text is not None:
         text = self.entered_text
        else:
         text = pytesseract.image_to_string(threshold_img)
    # Load the trained model
        text_clf = load('text_classifier.joblib')
    # Use the model to predict the category of the input text
        predicted_category = text_clf.predict([text])[0]
        self.category_label.setText(f"Predicted Category: {predicted_category}")
        self.text_label.setText(f"Entered Text: {text}")
        
    def process_text(self):
        if not hasattr(self, 'entered_text') or self.entered_text is None:
            return
        # Load the trained modelc
        text_clf = load('text_classifier.joblib')
        # Use the model to predict the category of the input text
        predicted_category = text_clf.predict([self.entered_text])[0]
        self.category_label.setText(f"Predicted Category: {predicted_category}")
        self.text_label.setText(self.entered_text)
if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)
    # Create the window instance
    window = ImageUploader()
    # Set font size for extracted text label
    font = QFont('Arial', 14)
    window.text_label.setFont(font)
    # Set style sheet to make the window more attractive
    style_sheet = """
        QWidget {
            background-color: #F5F5F5;
            border: 2px solid #BEBEBE;
            border-radius: 10px;
        }
        QPushButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #3E8E41;
            cursor: pointer;
        }
        QLabel {
            font-size: 16px;
            font-weight: bold;
        }
    """
    window.setStyleSheet(style_sheet)
    # Show the window
    window.show()
    # Run the event loop
    ret = app.exec_()
    print(type(ret), ret)
    sys.exit(ret)

