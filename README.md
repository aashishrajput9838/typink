<div align="center">
  <img src="assets/images/Typink%20logo.png" alt="Typink Logo" width="200"/>
  <h1>Typink</h1>
  <p><strong>A modern, elegant auto-typing tool built with CustomTkinter</strong></p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/CustomTkinter-UI-green?style=for-the-badge" alt="CustomTkinter" />
    <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Platform" />
  </p>
</div>

---

## ⚡ Overview
**Typink** is a simple yet powerful desktop application designed to automatically type text at your current cursor position. Whether you're filling out repetitive forms, testing inputs, or writing boilerplate code, Typink automates the process while maintaining a beautiful and responsive user interface.

## ✨ Key Features
- 🚀 **Auto-Typing**: Seamlessly types any block of text precisely where your cursor is placed.
- 🎛️ **Precision Speed Control**: Adjust the typing delay with **1ms increments** via slider or arrow keys.
- ⏸️ **Smart Pause & Resume**: Stop at any time and resume effortlessly. Includes a **5-second countdown** so you can perfectly reposition your cursor.
- 🪟 **Always-on-Top Floating Widget**: A compact, draggable control window with adjustable transparency (1% - 100%) that stays above other apps.
- 🎨 **Modern Aesthetics**: A sleek, dark-mode ready interface powered by CustomTkinter.
- 📝 **Formatting Preserved**: Accurately maintains all your original indentation and line breaks.

## 🛠️ Installation

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/aashishrajput9838/typink.git
   cd typink
   ```
2. **Install dependencies:**
   ```bash
   pip install customtkinter pyautogui
   ```
3. **Run Typink:**
   ```bash
   python main.py
   ```

## 🎮 How to Use
1. **Prepare Text:** Enter or paste the content you want to type into the main text box.
2. **Set Speed:** Adjust the typing speed (delay between keystrokes in ms). Use the slider or your keyboard's `←` / `→` arrows for precise tuning.
3. **Start:** Click **"Start Typing"**. You will have 5 seconds to switch to your target application and click where you want the text to appear.
4. **Float Mode:** Click **"Float"** to spawn the transparent, always-on-top mini controller.
5. **Control Flow:** Use the Pause/Resume and Stop buttons from either the main app or the floating widget as needed.

## 📦 Building an Executable
Want to run Typink without Python? You can easily compile it into a standalone `.exe` file using PyInstaller:

```bash
pyinstaller --onefile --windowed --name Typink main.py
```
> The compiled executable will be located in the newly created `dist/` folder.

## ⚠️ Important Note
Typink utilizes `pyautogui` to simulate keyboard inputs. Depending on your operating system (especially macOS), you may need to grant **accessibility permissions** to your terminal or IDE for the automation to work properly.

---
<div align="center">
  <p>Built with ❤️ by <a href="https://github.com/aashishrajput9838">Aspirinexar</a></p>
  <p>&copy; 2024 Aspirinexar. All rights reserved.</p>
</div>
