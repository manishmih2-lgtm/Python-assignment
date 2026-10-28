import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading

def check_alarm(alarm_time):
    """Continuously checks the current time against the alarm time."""
    while True:
        # Get current time in HH:MM format
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        if current_time == alarm_time:
            # Trigger the alarm popup
            messagebox.showinfo("Alarm", "Time to Wake Up!")
            break
            
        time.sleep(1) # Wait 1 second before checking again

def start_alarm():
    """Fetches the user input and starts the alarm thread."""
    # Format the time from the input fields
    alarm_time = f"{hour_var.get().zfill(2)}:{minute_var.get().zfill(2)}"
    status_label.config(text=f"Alarm set for {alarm_time}")
    
    # Run the check_alarm function in a separate thread to keep the GUI responsive
    threading.Thread(target=check_alarm, args=(alarm_time,), daemon=True).start()

# --- GUI Setup ---
app = tk.Tk()
app.title("Alarm Clock")
app.geometry("300x200")

# Instructions
tk.Label(app, text="Set Alarm Time (24h format)", font=("Helvetica", 14)).pack(pady=10)

# Input area frame
frame = tk.Frame(app)
frame.pack()

# Variables to store user input
hour_var = tk.StringVar(value="07")
minute_var = tk.StringVar(value="30")

# Hour and Minute inputs
tk.Entry(frame, textvariable=hour_var, width=3, font=("Helvetica", 18), justify="center").pack(side=tk.LEFT, padx=5)
tk.Label(frame, text=":", font=("Helvetica", 18)).pack(side=tk.LEFT)
tk.Entry(frame, textvariable=minute_var, width=3, font=("Helvetica", 18), justify="center").pack(side=tk.LEFT, padx=5)

# Set Alarm Button
tk.Button(app, text="Set Alarm", command=start_alarm, font=("Helvetica", 12)).pack(pady=20)

# Status text at the bottom
status_label = tk.Label(app, text="")
status_label.pack()

# Start the application
if __name__ == "__main__":
    app.mainloop()