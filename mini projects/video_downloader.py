# import the yt_dlp module, which is used for downloading videos from YouTube and other sites.
import yt_dlp

# get url from user
url = input("Enter url of the video: ") #prompting user for url

ydl_opts = {} #creating an empty dictionary of options.

# create a context for the YoutubeDL object using the options defined in 'ydl_opts'
with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
    ydl.download([url]) #calling the download function and passing the url as argument.

print("Video downloaded successfully!") #display message indicating successful download of video