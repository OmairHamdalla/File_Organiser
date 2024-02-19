from datetime import datetime 
import os

class clean():
    def __init__(self):
        self.date = datetime.now().strftime("%d-%m-%Y")
        self.file_categories = {
        'documents': ['.doc', '.docx', '.pdf', '.txt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        }
    

    def createFolder(self,name):
        new_directory = os.path.join(self.directory, name)
        os.makedirs(new_directory, exist_ok=True)


    def categoriesFolders(self):
        for category in self.file_categories:
            self.createFolder(category)

