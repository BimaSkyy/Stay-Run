from flask import Flask, render_template, send_from_directory
import os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__,
    template_folder=os.path.join(BASE, 'templates'),
    static_folder=os.path.join(BASE, 'static'),
    static_url_path='/static')

def scan(subfolder, exts):
    d = os.path.join(BASE, 'static', subfolder)
    if not os.path.exists(d):
        return []
    return sorted([f for f in os.listdir(d)
                   if os.path.splitext(f)[1].lower() in exts])

@app.route('/')
def index():
    music  = scan('music',  {'.mp3', '.ogg', '.wav'})
    photos = scan('photos', {'.jpg', '.jpeg', '.png', '.webp'})
    return render_template('index.html',
        music_files=json.dumps(music),
        photo_files=json.dumps(photos))

if __name__ == '__main__':
    app.run(debug=True)
