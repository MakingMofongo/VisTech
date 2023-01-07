
from flask import Flask, render_template, Response
from cam import VideoCamera,Bing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def sim_gen(img):
    while True:
        frame = img.draw()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame+ b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sim_feed')
def sim_feed():
    return Response(sim_gen(Bing()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)





