import tkinter as tk
import nltk
from textblob import TextBlob # Allows for sentiment and polarity
from newspaper import Article # Allows to extract title,author,date, summary

#nltk.download('punkt')

def summarize():

    url = utext.get('1.0', 'end').strip() # get the url into correct formate by strip/0


    article = Article(url)

    article.download()
    article.parse()

    article.nlp() 

    # Able to edit the boxes in gui
    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete('1.0','end') # clear 
    title.insert('1.0', article.title) # add the text

    author.delete('1.0','end')
    author.insert('1.0', article.authors)

    publication.delete('1.0','end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0', article.summary)

    # Sentiment on the whole article and give value if >1 postive else <1 negative else neutral
    # Check for words like good, happy, etc
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f"Polarity: {analysis.polarity}, Sentiment: {"Postive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "neutral"}")

    # Again disable the text box in gui so user cannot type into it
    title.config(state="disabled")
    author.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")

# Basic screen for GUI, with title and size
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x600")

# Name of the box
tlable = tk.Label(root, text = "Title")
tlable.pack()

# Text box size and color 
#.pack() is used to end the pack
title = tk.Text(root, height = 1, width = 140)
title.config(state = "disabled", bg = "#808080")
title.pack()

alable = tk.Label(root, text = "Author")
alable.pack()

author = tk.Text(root, height = 1, width = 140)
author.config(state = "disabled", bg = "#808080")
author.pack()

plable = tk.Label(root, text = "Publication")
plable.pack()

publication = tk.Text(root, height = 1, width = 140)
publication.config(state = "disabled", bg = "#808080")
publication.pack()

slable = tk.Label(root, text = "Summary")
slable.pack()

summary = tk.Text(root, height = 20, width = 140)
summary.config(state = "disabled", bg = "#808080")
summary.pack()

selable = tk.Label(root, text = "Sentiment Analysis")
selable.pack()

sentiment = tk.Text(root, height = 1, width = 140)
sentiment.config(state = "disabled", bg = "#808080")
sentiment.pack()

ulable = tk.Label(root, text = "URL")
ulable.pack()

utext = tk.Text(root, height = 1, width = 140)
utext.pack()

btn = tk.Button(root, text = "Summarize", command=summarize)
btn.pack()

# Run unless user cross the app
root.mainloop()