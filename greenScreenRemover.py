import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

video = cv2.VideoCapture("v.mp4")
image = cv2.imread('bbg.jpg')

def update_values(event=None):  # Add an event parameter with a default value
    l_green[0] = l_slider.get()
    l_green[1] = l_slider2.get()
    l_green[2] = l_slider3.get()
    u_green[0] = u_slider.get()
    u_green[1] = u_slider2.get()
    u_green[2] = u_slider3.get()

def process_frame():
    ret, frame = video.read()

    if not ret:
        # If no frame is read, break the loop
        return

    frame = cv2.resize(frame, (640, 480))
    image_resized = cv2.resize(image, (frame.shape[1], frame.shape[0]))

    # Create a mask to identify the green screen area
    mask = cv2.inRange(frame, l_green, u_green)

    # Apply bitwise operations to extract the foreground (green screen)
    foreground = cv2.bitwise_and(frame, frame, mask=mask)

    # Resize the background image to match the size of the foreground
    background = image_resized.copy()

    # Perform the bitwise OR operation to combine foreground and background
    result = cv2.bitwise_or(foreground, background)

    # Replace the green screen with the background image
    result = np.where(result == 0, background, result)

    cv2.imshow('video', frame)
    cv2.imshow('mask', result)

    # Call the process_frame function again after 25 milliseconds
    window.after(25, process_frame)

window = tk.Tk()
window.title("Color Controls")

l_green = np.array([0, 0, 100], dtype=np.uint8)
u_green = np.array([200, 200, 255], dtype=np.uint8)

l_label = ttk.Label(window, text="Lower Green")
l_label.grid(row=0, column=0, padx=10, pady=5)
l_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, length=200, command=update_values)
l_slider.set(l_green[0])
l_slider.grid(row=0, column=1, padx=10, pady=5)
l_slider2 = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, length=200, command=update_values)
l_slider2.set(l_green[1])
l_slider2.grid(row=0, column=2, padx=10, pady=5)
l_slider3 = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, length=200, command=update_values)
l_slider3.set(l_green[2])
l_slider3.grid(row=0, column=3, padx=10, pady=5)

u_label = ttk.Label(window, text="Upper Green")
u_label.grid(row=1, column=0, padx=10, pady=5)
u_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, length=200, command=update_values)
u_slider.set(u_green[0])
u_slider.grid(row=1, column=1, padx=10, pady=5)
u_slider2 = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, length=200, command=update_values)
u_slider2.set(u_green[1])
u_slider2.grid(row=1, column=2, padx=10, pady=5)
u_slider3 = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, length=200, command=update_values)
u_slider3.set(u_green[2])
u_slider3.grid(row=1, column=3, padx=10, pady=5)

process_frame()

window.mainloop()

video.release()
cv2.destroyAllWindows()
