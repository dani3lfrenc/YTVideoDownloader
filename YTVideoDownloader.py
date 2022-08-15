#!/usr/bin/env python3

# Import all the necessary library



from pytube import YouTube

import rumps

import pygame_gui


#-------------------------------------------------------


class YTVideoDownloader(object):

    def __init__(self):




        self.app = rumps.App(name="YTVideoDownloader")

        self.app.icon = 'icon.png'

        self.config = {

            "app_name" : "YTVideoDownloader",
  
        }

        self.window = rumps.Window(message="YTVideoDownloader", default_text="-------------------Paste first the link------------------\n\n------After a SPACE paste the path of the folder-------", ok="Download", dimensions=(320,160))
        

        self.download = rumps.MenuItem(title="Download", callback=self.downl)

        self.app.menu = [self.download]

#-------------------------------------------------------

# Create a function that download the video


    def downl(self, sender):

        response = self.window.run()
        
        if response.clicked == 1:

            link = str(response.text)
            
            list_obj = link.split(" ")

            print(list_obj)

            youtube_object = YouTube(list_obj[0])

            youtube_video = youtube_object.streams.get_highest_resolution()

            youtube_video.download(list_obj[1])

            
#-------------------------------------------------------         

# Function for run the application
        
    def run(self):
            self.app.run()


if __name__ == '__main__':
    app = YTVideoDownloader()
    app.run()