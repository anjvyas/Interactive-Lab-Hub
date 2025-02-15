# Chatterboxes
**NAMES OF COLLABORATORS HERE**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

My idea is for a device that can support people as they exercise. A lot of times when doing reps, people lose track of how many they have done. When counting the number of seconds with exercises like planks, people often end up counting inaccurately, especially when they might feel tired.

\*\***Post your storyboard and diagram here.**\*\*
![Pushup storyboard](https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/exercise_pushup.jpg)
![Squat storyboard](https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/exercise_squat.jpg)
![Plank and summary storyboard](https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/exercise_plank_summary.jpg)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*
My process was to create flow chart with my initial idea in figma. Then I went through and added comments while trying to improve every aspect of the diaogue.
![Dialogue Ideas](https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/dialogue_ideas.png)


### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

<a href="https://youtube.com/shorts/y-MSARshY0Q" title="Exercise buddy"><img src="https://images.unsplash.com/photo-1611162616475-46b635cb6868?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2274&q=80" width="40%" height="40%"></a>

Interesting things I noticed:
- My friend ended up using the stop keyword with the exercises other than the plank too even though I didn't mention it as an option. In hindsight I realized that this would be a good way to do it so when I actually write the code, I will do it this way.
- I also felt that the user might want to start the exercise even before the device finishes saying "starting the count for [exercise name]" so it needs to be alert for this case. 

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

### (1) Feedback
Here is the feedback I received on part 1 from Saki:
- Add a motivating component to the voice.
- Try to record data from exercises to show the user progress over time.

### (2) Modes of interaction beyond speech
Speech would definitely be the most convenient medium to interact with the device, however, in some noisy gym environments this approach may not be feasible, so an alternate version of the device can make use of buttons to switch between exercises. Also it may not be apparent as to how the device functions so a small display showing instructions visually for users would also be very useful.

### (3) New dialogue based on feedback
<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/dialogue_pt2.png" width=70% height=70%>

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

For my first try, I tried implementing the actual system, without any wizarding. I felt that this would result in a smoother user experience too.

To implement this, I wrote a shell script that allows me to continuously record with the microphone in 5 second increments and analyze the speech to output sounds accordingly - https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/speech2text/exercise_buddy.sh

I ran this python file (rep_counts.py) in parallel with the while loop that continuously records microphone sounds - https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/speech2text/rep_counter.py

rep_counts.py uses input from the proximity sensor as well and continously monitors and modifies the summary json file to keep track of the number of times the person has done pushups, squats, what the current command is (pushups, squats, stop or summary) - https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/speech2text/summary.json

My webcam's microphone was not working so I made use of my personal stereo webcam for its microphone and used the school provided webcam for its speaker. The shell script runs file to convert the sound from stereo - https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/speech2text/stereo_to_mono.py

After the recorded sound is converted from stereo to mono, the shell script runs test_words.py - a python file that identifies the words in the sound file - https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/speech2text/test_words.py

test_words.py updates summary.json (the file that rep_counts continously monitors) with the current exercise/command it heard from the microphone so that rep_counts can add counts to the correct exercise or say the summary.

Even though the system works in theory, in practice there is quite a lot of lag in the time it takes for the program to identify words from speech which would not be enjoyable for users. This is why, I switched to the wizarding approach. My setup can be seen in the video below.

<a href="https://youtube.com/shorts/3L6x85beG_U?feature=share" title="How the system is set up"><img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/video.png" width="40%" height="40%"></a>


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

### Video of friend interacting with device

<a href="https://youtube.com/shorts/-yEdhCRKeH0?feature=share" title="Exercise Buddy Prototype Interactions"> <img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/video.png" width="40%" height="40%"> </a>

Answer the following:

### What worked well about the system and what didn't?
In the original (non-wizarding) system, the lag of the speech2text interpreter made the system a little difficult to use practically. The wizarding setup was very smooth though and the only issue I encountered with it was its inability to pronounce the name of my friend correctly, although to be fair this is a problem most smart assistants have too. 

### What worked well about the controller and what didn't?
Even though the sound output was almost instantaneous, which was great, it was tricky to type everything fast enough and sometimes there ended up being a lag just because of this issue. This is why after my first trial run I made sure to keep common ready to copy and paste dialogue options written down that can be immediately pasted based on what the user does.  

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
One lesson I have taken away from this is that it is very useful to do a WoZ interaction first rather than an autonomous version as I did because I learned a lot from the WoZ version and it took much less time to do. One thing I would do is put a lot more emphasis on making the device appealing to use and portable because my friend who interacted with it found the wires and separate components to be quite unwieldy. It would be a good idea to package all components into one visually appealing closed container for next time. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
It would be useful to record how close people tend to get to the prozimity sensor while doing pushups and squats and compare this to what the advised proximity would be if the exercise is done in proper form. It would also be useful to see how people pronounce the different exercise names to make sure the analyzer is inclusive and works well for people with different accents. Another idea is that instead of using speech to trigger an exercise, we could also use gestures in high noise envrionments. 


