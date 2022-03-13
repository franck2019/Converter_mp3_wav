#!/bin/bash

mkdir -p data/audio/wav2
cd data/audio/mp3

for mp3_voice in *.mp3; do
    
    res=$(echo $mp3_voice | cut -d "." -f 1)
    len=5
    zero_to_add=$(( $len - ${#res} ))
    out=$(printf '%*s' "$zero_to_add" | tr ' ' '0')
    output=$(echo $out$res)
    sox $mp3_voice -r 16000 ../wav2/$output.wav;
    if [[ $? -eq 0 ]]
    then
        echo "$mp3_voice converted into $output.wav"
    else
        echo "failed to convert"
    fi
    #echo $output
done

