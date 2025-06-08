


# Typink - Auto Typing Tool
<img src="assets/images/typink logo.png" alt="Typink Logo" width="200">


A simple program that automatically types text at the current cursor position, featuring a modern UI built with CustomTkinter.

## Features

-   **Auto-Typing**: Types text at the current cursor position.
-   **Customizable Speed**: Adjust the typing speed (delay between characters) with **1ms increments** using a slider or **left/right arrow keys**.
-   **Modern UI**: Beautiful and responsive user interface with CustomTkinter.
-   **Indentation Support**: Preserves indentation and line breaks when typing.
-   **Real-time Progress Bar**: Visual feedback on typing progress.
-   **Pause/Resume Functionality**:
    -   Pause typing at any point and resume from the exact position.
    -   Includes a **5-second countdown** before resuming to allow cursor repositioning.
-   **Floating Control Window**:
    -   A dedicated compact window with Start, Pause/Resume, and Stop buttons that stays **always on top of other applications**.
    -   **Adjustable Transparency**: Control the floating window's visibility from **1% to 100%** using a dedicated slider or **left/right arrow keys (5% increments)**.
    -   Features a **sleek, transparent border** (OS-native) and is **draggable by its title bar**.

## Prerequisites

-   Python 3.x

## Installation

1.  Clone this repository or download the files.
2.  Navigate to the project directory:
    ```bash
    cd Typink
    ```
3.  Install the required Python packages:
    ```bash
    pip install customtkinter pyautogui
    ```

## Usage

1.  Run the application:
    ```bash
    python main.py
    ```
2.  Enter the text you want to type into the text box.
3.  Adjust the typing speed using the slider or the **left/right arrow keys (±1ms)**.
4.  Click the "Start Typing" button.
5.  You will have 5 seconds to switch to your target application (e.g., a text editor, IDE, or browser) and place your cursor where you want the text to be typed.
6.  To **pause** typing, click the "Pause" button. To **resume** from where you left off, click the "Resume" button (a 5-second countdown will precede resumption).
7.  To stop typing at any time, click the "Stop Typing" button.
8.  Click the **"Float"** button to open the floating control window. You can drag this window by its title bar and adjust its transparency using the slider or arrow keys within that window.

## Building Executable

You can compile the application into a standalone executable (`.exe`) file using PyInstaller:

```bash
pyinstaller --onefile --windowed --name Typink main.py
```
The executable will be generated in the `dist` folder within your project directory.

## Customization

-   To change the default text to be typed, modify the `text_input` content in `main.py`.
-   To change the default typing speed, adjust the `delay_slider.set()` value in `main.py`.

## Note

This program uses `pyautogui` for simulating keyboard presses, which requires accessibility permissions on some operating systems (e.g., macOS). 

---

© 2024 Aspirinexar. All rights reserved. 
