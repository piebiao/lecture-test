import tkinter as tk
import requests
import json

def fetch_joke():
    f = r"https://api.chucknorris.io/jokes/random"
    data = requests.get(f)
    tt = json.loads(data.text)
    joke_label.config(text=tt["value"])

# Create the main window
root = tk.Tk()
root.title("Chuck Norris Joke Fetcher")

# Create a label to display the joke
joke_label = tk.Label(root, text="Click the button to get a Chuck Norris joke", wraplength=300)
joke_label.pack(pady=20)

# Create a button to fetch the joke
joke_button = tk.Button(root, text="Fetch Joke", command=fetch_joke)
joke_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()