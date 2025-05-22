from datetime import datetime, timedelta
import os
import shutil
from pathlib import Path


class clean():
    def __init__(self):
        self.downloads_path = str(Path.home() / "Downloads")
        self.default_file_categories = {
            'documents': ['.doc', '.docx', '.pdf', '.txt', '.odt', '.rtf', '.md'],
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
            'videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'],
            'audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
            'python': ['.py', '.ipynb', '.pyc'],
            'scripts': ['.js', '.ts', '.sh', '.bat', '.ps1'],
            'spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
            'powerpoint': ['.pptx', '.pptm', '.ppt'],
            'compressed': ['.rar', '.zip', '.7z', '.tar', '.gz'],
            'programs': ['.exe', '.msi', '.apk', '.deb'],
            'databases': ['.db', '.sqlite', '.sql', '.mdb', '.accdb'],
            'design': ['.psd', '.ai', '.xd', '.fig', '.sketch'],
            'others': []
        }


    def setDirectory(self, directory_path):
        self.main_path = directory_path


    def getFileCategory(self, extension, active_categories):
        """This returns the file category based on selected active extensions."""
        for category, extensions in active_categories.items():
            if extension in extensions:
                return category
        active_categories['others'].append(extension)
        return 'others'


    def createFolder(self, directory, name):
        os.makedirs(os.path.join(directory, name), exist_ok=True)


    def getDateFolderName(self, date_mode, file_date):
        """Determines proper folder name based on the selected date mode."""
        
        if date_mode == "daily":
            return file_date.strftime("%d-%m-%Y")
        
        elif date_mode == "weekly":
            year, week, _ = file_date.isocalendar()
            return f"Week-{week}-{year}"
        
        elif date_mode == "monthly":
            return file_date.strftime("%B-%Y")
        
        elif date_mode == "last_month":
            last_month = datetime.now().replace(day=1) - timedelta(days=1)
            if file_date.month == last_month.month and file_date.year == last_month.year:
                return file_date.strftime("%B-%Y")
            return None
        
        return datetime.now().strftime("%d-%m-%Y")


    def organizeFiles(self, use_date_folders=False, date_mode="daily", selected_categories=None, skip_empty=True):
        """Main Organizing method"""
        active_categories = {
            cat: exts.copy() for cat, exts in self.default_file_categories.items()
            if selected_categories is None or cat in selected_categories
        }
        if 'others' not in active_categories:
            active_categories['others'] = []

        file_map = self.previewOrganization(use_date_folders, date_mode, selected_categories, skip_empty)
        for date_folder, categories in file_map.items():
            for category, files in categories.items():
                if skip_empty and not files:
                    continue
                base_path = os.path.join(self.main_path, date_folder, category)
                os.makedirs(base_path, exist_ok=True)
                for filename in files:
                    src = os.path.join(self.main_path, filename)
                    dst = os.path.join(base_path, filename)
                    if os.path.exists(src):
                        shutil.move(src, dst)


    def start(self, directory, use_date_folders=False, date_mode="monthly", selected_categories=None, skip_empty=True):
        self.setDirectory(directory)
        self.organizeFiles(use_date_folders, date_mode, selected_categories, skip_empty)


    def previewOrganization(self, use_date_folders=False, date_mode="monthly", selected_categories=None, skip_empty=True):
        """Return the files/folders and how they would be organized"""
        preview = {}
        active_categories = {
            cat: exts.copy() for cat, exts in self.default_file_categories.items()
            if selected_categories is None or cat in selected_categories
        }
        if 'others' not in active_categories:
            active_categories['others'] = []

        for filename in os.listdir(self.main_path):
            full_path = os.path.join(self.main_path, filename)
            if os.path.isfile(full_path):
                _, ext = os.path.splitext(filename)
                ext = ext.lower()
                category = self.getFileCategory(ext, active_categories)
                file_date = datetime.fromtimestamp(os.path.getmtime(full_path))

                if use_date_folders:
                    date_folder = self.getDateFolderName(date_mode, file_date)
                    if date_folder is None:
                        continue
                else:
                    date_folder = datetime.now().strftime("%d-%m-%Y")

                preview.setdefault(date_folder, {})
                preview[date_folder].setdefault(category, [])
                preview[date_folder][category].append(filename)

        if skip_empty: ## Always would anyway, Up for developers to change
            for date in list(preview.keys()):
                preview[date] = {cat: files for cat, files in preview[date].items() if files}
                if not preview[date]:
                    del preview[date]

        return preview
