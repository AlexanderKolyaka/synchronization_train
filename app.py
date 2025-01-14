from flask import Flask, render_template
import video_processing

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    video_processing.release_video()
    app.run(debug=True)