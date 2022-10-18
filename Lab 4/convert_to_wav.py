import subprocess
  
# convert mp3 to wav file
subprocess.call(['ffmpeg', '-i', 'D.mp3',
                 'D.wav'])

subprocess.call(['ffmpeg', '-i', 'D_sharp.mp3',
                 'D_sharp.wav'])

subprocess.call(['ffmpeg', '-i', 'F.mp3',
                 'F.wav'])

subprocess.call(['ffmpeg', '-i', 'G.mp3',
                 'G.wav'])