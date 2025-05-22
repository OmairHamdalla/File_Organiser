from customtkinter import *
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog
import organizer


class App(CTk):
    def __init__(self):
        super().__init__()
        self.cleaner = organizer.clean()
        self.directory = ""
        self.file_categories = [
            cat for cat in self.cleaner.default_file_categories.keys() if cat != "others"
        ]
        self.selected_categories = set()
        self.date_mode_options = ["daily", "weekly", "monthly"]
        self.date_mode = "daily"
        self.use_date_folders = False
        self.skip_empty_folders = True  # Always skip empty folders (helps to not mess the folders with massive amount of empty ones)
        self.category_vars = {}

        self.build_ui()

    def build_ui(self):
        self.title("📂 Smart File Organizer")
        self.geometry("850x820+500+50")
        self.configure(fg_color="#1f1f1f")

        CTkLabel(self, text="📁 Smart File Organizer", font=("Arial", 28, "bold")).pack(pady=20)

        # Directory selection
        CTkLabel(self, text="📌 Select Folder to Organize:", font=("Arial", 16)).pack()
        self.path_entry = CTkEntry(self, width=500, placeholder_text="Choose a folder...")
        self.path_entry.pack(pady=5)
        CTkButton(self, text="Browse Folder", command=self.select_folder_fun).pack(pady=5)

        # Date toggle & mode
        CTkLabel(self, text="Date Based Grouping", font=("Arial", 16)).pack(pady=10)
        self.date_switch = CTkSwitch(
            self, text="Enable Date Folders",
            command=self.toggle_date_options
        )
        self.date_switch.pack()
        self.date_mode_dropdown = CTkOptionMenu(
            self, values=self.date_mode_options,
            command=self.set_date_mode
        )
        self.date_mode_dropdown.pack(pady=5)
        self.date_mode_dropdown.configure(state="disabled")

        # File category checkboxes
        CTkLabel(self, text="📄 File Categories", font=("Arial", 16)).pack(pady=10)
        category_frame = CTkFrame(self)
        category_frame.pack()

        num_columns = 3
        for i, cat in enumerate(self.file_categories):
            row = i // num_columns
            col = i % num_columns
            checkbox = CTkCheckBox(
                category_frame, text=cat.capitalize(),
                command=lambda c=cat: self.toggle_category(c)
            )
            checkbox.grid(row=row, column=col, padx=20, pady=5, sticky="w")
            self.category_vars[cat] = checkbox

        # Buttons
        CTkLabel(self, text="Actions", font=("Arial", 16)).pack(pady=10)
        CTkButton(self, text='Preview Organization', command=self.preview).pack(pady=5)
        CTkButton(self, text='Start Organization', fg_color="#306839",command=self.organize_files).pack(pady=5)

        # Preview output
        CTkLabel(self, text="🧾 Organization Preview", font=("Arial", 16)).pack(pady=10)
        self.preview_output = CTkTextbox(self, width=750, height=250)
        self.preview_output.pack(pady=10)

    def toggle_date_options(self):
        self.use_date_folders = self.date_switch.get()
        if self.use_date_folders:
            self.date_mode_dropdown.configure(state="normal")
        else:
            self.date_mode_dropdown.configure(state="disabled")

    def set_date_mode(self, value):
        self.date_mode = value

    def toggle_category(self, category):
        if category in self.selected_categories:
            self.selected_categories.remove(category)
        else:
            self.selected_categories.add(category)

    def select_folder_fun(self):
        folder = filedialog.askdirectory()
        if folder:
            self.directory = folder
            self.path_entry.delete(0, 'end')
            self.path_entry.insert(0, folder)

    def preview(self):
        if not self.path_entry.get():
            CTkMessagebox(title="Error", message="Please select a folder first.", icon="cancel")
            return

        self.cleaner.setDirectory(self.path_entry.get())

        preview_data = self.cleaner.previewOrganization(
            use_date_folders=self.use_date_folders,
            date_mode=self.date_mode,
            selected_categories=list(self.selected_categories) if self.selected_categories else None,
            skip_empty=True  # Always skip empty folders
        )

        self.preview_output.delete("0.0", "end")
        for date_folder, categories in preview_data.items():
            self.preview_output.insert("end", f"\n📂 {date_folder}:\n")
            for cat, files in categories.items():
                self.preview_output.insert("end", f"   📁 {cat}:\n")
                for f in files:
                    self.preview_output.insert("end", f"      • {f}\n")

    def organize_files(self):
        if not self.path_entry.get():
            CTkMessagebox(title="Error", message="Please select a folder first.", icon="cancel")
            return

        confirm = CTkMessagebox(
            title="Confirm",
            message="Are you sure you want to organize files?",
            icon="question",
            options=["Yes", "No"]
        )
        if confirm.get() == "Yes":
            self.cleaner.start(
                directory=self.path_entry.get(),
                use_date_folders=self.use_date_folders,
                date_mode=self.date_mode,
                selected_categories=list(self.selected_categories) if self.selected_categories else None,
                skip_empty=True  # Always skip empty folders
            )
            CTkMessagebox(title="Success", message="Files have been organized!", icon="check")

if __name__ == "__main__":
    app = App()
    app.mainloop()
