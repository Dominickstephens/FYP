import tkinter as tk
from tkinter import ttk

class MuscleActivationSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Muscle Activation Simulation")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")

        # Create a style for the UI
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
        self.style.configure("TButton", font=("Arial", 12), background="#4CAF50", foreground="white")

        # Create main frames
        self.create_widgets()

    def create_widgets(self):
        # Frame for Settings
        settings_frame = ttk.LabelFrame(self.root, text="Settings", style="TLabelframe")
        settings_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        self.setting1_label = ttk.Label(settings_frame, text="Setting 1:", style="TLabel")
        self.setting1_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.setting1_entry = ttk.Entry(settings_frame, width=20)
        self.setting1_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.setting2_label = ttk.Label(settings_frame, text="Setting 2:", style="TLabel")
        self.setting2_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.setting2_entry = ttk.Entry(settings_frame, width=20)
        self.setting2_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Frame for Simulation
        simulation_frame = ttk.LabelFrame(self.root, text="Simulation Window", style="TLabelframe")
        simulation_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.simulation_canvas = tk.Canvas(simulation_frame, width=700, height=600, bg="white")
        self.simulation_canvas.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        # Configure grid weights for resizing
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        simulation_frame.grid_rowconfigure(0, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = MuscleActivationSimulationApp(root)
    root.mainloop()
