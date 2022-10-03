from pydub import AudioSegment
sound = AudioSegment.from_wav("recorded_stereo.wav")
sound = sound.set_channels(1)
sound.export("recorded_mono.wav", format="wav")