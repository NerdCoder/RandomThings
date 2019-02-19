import os 
from pathlib import Path 

DIRECTORIES = {
	"Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
			".heif", ".psd"], 
	"Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
			".qt", ".mpg", ".mpeg", ".3gp"], 
	"Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
				"pptx", ".pdf"], 
	"Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
				".dmg", ".rar", ".xar", ".zip"], 
	"Music": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
	"Codes": [".py", ".c", ".cpp", ".xml", ".txt", ".in", ".out", ".html", ".js",
             ".css"], 
    "Applications": [".tpk", ".apk", ".exe"],
	"SHELL": [".sh"]
} 

FILE_FORMATS = {file_format: directory 
				for directory, file_formats in DIRECTORIES.items() 
				for file_format in file_formats} 

def organize():
	for entry in os.scandir(): 
		if entry.is_dir(): 
			continue 
		file_path = Path(entry) 
		file_format = file_path.suffix.lower() 
		if file_format in FILE_FORMATS: 
			directory_path = Path(FILE_FORMATS[file_format]) 
			directory_path.mkdir(exist_ok=True) 
			file_path.rename(directory_path.joinpath(file_path)) 

		for dir in os.scandir(): 
			try: 
				os.rmdir(dir) 
			except: 
				pass

if __name__ == "__main__": 
	organize()

#TODO
"""
xclip -selection clipboard -o -t TARGETS
xclip -selection clipboard -o -t text/html

[maybe] bs4 to parse data... 
make folders and download them all 
then organize.
"""