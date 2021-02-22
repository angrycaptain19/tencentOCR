import base64
import os.path

def convertToBase64(image_path):
    with open(image_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        return s



