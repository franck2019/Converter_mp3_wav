# Converter_mp3_wav version 1.0
A script shell which converts *.mp3 files into .wav

This version take audio .mp3 files inside the directoty data/audio/mp3

The script will create a new directory called data/audio/wav to store converted file into .wav format using the command:
```
sox $mp3_voice -r 16000 ../wav/$res.wav;
```

The $rest value is the substring filename took from the name filename.mp3.
```
e.g. 1.mp3 will become 1.wav after conversion.
```

We extract the filename inside filename.mp3 by using the following trick:
```
res=$(echo $mp3_voice | cut -d "." -f 1)
```


