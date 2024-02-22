from datetime import datetime 
import os
import shutil

class clean():
    def __init__(self):
        self.date = datetime.now().strftime("%d-%m-%Y")
        self.file_categories = {
        'documents': ['.doc', '.docx', '.pdf', '.txt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'videos' : ['.mp4', '.mov','.avi'],
        'python' : ['.py' , '.ipynb'],
        'powerpoint' : ['.pptx', '.pptm', '.ppt'],
        'compressed' : ['.rar', '.zip'],
        'programs' : ['.exe' ],
        'others':[]
        }

    def setDirectory(self,directory_path):
        self.main_path = directory_path
        self.to_directory = os.path.join(self.main_path, self.date)
        

    def organizeFiles(self):
        for filename in os.listdir(self.main_path):
            if os.path.isfile(os.path.join(self.main_path, filename)):

                _, file_extension = os.path.splitext(filename)
                file_extension = file_extension.lower()

                file_category = None
                for category, extensions in self.file_categories.items():
                    if file_extension in extensions:
                        file_category = category
                        break

                if not file_category:
                    file_category = 'others'
                    self.file_categories['others'].append(file_extension)

                if file_category:
                    source_path = os.path.join(self.main_path, filename)
                    destination_path = os.path.join(self.to_directory, file_category, filename)
                    shutil.move(source_path, destination_path)


    def createFolder(self,directory,name):
        new_directory = os.path.join(directory, name)
        os.makedirs(new_directory, exist_ok=True)

    def createsFolders(self):
        self.createFolder(self.main_path, self.date)
        for category in self.file_categories:
            self.createFolder(self.to_directory,category)
        


    def start(self,directory):
        self.setDirectory(directory)
        self.createsFolders()
        self.organizeFiles()

App = clean()
p = r'C:\Users\o2m0a\Desktop\Organiser\test - Copy (2)'
App.start(p)