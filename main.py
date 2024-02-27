from customtkinter import *
from CTkMessagebox import CTkMessagebox
import organizer 

class App(CTk):

    def __init__(self):
        super().__init__()
        self.Build()
        self.printInfo()
        self.cleaner = organizer.clean()
#     # label
#     self.label = ttk.Label(self, text='Hello, Tkinter!')
#     self.label.pack()
#     # button

    
    def Build(self):
        self.title('Organizer App')
        self.geometry('600x600')
        self.geometry(f"+{660}+{240}")

        self.columnconfigure((1,3), weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure((1,2,4,7,8) ,weight=1)
        self.rowconfigure((3,5,6) ,weight=1)

        self.text = CTkLabel(self, text="Hello").grid(row=3,column = 2)
        self.download_button = CTkButton(self, text='Downloads', command = self.download_fun).grid(row=3,column=2)
        self.close_button = CTkButton(self, text='Exit', command = self.close_fun).grid(row=5,column=2)


    def download_fun(self):
        msg = CTkMessagebox(title='Downloads', message='This will clean the downloads folder,\nAre you sure?',icon='check',
                            options=["Yes","No"])
        if msg.get() == "Yes":
            # self.cleaner.setDirectory(self.cleaner.downloads_path)
            self.cleaner.start(r'C:\Users\o2m0a\Desktop\Organiser\test - Copy (2)')

    def close_fun(self):
        msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                            icon="warning",  options=["Yes","No"])
        response = msg.get()
        
        if response=="Yes":
            self.destroy()       
        else:
            print("Click 'Yes' to exit!")

    def printInfo(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        print("Screen Width:", screen_width)
        print("Screen Height:", screen_height)

        

class newApp(App):
    def __init__(self):
        super().__init__()
        print("hello")
        

    



if __name__ == "__main__":
  app = App()
  app.mainloop()
 