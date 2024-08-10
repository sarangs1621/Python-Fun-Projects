
import pafy  
  
url = input("enter the youtube url to convert mp3:")
video = pafy.new(url) 
  
bestaudio = video.getbestaudio() 
bestaudio.download() 
