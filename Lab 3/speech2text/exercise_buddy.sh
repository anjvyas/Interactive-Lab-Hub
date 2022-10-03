i=0
python3 rep_counter.py &
while [ $i -le 10 ] # keep recording in 5 second increments for 1 min total
do 
    arecord -D hw:1,0 -f cd -c 2 -r 32000 -d 5 -t wav recorded_stereo.wav
    python3 stereo_to_mono.py # convert stereo sound from my webcam to mono sound
    python3 test_words.py recorded_mono.wav # count the number of exercises done
    ((i++))
    sleep 1
done