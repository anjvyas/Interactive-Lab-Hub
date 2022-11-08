import paho.mqtt.client as mqtt
import uuid
import os

# the # wildcard means we subscribe to all subtopics of IDD
aa_topic = 'IDD/Aashika'
an_topic = "IDD/Anjali"
msg_morse = []

# some other examples
# topic = 'IDD/a/fun/topic'


def morse_to_english(morse_code):
    english = ""
    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}

    new_dict = {MORSE_CODE_DICT[k]: k for k in MORSE_CODE_DICT}

    # each letter is split by _
    # each word is split by /
    words = morse_code.split("/")

    for word in words:
        # get all the letters
        letters = word.split("*")

        for letter in letters:
            english += new_dict[letter]

    return english

#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(aa_topic)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')


# this is the callback that gets called each time a message is recived
def on_message(client, userdata, msg):
	# print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    
	# you can filter by topics
	# if msg.topic == 'IDD/some/other/topic': do thing
    code = msg.payload.decode('UTF-8')
    print(code)
    # we have reached the end of the message
    if code == "!":
        # decrypt the morse code
        morse = ''.join([str(elem) for elem in msg_morse])
        print(morse)

        english = morse_to_english(morse)
        os.system(f"say '{english}'")
        client.publish(an_topic, english)

    else:
        msg_morse.append(code)

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_forever()