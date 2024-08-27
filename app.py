import os, time
from flask import Flask
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, url_for, request, session, jsonify
from flask_session import Session
from threading import Thread

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

class ObsImageHandler(FileSystemEventHandler):
    def __init__(self):
        self.latestImg = None

    def getLatestImage(self):
        return self.latestImg
    
    def on_created(self, event):
        print("on_created called")
        if not event.is_directory and event.src_path.endswith(('.png', '.jpg', '.jpeg')):
            self.latestImg = event.src_path
            print(f"New File {event.src_path} has been loaded.")

def start_watchdog():
    ABS_PATH = 'D:\FILES\PROGRAMMING\GDSC_Photobooth\images' #C:\Users\WIndows 11\Pictures\Screenshots
    event_handler = ObsImageHandler()
    observer = Observer()
    observer.schedule(event_handler, ABS_PATH, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('stopped')
        observer.stop()
    observer.join()

@app.route('/')
def index():
    return render_template('layout.html')

if __name__ == '__main__':
    Thread(target=start_watchdog).start()
    app.run()