from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music/<path:filename>')
def music(filename):
    return send_from_directory(os.path.join(BASE, 'music'), filename)

@app.route('/photos/<path:filename>')
def photos(filename):
    return send_from_directory(os.path.join(BASE, 'photos'), filename)

@app.route('/api/music-list')
def music_list():
    music_dir = os.path.join(BASE, 'music')
    files = []
    if os.path.exists(music_dir):
        for f in sorted(os.listdir(music_dir)):
            if f.lower().endswith(('.mp3', '.ogg', '.wav')):
                files.append(f)
    return jsonify({'files': files})

@app.route('/api/photo-list')
def photo_list():
    photo_dir = os.path.join(BASE, 'photos')
    files = []
    if os.path.exists(photo_dir):
        for f in sorted(os.listdir(photo_dir)):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                files.append(f)
    return jsonify({'files': files})

if __name__ == '__main__':
    app.run(debug=True)
