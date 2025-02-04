from pynput.keyboard import Key, Controller
import pygetwindow as gw
import time
import tkinter as tk
import threading

jumped = 0
keyboard = Controller() 
jumping = False

def StartJumping():
    global jumping, jumped, jump_duration
    try:
        jump_duration = float(duration_entry.get()) if duration_entry.get() else 120.0  # Default to 120 seconds if empty or invalid
        while jumping:
            wow_windows = gw.getWindowsWithTitle('World of Warcraft') # Change this if you want to use in another game
            if wow_windows:
                win = wow_windows[0]
                win.activate()
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                jumped += 1
                root.after(0, update_label, jumped)
                time.sleep(jump_duration)  # Sleep for the entered duration
            else:
                print("World of Warcraft window not found.")
                break
    except ValueError:
        print("Invalid jump duration. Please enter a number.")
        jumping = False
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if jumping:
            jumping = False
            print("Jumping stopped unexpectedly - total jumps:", jumped)
        root.after(0, update_label, jumped)

def update_label(count):
    jump_count_label.config(text=f"Jumped: {count}")

def start_button_clicked():
    global jumping, jumped
    jumping = True
    jumped = 0
    jump_count_label.config(text="Jumped: 0")
    print("Jumping started!")
    root.attributes('-topmost', True)
    threading.Thread(target=StartJumping, daemon=True).start()

def stop_button_clicked():
    global jumping
    jumping = False
    print("Jumping stopped - total jumps:", jumped)
    root.attributes('-topmost', False)

root = tk.Tk()
root.title("Jump Control")

# Jump Count Label
jump_count_label = tk.Label(root, text="Jumped: 0", font=("Arial", 14))
jump_count_label.pack(pady=(10, 0))

# Duration Entry
duration_entry = tk.Entry(root, width=10)
duration_entry.insert(0, "3")  # Default value in seconds
duration_entry.pack(pady=5)

duration_label = tk.Label(root, text="Jump Duration (in seconds):")
duration_label.pack()

# Start Button
start_button = tk.Button(root, 
                         text="Start", 
                         command=start_button_clicked,
                         activebackground="blue", 
                         activeforeground="white",
                         anchor="center",
                         bd=3,
                         bg="lightgray",
                         cursor="hand2",
                         disabledforeground="gray",
                         fg="black",
                         font=("Arial", 12),
                         height=2,
                         highlightbackground="black",
                         highlightcolor="green",
                         highlightthickness=2,
                         justify="center",
                         overrelief="raised",
                         padx=10,
                         pady=5,
                         width=15,
                         wraplength=100)

# Stop Button
stop_button = tk.Button(root, 
                        text="Stop", 
                        command=stop_button_clicked,
                        activebackground="red", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Arial", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="red",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)

start_button.pack(side=tk.LEFT, padx=(20, 10), pady=20)
stop_button.pack(side=tk.RIGHT, padx=(10, 20), pady=20)

root.mainloop()
