import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui
import numpy as np
import cv2

class DinoBot:
    def __init__(self, master):
        self.master = master
        self.master.title("🦖 T-Rex Game Bot by Andhika")
        self.master.geometry("320x250")
        self.running = False

        self.label = tk.Label(master, text="Klik Start untuk jalankan bot.")
        self.label.pack(pady=10)

        # Tambah slider sensitivitas
        self.sens_label = tk.Label(master, text="Sensitivitas Deteksi:")
        self.sens_label.pack()

        self.threshold = tk.IntVar(value=600)
        self.slider = tk.Scale(master, from_=100, to=1500, orient="horizontal", variable=self.threshold)
        self.slider.pack()

        self.start_button = tk.Button(master, text="Start Bot", command=self.start_bot)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop Bot", command=self.stop_bot, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Keluar", command=self.exit_program)
        self.exit_button.pack(pady=10)

    def start_bot(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.run_bot).start()

    def stop_bot(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def exit_program(self):
        self.running = False
        self.master.destroy()

    def run_bot(self):
        time.sleep(2)  # Waktu untuk buka game
        x, y, w, h = 340, 390, 100, 30  # Area deteksi

        while self.running:
            image = pyautogui.screenshot(region=(x, y, w, h))
            image_np = np.array(image)
            gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
            count = cv2.countNonZero(thresh)

            # Ambil nilai threshold dari slider
            current_threshold = self.threshold.get()
