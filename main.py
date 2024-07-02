'''
from moviepy.editor import VideoFileClip,concatenate_videoclips,vfx

c1=VideoFileClip("1.mp4").subclip(0,5)
c2=VideoFileClip("2.mp4").subclip(0,5)
c3=VideoFileClip("1.mp4").subclip(0,5).fx(vfx.colorx,1.5)\
                                                  .fx(vfx.lum_contrast,0,50,128)

cc=concatenate_videoclips([c1,c2,c3])
cc.write_videofile("cc.mp4")

'''

from moviepy.editor import ImageSequenceClip
import os

# Define the path to the directory containing your images
image_folder = 'BRAVE'

# List all files in the directory and sort them
image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(('.png', '.jpg', '.jpeg'))]

# Define the frame rate for your video
fps =6

# Create a video clip from the image sequence
video_clip = ImageSequenceClip(image_files, fps=fps)

# Write the video file
video_clip.write_videofile("output_video.mp4", codec="libx264")
