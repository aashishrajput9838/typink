# Typink - Auto Typing Tool

A simple program that automatically types text at the current cursor position, featuring a modern UI built with CustomTkinter.

## Features

-   **Auto-Typing**: Types text at the current cursor position.
-   **Customizable Speed**: Adjust the typing speed (delay between characters).
-   **Modern UI**: Beautiful and responsive user interface with CustomTkinter.
-   **Indentation Support**: Preserves indentation and line breaks when typing.

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
3.  Adjust the typing speed using the slider (in milliseconds).
4.  Click the "Start Typing" button.
5.  You will have 5 seconds to switch to your target application (e.g., a text editor, IDE, or browser) and place your cursor where you want the text to be typed.
6.  To stop typing at any time, click the "Stop Typing" button.

## Customization

-   To change the default text to be typed, modify the `text_input` content in `main.py`.
-   To change the default typing speed, adjust the `delay_slider.set()` value in `main.py`.

## Note

This program uses `pyautogui` for simulating keyboard presses, which requires accessibility permissions on some operating systems (e.g., macOS). 