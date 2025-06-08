import customtkinter as ctk
import pyautogui
import time

class TypinkApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Typink - Auto Typing Tool")
        self.geometry("700x500")
        self.resizable(False, False)

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)

        # Text input field
        self.text_label = ctk.CTkLabel(self, text="Text to Type:")
        self.text_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        self.text_input = ctk.CTkTextbox(self, width=600, height=200)
        self.text_input.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="nsew")

        # Typing speed slider
        self.delay_label = ctk.CTkLabel(self, text="Typing Speed (ms):")
        self.delay_label.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")

        self.delay_slider = ctk.CTkSlider(self, from_=50, to=500, number_of_steps=45, command=self.update_delay_label)
        self.delay_slider.set(100) # Default delay
        self.delay_slider.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")
        
        self.delay_value_label = ctk.CTkLabel(self, text=f"{int(self.delay_slider.get())} ms")
        self.delay_value_label.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="e")

        # Start and Stop buttons
        self.start_button = ctk.CTkButton(self, text="Start Typing", command=self.start_typing)
        self.start_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        self.stop_button = ctk.CTkButton(self, text="Stop Typing", command=self.stop_typing, state="disabled")
        self.stop_button.grid(row=4, column=0, padx=20, pady=10, sticky="e")

        self.is_typing = False

    def update_delay_label(self, value):
        self.delay_value_label.configure(text=f"{int(value)} ms")

    def start_typing(self):
        self.is_typing = True
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        
        text_to_type = self.text_input.get("1.0", "end-1c") # Get all text from textbox
        delay = self.delay_slider.get() / 1000.0 # Convert ms to seconds

        # Give user time to switch to the target application
        print("Auto-typing will start in 5 seconds...")
        print("Please place your cursor where you want the text to be typed.")
        time.sleep(5)
        print("Starting to type...")

        for char in text_to_type:
            if not self.is_typing:
                break
            pyautogui.write(char)
            time.sleep(delay)
        
        print("Finished typing!")
        self.stop_typing()

    def stop_typing(self):
        self.is_typing = False
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

if __name__ == "__main__":
    ctk.set_appearance_mode("System") # Set theme to system default
    ctk.set_default_color_theme("blue") # Set color theme
    app = TypinkApp()
    app.mainloop() 