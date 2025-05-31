# 📂 File Organizer

A user-friendly desktop application built with **Python** and **customtkinter** to help you organize your files into folders based on categories and optional date grouping. Ideal for cleaning up your Downloads folder or any cluttered directory.

---

## 🚀 Features

-  **Preview Before Organizing**: Instantly view how your files will be organized before making any changes.
-  **Date-Based Grouping**:
  - Organize files into folders by **daily**, **weekly**, or **monthly** modification date.
-  **Category Detection**:
  -  Classifies files into types like `documents`, `images`, `videos`, `audio`, `scripts`, `programs`, `design`, etc. based on their extension.
-  **Custom File Type Selection**:
  - Select any specific categories you want to organize and put the rest into others.
-  **Skip Empty Folders**:
  - Prevents the creation of unnecessary folders.
-  **User-Friendly GUI** using `customtkinter`:
  - Built-in directory selection.
  - Toggle and select date-based modes and categories with ease.
  - Easy preview and start buttons.

---



## 📁 Project Structure

#### ├── organizer.py # Backend logic for organizing files
#### ├── gui.py (main file) # CustomTkinter GUI interface

> Note: `gui.py` is the main file to run the application.

---

## 🛠️ How It Works

### 🧠 organizer.py
This module contains the logic for:
- Categorizing files based on extensions.
- Creating folders by file category and date.
- Previewing the structure before organizing.
- Moving files to new locations safely.

The `clean` class supports:
- Setting the main directory to clean.
- Defining file categories.
- Customizable organization with or without date grouping.

### 🎨 gui.py
An intuitive GUI built with `customtkinter` that enables:
- Folder selection through a file dialog.
- Toggle date-based grouping.
- Select desired file categories via checkboxes.
- Live preview of organization output.
- Button to start the organization process with confirmation dialog.

---



---

## This project is a great demonstration of:
- GUI development with customtkinter
- Object-Oriented Programming
- File system operations (os, shutil, datetime)
- Modular Python design
