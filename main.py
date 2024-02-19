from datetime import datetime 
import os
import shutil

class clean():
    def __init__(self):
        self.date = datetime.now().strftime("%d-%m-%Y")
        self.file_categories = {
        'documents': ['.doc', '.docx', '.pdf', '.txt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        }

    def setDirectory(self,directory_path):
        self.main_path = directory_path
        self.to_directory = os.path.join(directory_path, self.date)
        


    def organize_files(self):
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


    def createFolder(self,name):
        new_directory = os.path.join(self.directory, name)
        os.makedirs(new_directory, exist_ok=True)


    def createsFolders(self):
        for category in self.file_categories:
            self.createFolder(category)
        self.createFolder(self.to_directory)

