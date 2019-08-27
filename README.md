# Object-Detection_OCR
Vehicle Number Plate detection 
Identify the license place in the image and do an OCR to extract the characters from the detected license plate

The project developed using TensorFlow to detect the License Plate from a car and 
uses the Tesseract Engine to recognize the charactes from the detected plate.

Python Packages Needed
Tensorflow
openCV
pytesseract
labelImg

You have to object detection model, you need to import object detection model from https://github.com/tensorflow/models
You can either make a clone or you can download and extract it. Further Protobuf is required in order to make some files
so use the command protoc object_detection/protos/*.proto --python_out=.

