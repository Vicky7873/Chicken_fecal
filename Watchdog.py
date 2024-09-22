import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PipelineTriggerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"{event.src_path} has been modified. Running pipeline...")
            subprocess.run(["python", "main.py"], check=True)

if __name__ == "__main__":
    path = "."  # Monitor current directory and subdirectories
    event_handler = PipelineTriggerHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    print(f"Monitoring {path} for changes in Python files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
