## Project Plan

### Team Members:
Aashika Perunkolam [ap966]
Anjali Vyas [av379]

### Big Idea: 

Older adults with cognitive deficits often find it difficult to live independently as they require assistance with different tasks of daily living. To enable independent living we are going to focus on one of the most critical tasks of daily living for older adults which is to take their medications on time to prevent further cognitive decline.

We are going to build a smart medicine dispenser that has the following functions:

### Design of our Smart Medicine Dispenser:

<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/design.png" width=70% height=70%>

Step 1: 
Place the pill bottle in on the tray on the side of the device. 
Once the pill bottle is detected using the Proximity Sensor, the camera takes an image of the label on the pill bottle. 
The captured image is parsed through an image to text conversion software to detect the medicine name. 
The detected pill name is displayed on the screen of the device.

Step 2: 
Once the medicine name is detected, the servo motor opens the lid of the device and the user can pour in all the pills in the bottle into the compartment.
This completes the refilling process for the medicines in the medicine dispenser.

Step 3:
When it's time to take the medicine, the device produces a sound alert from the speaker using a TTS file.
It reminds the user to take the medicine.

Step 4:
Once the user approaches the device based on the sound alert, the display screen asks the user “How do you want to take the medicine?”
There are three buttons on the device. Each button indicates the types of formulation for the medicine. Button 1 indicates that the pill will be split into two halves across the serration already provided. Button 2 indicates that the pill will be dispensed as a whole, without a change in Formulation. Button 3 indicates that the pill will be dispensed in powdered form [This can only be done for certain pills without enteric coating, so we will have a mechanism to check if the medicine can be powdered or not before crushing it.]


### Differentiators:

Despite the presence of smart medicine dispensers in the market, none of them really cater specifically to the needs of older adults with cognitive deficits. Whereas our device caters specifically to older adults with cognitive deficits in the following two ways:
Reduces cognitive load on the user by eliminate the need of text input:
All of the dispensers currently available in the market require users to enter medicine name and prescription labels manually into the device through the app. 
However older adults with cognitive deficits find it difficult to read the labels on pill bottles as the text is extremely small. 
To eliminate the need for manual input to the device we are automating the process of entering the medicine name by capturing an image of the pill bottle and using an image to text conversion software to decode the medication name.
Alters the form of the medicine to make pills easier to swallow:
Older adults find it difficult to swallow pills that are larger in size. 
To make this easier our device provides different formulations for the same pill based on a check that is done to determine if it is legal to crush that particular pill before dispensing it. 
If it is not legal the device will provide an error message to the user indicating that they cannot change the formulation for that pill. 
This is a novel feature of our device and has not been implemented before.


### Timeline: 

Here is the timeline we intend to follow to get our interactive device ready on time:

<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/timeline.png" width=30% height=30%>

To make sure we create the most robust physical interface possible for our purposes we will be relying on the advice of maker lab members so we intend to meet with them before we begin this whole process.


### Parts Needed: 

Raspberry Pi [1]
Proximity Sensor [1]
Camera + Speaker [1]
Servo Motor [1]
Display Screen [1]
Buttons [3]


### Risks/Contingencies: 

There are several risks associated with our project that we will be putting conscious efforts to mitigate:

- It might be difficult for our image detection model to read the pill names correctly because of a lot of different factors such as bad lighting or the information being displayed on a curved surface.
- We are not sure about the best way to dispense pills one at a time, we need to brainstorm different approaches for this.
- We need to make sure that our design is friendly for older adults to use, if we had more time we would test it out with them and iterate on the design from there. However, in the time we have to make our design as friendly as possible we will research common problems older adults tend to face with electronic devices.
- Older adults who have poor memory might end up trying to crush pills that they should not be crushing. We need to have some security features in place which prevent cases like this from happening (we were envisioning checking some kind of hard coded database which maps each medication to true / false values representing whether it can be crushed or cut).
- Pills come in all shapes and sizes, we need to make sure that our holding, crushing and cutting capabilities can handle all of these somehow.

### Fall-back plan:

We will try our best to address all the risks mentioned above. However, in case we are not able to mitigate all of them, here is our plan for what alternative, simpler approaches we can take:

- We can use speech2text to allow users to provide the pill name to the device - this is a little more work on the part of the user but is likely to be more robust than the image solution.
- In case the pill loading / name detection functionality ends up being too complex to implement in our time frame, we will focus on just implementing the dispensing portion really well.
- In case we are not able to implement the security feature, we will make sure to mention this in our instructions and say that the device would be better intended for use by trained caregivers instead of older adults directly.
- We will try to make our device work with just a few pill shapes and sizes as a simple, initial prototype and will mention this limitation upfront.


### Slide for in-class presentation:

<img src="https://github.com/anjvyas/Interactive-Lab-Hub/blob/Fall2022/slide.png" width=70% height=70%>
