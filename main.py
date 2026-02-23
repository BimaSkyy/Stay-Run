from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music/<path:filename>')
def music(filename):
    return send_from_directory('music', filename)

@app.route('/photos/<path:filename>')
def photos(filename):
    return send_from_directory('photos', filename)

@app.route('/api/music-list')
def music_list():
    music_dir = os.path.join(os.path.dirname(__file__), 'music')
    files = []
    if os.path.exists(music_dir):
        for f in os.listdir(music_dir):
            if f.lower().endswith(('.mp3', '.ogg', '.wav')):
                files.append(f)
    return jsonify({'files': files})

@app.route('/api/photo-list')
def photo_list():
    photo_dir = os.path.join(os.path.dirname(__file__), 'photos')
    files = []
    if os.path.exists(photo_dir):
        for f in os.listdir(photo_dir):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                files.append(f)
    return jsonify({'files': files})

if __name__ == '__main__':
    app.run(debug=True)