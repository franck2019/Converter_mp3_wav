#!/bin/bash

mkdir -p data/audio/wav
cd data/audio/mp3

for mp3_voice in *.mp3; do
    
    res=$(echo $mp3_voice | cut -d "." -f 1)
    
    sox $mp3_voice -r 16000 ../wav/$res.wav;
    if [[ $? -eq 0 ]]
    then
        echo "$mp3_voice converted into $res.wav"
    else
        echo "failed to convert"
    fi
done

