'''import moviepy.editor
video=moviepy.editor.VideoFileClip("war.mp4")
audio=video.audio
audio.write_audiofile("reasult.mp3")
'''
import moviepy.editor as mp 

# Insert Local Video File Path 
clip = mp.VideoFileClip(r"Dil Ke Dastakk.mp4") 

# Insert Local Audio File Path 
clip.audio.write_audiofile(r"reasult.mp3") 
