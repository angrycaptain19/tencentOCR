from flask import Flask,request,jsonify
import generalOCR
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/OCR/images',methods=["POST"])
def get_image():
    if request.method=='POST':
        file = request.files.get('images')

        if file is None:
            return 'no file'

        fileName = file.filename
        image_path = os.path.join('static/upload_images', fileName)
        file.save(image_path)

        msg = generalOCR.postToOCR(image_path)
        print(msg)
        return jsonify(msg)



if __name__ == '__main__':
    app.run()
