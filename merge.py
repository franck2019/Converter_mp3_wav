# a python file to merge "dict - Yemba".csv and preparing.csv

import pandas as pd

# Reading csv files
cols1_types= {"record_id": str,"speaker_id": str,"Utterance_id": str,"10combined_letter": str,"extended_filename": str,"text_id": str,"sentence_id": int}

preparing_df = pd.read_csv('preparing.csv', sep=';', dtype=cols1_types)
dict_yemba_df = pd.read_csv('dict-yemba.csv', dtype={"sentence_id": int, "sentence":str})

#print(preparing_df.dtypes)

# We are going to use the merge function by setting how= 'right'
# since some sentences don't have audio
global_data_df = pd.merge(preparing_df, dict_yemba_df, on='sentence_id', how='right')

# save our global df into a csv file called global_data.csv
global_data_df.to_csv('./product/global_data.csv', index=False)


# extraction The wav.csv file metadata structure
# <record-id> <extended-filename>

wav_df = global_data_df[['record_id','extended_filename']]
#print(wav_df)
wav_df.to_csv('./product/wav.csv', index=False)

# The utt2spk.csv file meta data structure
# <utterance-id> <speaker-id>

utt2spk_df = global_data_df[['Utterance_id','speaker_id']]
utt2spk_df.to_csv('./product/utt2spk.csv', index=False)

#end of extraction
