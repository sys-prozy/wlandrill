import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def play_gif():
    try:
        # Load the GIF from the provided URL
        response = requests.get('https://raw.githubusercontent.com/sys-prozy/wlandrill/main/imgs/wip.gif')
        img_data = response.content
        gif = Image.open(BytesIO(img_data))

        # Create a list to store each frame of the GIF
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(gif.copy()))
                gif.seek(len(frames))  # Go to the next frame
        except EOFError:
            pass  # End of the GIF

        # Function to update the frame
        def update_frame(index):
            frame = frames[index]
            gif_label.config(image=frame)
            root.after(100, update_frame, (index + 1) % len(frames))  # 100 ms delay for the next frame

        update_frame(0)  # Start the GIF animation
    except Exception as e:
        print("Failed to load GIF:", e)

root = tk.Tk()
root.title("wlan drill")

# Create a label for the text
text_label = tk.Label(root, text="wip, im a lil lazy", font=("Helvetica", 18))
text_label.pack()

# Create a label to display the GIF
gif_label = tk.Label(root)
gif_label.pack()

play_gif()

root.mainloop()
