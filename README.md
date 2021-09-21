# Installation:
`virtualenv .`  
`./bin/activate`  
`pip install -r requirements.txt`  

# Files:
The final csv file generated is: `/revised/merged_hanzi_data.csv`.  
It includes these columns on each rows, when available:  
`traditional`  
`simplified`  
`pinyin`  
`translation_en-US`  
`translation_fr-FR`  
`serial_number` (optional)  
`individual_raw_frequency` (optional)  
`cumulative_frequency_in_percentile` (optional)  
`hsk2.0` (optional)  
`hsk3.0` (optional)  


# Usage:
## cxdict_to_csv.py
If you are willing to merge another data source into this file, use:  
`$ cxdict_to_csv {cxdict_filepath} {language}`  

Where `{cxdict_filepath}` is the absolute or relative filepath to your cxdict file.  
`{language}` should be (not a requirement) of the form `{iso639-1}-{iso3166-1}` like 'en-US', 'fr-FR', 'de-DE'.  

## hsk_file_prefixer.py
This script can be used to build a csv file from the HSK3.0 data found in `/originals/hsk3_0_wordlist`.  
`$ cxdict_to_csv {hsk_levels_filepath} {hsk_version}`  

## hsk_file_prefixer.py
Merge multiple sources into on final csv file.  
Currently takes these arguments:  
`-ce` or `--csv_cedict_file`  
`-cf` or `--csv_cfdict_file`  
`-cfrq` or `--chinese_charfreq`  
`-hsk3wl` or `--hsk3_0_wordlist_file`  
`-hsk2wl` or `--hsk2_0_wordlist_file`  

which are all filepaths to files corresponding to the name of the argument.  
You could easily add an argument to merge another csv. The only requirement being to take care which column(s) you merge with pandas.  

# Sources
https://www.mdbg.net/chinese/dictionary?page=cedict  
https://lingua.mtsu.edu/chinese-computing/  
https://raw.githubusercontent.com/gigacool/hanyu-shuiping-kaoshi/master/hsk.csv  
https://github.com/infinyte7/HSK-3.0-words-list  
