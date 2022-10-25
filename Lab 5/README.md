# Observant Systems

**NAMES OF COLLABORATORS HERE**


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1. Spend about 10 Minutes doing the Listening exercise as described in [ListeningExercise.md](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%205/ListeningExercise.md)
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo.(Please wait until thursday morning. There are still some incompatabilities to make the assignment work.)
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show the filledout answers for the Contextual Interaction Design Tool.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

The following command is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

##### Face Detection
<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%205/face_detection.png" width=70% height=70%>

We can make use of this face detection system to enable some cool smart home features. For instance, there can be a corner of the wall with a camera. Whenever someone directly looks at the camera, it automatically triggers the lights to turn on or off (or the AC or TV or any device). This would save the person the trouble of even needing to say something out loud. 

##### Contours Detection
<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%205/contours.png" width=70% height=70%>

Contour detection would be useful for artistic effects like those seen in Snapchat filters. Here is an idea for a spooky one that could be fun to use as halloween decor: there can be a system which continuously takes in video footage and relays it onto a bigger screen with contours marked in white, everything that is not a contour can be shown in black. For an artistic exhibit it could be fun to have live contours and non-contours shown in different bright colors with high contrast. This would be similar to Andy Warhol's art but would be in video form instead! https://www.wikiart.org/en/andy-warhol

##### Flow Detection
<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%205/flow_detection.png" width=70% height=70%>

Flow detection can be used by blind individuals to get a sense of how busy areas around them might be. The busyness captured through a video camera attached to a cane or glasses can be relayed to the individual in the form of subtle vibrations. However, a lot of care would need to be taken to make sure that the system is actually useful for their navigation and does not feel overwhelming, especially in highly busy areas.

##### Object Detection
<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%205/object_detection.png" width=70% height=70%>
Object detection can be used to track the movement of surgical instruments from video footage. This movement can then be fed into models that can compare performance between novice and experienced surgeons to give them advice on how to improve.

#### Filtering, FFTs, and Time Series data. 
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU or Microphone data stream could create a simple activity classifier between walking, running, and standing.

To get the microphone working we need to install two libraries. `PyAudio` to get the data from the microphone, `sciPy` to make data analysis easy, and the `numpy-ringbuffer` to keep track of the last ~1 second of audio. 
Pyaudio needs to be installed with the following comand:
``sudo apt install python3-pyaudio``
SciPy is installed with 
``sudo apt install python3-scipy`` 

Lastly we need numpy-ringbuffer, to make continues data anlysis easier.
``pip install numpy-ringbuffer``

Now try the audio processing example:
* Find what ID the micrpohone has with `python ListAvalibleAudioDevices.py`
    Look for a device name that includes `USB` in the name.
* Adjust the variable `DEVICE_INDEX` in the `ExampleAudioFFT.py` file.
    See if you are getting results printed out from the microphone. Try to understand how the code works.
    Then run the file by typing `python ExampleAudioFFT.py`



Using the microphone, try one of the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up a running averaging** Can you set up a running average over one of the variables that are being calculated.[moving average](https://en.wikipedia.org/wiki/Moving_average)

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

For technical references:

* Volume Calculation with [RootMeanSqare](https://en.wikipedia.org/wiki/Root_mean_square)
* [RingBuffer](https://en.wikipedia.org/wiki/Circular_buffer)
* [Frequency Analysis](https://en.wikipedia.org/wiki/Fast_Fourier_transform)


**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***

For this part, I implemented threshold detection. Here is a link to my code https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%205/part_a_threshold.py

My program first asks the user for a volume threshold. Then, whenever the sound goes above that volume threshold, the program prints "The volume is above [threshold value]!!".

### (Optional Reading) Introducing Additional Concepts
The following sections ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)) are included for your own optional learning. **The associated scripts will not work on Fall 2022's Pi Image, so you can move onto part B.** However, you are welcome to try it on your personal computer. If this functionality is desirable for your lab or final project, we can help you get a different image running the last OS and version of python to make the following code work.

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr25
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi3 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

~~\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\*~~

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

~~**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***~~


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.
* Fill out the ``Contextual Interaction Design Tool`` sheet.[Found here.](ThinkingThroughContextandInteraction.png)

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

I decided to think of a way to use the audio analysis model to implement functionality that could potentially be of benefit to people. As a student living in dorms and off campus apartments too, my rooms have often had thin walls. Sometimes when I get excited, I talk in quite a high pitched / loud voice and the next day my friends who live next door would joke that they could hear me. I've also had several friends who have had anonymous noise complaints given to them when they were just watching TV and didn't really realize that it was heard outside their room too. And of course, whenever they hosted parties, getting noise complaints was very common. A lot of times it is difficult to realize that the noise coming from your apartment is higher than it should be.

This is why I wanted to prototype a noise level detector that warns people when they are being too loud and potentially disturbing their neighbors. 

I tried out all these different noises with the system:
1. The sound of a TV show playing at different volumes (1 through 100)
2. The sound of me talking (softly to super loud)
3. The sound of a song (baby shark doo doo) playing from lowest to highest volume

I also tried a few different alert sounds to see which one was able to best cut through the sound that was already playing.
<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%205/design_tool.jpeg" width=70% height=70%>

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

#### When does it do what it is supposed to do?
The system emits a sound whenever the volume exceeds the threshold specified by the user.

#### When does it fail, and why?
It was very interesting to see which sounds the model considers to be high volume as opposed to soft volume. I just shuffled by jacket around a little bit and it found that to be loud, but then when I said something quite loudly but in a deep voice, it didn't find that to be loud. To be able to capture loud deep noises, maybe I can also include frequency as a parameter in my next iteration of this device. When I covered it slightly with a jacket, it wasn't able to detect any loud sounds. From this experiments, I learned that it would be very important to make sure that the device is placed in a spot that can't be obstructed and can freely capture sounds.

Another interesting issue that I noticed was that when I turned on the AC, its ability to detect loud sounds seemed to have diminished because of the ambient white noise that the AC made. 

#### What other scenarios could cause problems?
I wasn't able to test the system with extremely loud noises. The alert I am currently using might not even be heard in such situations. This is why the volume of the alert should probably be dynamic based on the volume of the sound that the system ends up capturing. Another potential (more complicated but cleaner) way around this problem would be to notify the user by sending an alert to their mobile device. This would avoid making a loud sound that would end up disturbing neighbors by itself too.

#### User considerations

##### Uncertainties in the system
There can be a lot of usability issues with using this system unless some measures are put in place:
1. In case there is a loud noise playing that is out of the user's control, it should be possible to very easily override the alert and temporarily turn the listening off (maybe through a button), otherwise the user would feel quite irritated.
2. Another uncertainty with using the system is manually specifying the volume threshold that should trigger the alert. Although offering this flexibility is important it is very unclear how a user would go about figuring out this threshold. Maybe, we can provide some simple calibration instructions for the user where they have a friend sit on the other side of the wall. Next the user can turn the volume up point by point while running the system and ask their friend to let them know as soon as they are able to hear the sound outside. Since the system prints the volume captured at every point in time, this way the user will be able to figure out what threshold will work best for their particular household given the roommate preferences as well as the wall thickness.

##### Consequences of misclassification
If an alert fails to play even though the noise level is high, the entire value of the system would be nullified. The users would get noise complaints and they would completely lose faith in the device.
If alerts keep playing even though the noise level is low, the user will feel very annoyed and just stop using the device.
This can be a tricky balance to achieve, especially if the user finds it difficult to accurately set up a threshold value.

##### How can I change my system to address this?
To minimize the chances of such situations (misclassifications arising), I would provide the user with some information in a brochure on standard threshold values that people tend to use and have worked well depending on their lifestyle preferences. Another smooth way to make this happen would be to offer a fun online quiz where they just answer some questions and then the quiz will give them a recommended threshold value. 

Another failsafe to keep in place in case users still end up setting wrong thresholds is having a warning message that says something like - "are you sure? this threshold is very low and will trigger an alert with very soft sounds too" or "are you sure? this threshold is very high, for context, an elephant would have to roar super loud for it to trigger". The system can have a sanity check for super high and super low thresholds and display these messages accordingly.

##### Optimizations to sense making algorithm
As I said previously, in my future iterations of this device I would definitely like to play around with frequency and a wider variety of sounds levels to see how that information can also be leveraged to provide a more accurate alert for disturbing sounds.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

#### Catophonous - the noisiness detector 🐱
<a href="https://youtu.be/u2tRoRxDOWI" title="Catophonous"><img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/Lab%203/video.png" width="40%" height="40%"></a>

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
