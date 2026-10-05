import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.src_path.endswith("Class3.py"):
            print("\nFile updated. Running Class3.py...\n")
            subprocess.run(["python", "Class3.py"])


observer = Observer()
observer.schedule(MyHandler(), ".", recursive=False)
observer.start()

print("Watching Class3.py for changes...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()