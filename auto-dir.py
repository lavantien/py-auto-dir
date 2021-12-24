import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

watch_folder = "/home/savaka/Downloads"
excluded_folders = ["dump", "pics", "docs", "db", "vids"]

dump_folder = "/home/savaka/Downloads/dump"
extDump = [".zip", ".gz", ".deb"]

pics_folder = "/home/savaka/Downloads/pics"
extPics = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".tif", ".svg", ".webp"]

docs_folder = "/home/savaka/Downloads/docs"
extDocs = [".pdf", ".md", ".epub", ".mobi", ".doc", ".docx", ".txt", ".odf", ".ods", ".xls", ".xlsx", ".ppt", ".pptx", ".odp"]

db_folder = "/home/savaka/Downloads/db"
extDb = [".sql", ".csv", ".ddl", ".sqlite"]

vids_folder = "/home/savaka/Downloads/vids"
extVids = [".mp3", ".mp4", ".mov", ".wmv", ".avi", ".mvk", ".webm", ".avchd"]

os.chdir(watch_folder)

def lower_ext(path):
	base, ext = os.path.splitext(path)
	return base + ext.lower()

class Watcher(FileSystemEventHandler):
	def on_modified(self, event):
		for file in os.listdir(watch_folder):
			file = lower_ext(file)
			if not file.startswith(tuple(excluded_folders)):
				if os.path.isdir(os.path.join(watch_folder, file)) or file.endswith(tuple(extDump)):
					src = watch_folder+"/"+file
					move_to = dump_folder+"/"+file
					os.rename(src, move_to)
				elif file.endswith(tuple(extPics)):
					src = watch_folder+"/"+file
					move_to = pics_folder+"/"+file
					os.rename(src, move_to)
				elif file.endswith(tuple(extDocs)):
					src = watch_folder+"/"+file
					move_to = docs_folder+"/"+file
					os.rename(src, move_to)
				elif file.endswith(tuple(extDb)):
					src = watch_folder+"/"+file
					move_to = db_folder+"/"+file
					os.rename(src, move_to)
				elif file.endswith(tuple(extVids)):
					src = watch_folder+"/"+file
					move_to = vids_folder+"/"+file
					os.rename(src, move_to)
			print(file.title)

event_handler = Watcher()
observer = Observer()

observer.schedule(event_handler, watch_folder, recursive=True)
observer.start()

try:
	while True:
		time.sleep(60)
finally:
	observer.stop()
	observer.join()
