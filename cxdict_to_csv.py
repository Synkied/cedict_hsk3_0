"""
A parser for the CC-Cedict. Convert the Chinese-English dictionary into
a list of python dictionaries
with "traditional","simplified", "pinyin",and "translation" keys.

Make sure that the cedict_ts.u8 file is in the same folder as this file,
and that the name matches the file name on line 13.

Before starting, open the CEDICT text file and delete the copyright information
at the top. Otherwise the program will try to parse it
and you will get an error message.

Characters that are commonly used as surnames have two entries in CC-CEDICT.
This program will remove the surname entry
if there is another entry for the character.
If you want to include the surnames, simply delete lines 59 and 60.

This code was written by Franki Allegra in February 2020.
Cleaned and updated by Quentin Lathiere August 2021.
"""

import argparse


def parse_line(line):
    parsed = {}
    if line == '':
        return 0
    line = line.rstrip('/')
    line = line.split('/')
    if len(line) <= 1:
        return 0
    translation = '|'.join(line[1:-1]).replace('"', '\'')
    char_and_pinyin = line[0].split('[')
    characters = char_and_pinyin[0]
    characters = characters.split()
    traditional = characters[0]
    simplified = characters[1]
    pinyin = char_and_pinyin[1]
    pinyin = pinyin.rstrip()
    pinyin = pinyin.rstrip("]")
    parsed['traditional'] = traditional
    parsed['simplified'] = simplified
    parsed['pinyin'] = pinyin
    parsed['translation'] = translation

    reworked_line = '\t'.join(
        [traditional, simplified, pinyin, '"{}"'.format(translation)]
    )

    return reworked_line


def to_csv(cxdict_filepath, csv_cedict_headers, merge_filepath):
    with open(cxdict_filepath) as f1, open(merge_filepath, "w") as f2:
        lines = f1.readlines()
        f2.write('{}\n'.format('\t'.join(csv_cedict_headers)))

        for line in lines:
            line = parse_line(line)

            f2.write('{}\n'.format(line))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process a CXDICT file into csv file.'
    )
    parser.add_argument(
        'cxdict_filepath', nargs='?',
        help='Path to CXDICT file.',
        default="./originals/cedict_ts.u8",
    )
    parser.add_argument(
        'language', nargs='?',
        help='CXDICT file language.',
        default="en-US",
    )

    args = parser.parse_args()
    cxdict_filepath = args.cxdict_filepath
    language = args.language

    csv_cedict_headers = [
        'traditional', 'simplified', 'pinyin',
        'translation_{}'.format(language)
    ]
    merge_filepath = './revised/c{}dict_ts.csv'.format(language[0])

    to_csv(cxdict_filepath, csv_cedict_headers, merge_filepath)
