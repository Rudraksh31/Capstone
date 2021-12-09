from django.shortcuts import render,HttpResponse
import speech_recognition as sr
import pyaudio
r = sr.Recognizer()

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("Here are our services")
def contact(request):
    return render(request, "ContactUs.html")
    # return HttpResponse("Here are our services{}".format("jatin"))
def audio(request):
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source, timeout=3)
        try:
            text = r.recognize_google(audio)
            return HttpResponse("You said : {}".format(text))
        except:
            return HttpResponse("Sorry could not recognize what you said")