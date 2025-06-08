import customtkinter as ctk
import pyautogui
import time
import threading
from datetime import datetime, timedelta
import tkinter as tk

# Configure PyAutoGUI
pyautogui.FAILSAFE = True  # Keep fail-safe enabled for safety
pyautogui.PAUSE = 0.01  # Small pause between actions

class TypinkApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Typink - Auto Typing Tool")
        self.geometry("700x550")  # Adjusted height
        self.resizable(True, True)

        # Configure grid layout for full responsiveness
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Label
        self.grid_rowconfigure(1, weight=2)  # Textbox
        self.grid_rowconfigure(2, weight=0)  # Speed label/slider
        self.grid_rowconfigure(3, weight=0)  # Slider
        self.grid_rowconfigure(4, weight=0)  # Keyboard/burst
        self.grid_rowconfigure(5, weight=0)  # Progress label
        self.grid_rowconfigure(6, weight=1)  # Progress bar
        self.grid_rowconfigure(7, weight=0)  # Buttons

        # Text input field
        self.text_label = ctk.CTkLabel(self, text="Text to Type:")
        self.text_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="ew")

        self.text_input = ctk.CTkTextbox(self, width=600, height=200)
        self.text_input.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="nsew")

        # Typing speed slider
        self.delay_label = ctk.CTkLabel(self, text="Typing Speed (ms):")
        self.delay_label.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")

        self.delay_slider = ctk.CTkSlider(self, from_=1, to=1000, number_of_steps=999, command=self.update_delay_label)
        self.delay_slider.set(50)  # Default to 50ms
        self.delay_slider.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")
        
        self.delay_value_label = ctk.CTkLabel(self, text=f"{int(self.delay_slider.get())} ms")
        self.delay_value_label.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="e")

        # Warning label for fast speeds
        self.warning_label = ctk.CTkLabel(self, text="", text_color="red")
        self.warning_label.grid(row=3, column=0, padx=20, pady=(0, 0), sticky="e")

        # Keyboard control instructions
        self.keyboard_label = ctk.CTkLabel(self, text="Use ← and → arrow keys to adjust speed (±1ms)")
        self.keyboard_label.grid(row=4, column=0, padx=20, pady=(0, 10), sticky="w")

        # Progress bar
        self.progress_label = ctk.CTkLabel(self, text="Typing Progress:")
        self.progress_label.grid(row=5, column=0, padx=20, pady=(10, 0), sticky="ew")
        
        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.grid(row=6, column=0, padx=20, pady=(0, 10), sticky="ew")
        self.progress_bar.set(0)

        # Buttons frame
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=7, column=0, padx=20, pady=10, sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1) # Added a column for the new button

        self.start_button = ctk.CTkButton(self.button_frame, text="Start Typing", command=self.start_typing)
        self.start_button.grid(row=0, column=0, padx=5, pady=0, sticky="ew")

        self.pause_button = ctk.CTkButton(self.button_frame, text="Pause", command=self.toggle_pause, state="disabled")
        self.pause_button.grid(row=0, column=1, padx=5, pady=0, sticky="ew")

        self.stop_button = ctk.CTkButton(self.button_frame, text="Stop Typing", command=self.stop_typing, state="disabled")
        self.stop_button.grid(row=0, column=2, padx=5, pady=0, sticky="ew")
        
        # New float button
        self.float_button = ctk.CTkButton(self.button_frame, text="Float", command=self.toggle_float)
        self.float_button.grid(row=0, column=3, padx=5, pady=0, sticky="ew")

        self.is_typing = False
        self.is_paused = False
        self.typing_thread = None
        self.current_position = 0
        self.float_window = None # Initialize float window to None
        
        # Bind arrow keys
        self.bind("<Left>", self.decrease_speed)
        self.bind("<Right>", self.increase_speed)

    def decrease_speed(self, event=None):
        current_value = self.delay_slider.get()
        if current_value > 1:  # Don't go below 1ms
            new_value = current_value - 1
            self.delay_slider.set(new_value)
            self.update_delay_label(new_value)

    def increase_speed(self, event=None):
        current_value = self.delay_slider.get()
        if current_value < 1000:  # Don't go above 1000ms
            new_value = current_value + 1
            self.delay_slider.set(new_value)
            self.update_delay_label(new_value)

    def update_delay_label(self, value):
        self.delay_value_label.configure(text=f"{int(value)} ms")
        if value < 5:  # 5 milliseconds
            self.warning_label.configure(text="Warning: Extreme speed!")
        elif value < 50:  # 50 milliseconds
            self.warning_label.configure(text="Warning: Very fast speed!")
        else:
            self.warning_label.configure(text="")

    def update_progress(self, current, total):
        progress = current / total
        self.progress_bar.set(progress)
        self.update_idletasks()  # Force immediate UI update

    def update_button_states(self, is_typing_active):
        state = "normal" if is_typing_active else "disabled"
        self.start_button.configure(state="disabled" if is_typing_active else "normal")
        self.pause_button.configure(state=state)
        self.stop_button.configure(state=state)

        # Update floating window buttons if it exists
        if self.float_window:
            self.float_start.configure(state="disabled" if is_typing_active else "normal")
            self.float_pause.configure(state=state)
            self.float_stop.configure(state=state)

    def start_typing(self):
        if not self.is_typing:
            text_to_type = self.text_input.get("1.0", "end-1c")
            if not text_to_type.strip():
                return
                
            self.is_typing = True
            self.is_paused = False
            self.current_position = 0
            self.update_button_states(True)
            self.progress_bar.set(0)
            
            print("Auto-typing will start in 5 seconds...")
            print("Please place your cursor where you want the text to be typed.")
            
            # Countdown with ability to cancel
            for i in range(5, 0, -1):
                if not self.is_typing:
                    print("Typing cancelled during countdown.")
                    self.stop_typing()
                    return
                print(f"Starting in {i} seconds...")
                time.sleep(1)
            
            if not self.is_typing: # Check again after countdown
                return

            print("Starting to type...")
            # Start typing in a separate thread
            self.typing_thread = threading.Thread(
                target=self.typing_process,
                args=(text_to_type, self.delay_slider.get() / 1000, len(text_to_type))
            )
            self.typing_thread.daemon = True
            self.typing_thread.start()

    def stop_typing(self):
        if self.is_typing:
            self.is_typing = False
            self.is_paused = False
            self.update_button_states(False)
            self.pause_button.configure(text="Pause") # Reset pause button text
            if self.float_window:
                self.float_pause.configure(text="Pause")
            if self.typing_thread and self.typing_thread.is_alive():
                # It's generally not safe to stop a thread directly, but we set a flag
                # The thread's loop will check is_typing and exit cleanly
                pass
            print("Typing stopped by user")
            # Force update the UI
            self.update_idletasks()

    def toggle_pause(self):
        if self.is_typing:
            if not self.is_paused:  # If we're about to pause
                self.is_paused = True
                self.pause_button.configure(text="Resume")
                if self.float_window:
                    self.float_pause.configure(text="Resume")
                print("Typing paused")
            else:  # If we're about to resume
                print("Auto-typing will resume in 5 seconds...")
                print("Please place your cursor where you want to continue typing.")
                
                # Countdown with ability to cancel
                for i in range(5, 0, -1):
                    if not self.is_typing:
                        print("Resume cancelled")
                        self.stop_typing()
                        return
                    print(f"Resuming in {i} seconds...")
                    time.sleep(1)
                
                if not self.is_typing:
                    return
                    
                self.is_paused = False
                self.pause_button.configure(text="Pause")
                if self.float_window:
                    self.float_pause.configure(text="Pause")
                print("Typing resumed")

    def typing_process(self, text_to_type, delay, total_chars):
        try:
            start_time = datetime.now()
            char_times = []  # Store time for each character
            
            for i in range(self.current_position, len(text_to_type)):
                if not self.is_typing:
                    print("Typing stopped by user")
                    return
                
                # Check for pause
                while self.is_paused and self.is_typing:
                    time.sleep(0.1)  # Small delay while paused
                    continue
                
                if not self.is_typing:
                    return
                    
                try:
                    char = text_to_type[i]
                    char_start = datetime.now()
                    pyautogui.write(char)
                    char_end = datetime.now()
                    char_time = (char_end - char_start).total_seconds() * 1000  # Convert to ms
                    char_times.append(char_time)
                    
                    # Update progress and force UI update
                    self.update_progress(i + 1, total_chars)
                    self.current_position = i + 1
                    
                    # Check if stopped before sleeping
                    if not self.is_typing:
                        return
                        
                    time.sleep(delay)
                except pyautogui.FailSafeException:
                    print("PyAutoGUI fail-safe triggered. Stopping typing.")
                    self.stop_typing()
                    return
                    
            if not self.is_typing: # Check if typing was stopped during the loop
                return
            
            end_time = datetime.now()
            total_time = (end_time - start_time).total_seconds()
            total_chars_typed = len(char_times)
            
            if total_chars_typed > 0:
                actual_speed = total_chars_typed / total_time
                avg_char_time = sum(char_times) / len(char_times)
                print(f"Actual typing speed: {actual_speed:.2f} characters per second")
                print(f"Average time per character: {avg_char_time:.2f} ms")
                print(f"Set delay: {delay*1000:.2f} ms")
                print(f"Actual delay (including typing): {avg_char_time:.2f} ms")
            
            print("Finished typing!")
            self.is_typing = False
            self.update_button_states(False)
            
        except Exception as e:
            print(f"Error during typing: {str(e)}")
            self.is_typing = False
            self.update_button_states(False)

    def toggle_float(self):
        if self.float_window is None or not self.float_window.winfo_exists():
            # Create floating window
            self.float_window = ctk.CTkToplevel(self)
            self.float_window.title("Typink Controls")
            self.float_window.geometry("250x130") # Adjusted height for transparency slider + title bar
            self.float_window.attributes('-topmost', True) # Keep on top
            # self.float_window.overrideredirect(True) # Removed to show default borders

            # Create control buttons and transparency slider frame
            float_main_frame = ctk.CTkFrame(self.float_window, fg_color="transparent")
            float_main_frame.pack(fill="both", expand=True, padx=5, pady=5)
            float_main_frame.grid_columnconfigure((0, 1, 2), weight=1)
            
            # Start button
            self.float_start = ctk.CTkButton(
                float_main_frame,
                text="Start",
                command=self.start_typing,
                font=("Helvetica", 12, "bold")
            )
            self.float_start.grid(row=0, column=0, padx=2, pady=2, sticky="ew")
            
            # Pause/Resume button
            self.float_pause = ctk.CTkButton(
                float_main_frame,
                text="Pause",
                command=self.toggle_pause,
                font=("Helvetica", 12, "bold"),
                state="disabled"
            )
            self.float_pause.grid(row=0, column=1, padx=2, pady=2, sticky="ew")
            
            # Stop button
            self.float_stop = ctk.CTkButton(
                float_main_frame,
                text="Stop",
                command=self.stop_typing,
                font=("Helvetica", 12, "bold"),
                state="disabled"
            )
            self.float_stop.grid(row=0, column=2, padx=2, pady=2, sticky="ew")
            
            # Transparency control
            self.float_transparency_label = ctk.CTkLabel(
                float_main_frame,
                text="Transparency:",
                font=("Helvetica", 10)
            )
            self.float_transparency_label.grid(row=1, column=0, padx=2, pady=(5, 0), sticky="w")
            
            self.float_transparency_slider = ctk.CTkSlider(
                float_main_frame,
                from_=1,
                to=100,
                number_of_steps=19, # 1 to 100, step 5 (1, 6, 11...96, 100)
                command=self.update_float_transparency
            )
            self.float_transparency_slider.set(90) # Default to 90% transparency
            self.float_transparency_slider.grid(row=1, column=1, columnspan=2, padx=2, pady=(5, 2), sticky="ew")
            
            # Set initial transparency
            self.update_float_transparency(self.float_transparency_slider.get())

            # Bind arrow keys to float window for transparency control
            self.float_window.bind("<Left>", lambda e: self.adjust_float_transparency(-5))
            self.float_window.bind("<Right>", lambda e: self.adjust_float_transparency(5))

            # Update main window float button text
            self.float_button.configure(text="Unfloat")
            # Update initial state of floating buttons
            self.update_button_states(self.is_typing)
        else:
            # Destroy floating window
            self.float_window.destroy()
            self.float_window = None
            self.float_button.configure(text="Float")
    
    def start_move(self, event):
        # Removed custom drag logic, OS handles title bar drag
        pass

    def on_move(self, event):
        # Removed custom drag logic, OS handles title bar drag
        pass

    def update_float_transparency(self, value):
        # Ensure value is a multiple of 5, but at least 1
        percent = max(1, round(value / 5) * 5)
        alpha_value = percent / 100.0
        if self.float_window:
            self.float_window.attributes('-alpha', alpha_value)
        self.float_transparency_label.configure(text=f"Transparency: {percent}%")

    def adjust_float_transparency(self, delta):
        current = self.float_transparency_slider.get()
        new_value = max(1, min(100, current + delta))
        self.float_transparency_slider.set(new_value)
        self.update_float_transparency(new_value) # Explicitly call to update transparency

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = TypinkApp()
    app.mainloop() 