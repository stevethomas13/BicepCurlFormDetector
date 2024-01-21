from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import gzip
import cv2
import threading

# Create your views here.

@gzip.gzip_page
def home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(came, content_type="multipart/x-mixed-replace;boundary=frame"))
    except:
        pass
    return render(request, 'main/home.html')

def index(request):
    button_clicked = False
    return render( request, "main/index.html")

def form(request):
    return render( request, "main/form.html" )


def onboarding(request):
    return render( request, "main/onboarding.html" )

def detect(request):
    return render( request, "main/detect.html" )


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.reelase()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    
    def update():
        while True:
            (self.grabbed, self.frame) = self.video.read()
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')