from flask import Flask, render_template, request
from fact_check import fact_check_text, fact_check_image
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Home route with options for text or photo fact-checking
@app.route('/')
def home():
    return render_template('dashboard.html')

# Text fact-checking route
@app.route('/text_check', methods=['GET', 'POST'])
def text_check():
    if request.method == 'POST':
        claim = request.form['claim']
        result = fact_check_text(claim)
        print("Text Check Route Result:", result)  # Debugging: Verify result
        return render_template('result.html', claim=claim, result=result)
    return render_template('text_check.html')


# Photo fact-checking route
@app.route('/photo_check', methods=['GET', 'POST'])
def photo_check():
    if request.method == 'POST':
        image = request.files['image']
        image.save("temp_image.jpg")
        result = fact_check_image("temp_image.jpg")
        os.remove("temp_image.jpg")
        print("Photo Fact-Check Result:", result)  # Debugging: Check result content
        return render_template('result.html', claim="Photo OCR Text", result=result)
    return render_template('photo_check.html')

if __name__ == '__main__':
    #app.run(host=' 192.168.1.49', port=5000, debug=True)
    app.run(debug=True)
