# Import necessary libraries
import tkinter as tk  # For creating the GUI window
from tkinter import scrolledtext, messagebox  # Additional GUI elements
import requests  # To make HTTP requests to the NewsAPI

# Function to fetch and display the latest news
def get_latest_news():
    """
    Fetch the latest news headlines from the NewsAPI and display them
    in the scrolled text widget with titles highlighted in a different color.
    """
    api_key = "ee8c8310eb654e559f879e1141a77063"  # Replace with your valid NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        # Send a GET request to the NewsAPI
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request failed
        data = response.json()  # Parse the response JSON

        if data["status"] == "ok":
            articles = data["articles"]
            news_display.delete(1.0, tk.END)  # Clear previous news content

            # Loop through the articles and display the top 10
            for article in articles[:10]:
                title = article.get("title", "No title")
                description = article.get("description", "No description")

                # Insert the title with a custom tag
                news_display.insert(tk.END, f"Title: {title}\n", "title")
                # Insert the description in the default style
                news_display.insert(tk.END, f"Description: {description}\n\n")
        else:
            messagebox.showerror("Error", "Failed to fetch news!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("Latest News")
root.geometry("600x400")

# Create a button for fetching the latest news
fetch_news_btn = tk.Button(
    root, text="Get Latest News", command=get_latest_news, bg="blue", fg="white"
)
fetch_news_btn.pack(pady=10)

# Create a scrolled text widget to display the fetched news
news_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
news_display.pack(pady=10)

# Configure a tag to highlight the title with a specific color
news_display.tag_configure("title", foreground="blue", font=("Helvetica", 12, "bold"))

# Start the GUI event loop
root.mainloop()
