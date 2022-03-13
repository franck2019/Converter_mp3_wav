# Converter_mp3_wav version 2
A script shell which converts *.mp3 files into .wav

This version take audio .mp3 files inside the directoty data/audio/mp3

The script will create a new directory called data/audio/wav2 to store converted file into .wav format using the command:
```
sox $mp3_voice -r 16000 ../wav/$output.wav;
```

The $output value is the substring filename took from the name "filename.mp3".

We are going to rename it by adding 4 zero before if the length of fileneme is 1, 3 zero f the length of fileneme is 2 and so on... But the max length of the name of the file is 5.
```
e.g. 1.mp3 will become 00001.wav after conversion.
     22.mp3 -> 00022.wav
     101mp3 -> 00101.wav
```

We extract the filename inside filename.mp3 by using the following trick:
```
res=$(echo $mp3_voice | cut -d "." -f 1)
len=5
zero_to_add=$(( $len - ${#res} ))
out=$(printf '%*s' "$zero_to_add" | tr ' ' '0')
output=$(echo $out$res)
```

