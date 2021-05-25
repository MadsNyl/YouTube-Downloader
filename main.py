import tkinter as tk
from pytube import YouTube
import datetime

# set up tkinter window
root = tk.Tk()

# window setup
canvas = tk.Canvas(root, width = 800, height = 600)
canvas.pack()

# user input
headerLabel = tk.Label(root, text = 'YouTube Downloader')
headerLabel.config(font=('serif, 22'))
inputLabel = tk.Label(root, text = 'Enter your YouTube URL:')
inputLabel.config(font=('serif, 14'))
canvas.create_window(400, 140, window = inputLabel)
canvas.create_window(400, 40, window = headerLabel)

entry = tk.Entry()
canvas.create_window(370, 200, window=entry)


# function for downloading youtube video


def getURL () :
    global link, yt, ys
    link = entry.get()
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()

    fileLabel = tk.Label(root, text = f'FileTitle: {yt.title} \n\n FileSize: {round(ys.filesize * 0.000001)} mb \n\n Length: {datetime.timedelta(seconds = yt.length)}')
    fileLabel.config(font=('serif, 12'))
    canvas.create_window(400, 360, window = fileLabel)

def downloadURL () :
    ys.download()
    donwloadFinishedLabel = tk.Label(root, text = 'Download Finished! Enjoy!')
    donwloadFinishedLabel.config(font=('serif, 16'))
    canvas.create_window(400, 550, window = donwloadFinishedLabel)
    entry.delete(0, 'end')




# buttons
loadButton = tk.Button(text = 'Load', command = getURL, bg='green', fg='white', font=('serif', 10, 'bold'))
downloadButton = tk.Button(text = 'Download', command = downloadURL, bg='green', fg='white', font=('serif', 10, 'bold'))
canvas.create_window(530, 200, window = loadButton)
canvas.create_window(400, 490, window = downloadButton)





tk.mainloop()