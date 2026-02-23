from flask import Flask, render_template
import os, json

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))

def scan_static(subfolder, exts):
    d = os.path.join(BASE, 'static', subfolder)
    if not os.path.exists(d):
        return []
    return sorted([
        f for f in os.listdir(d)
        if os.path.splitext(f)[1].lower() in exts
    ])

@app.route('/')
def index():
    music  = scan_static('music',  {'.mp3','.ogg','.wav'})
    photos = scan_static('photos', {'.jpg','.jpeg','.png','.webp'})
    return render_template('index.html',
        music_files=json.dumps(music),
        photo_files=json.dumps(photos))

if __name__ == '__main__':
    app.run(debug=True)
