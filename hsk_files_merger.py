"""
Input: Hsk data files.
Output: HSK infos merged file.
"""

import argparse
import os

import pandas

MERGE_FILEPATH = os.path.join(os.getcwd(), 'revised/merged_hanzi_data.csv')


HEADERS = [
    'simplified', 'traditional', 'pinyin', 'translation',
    'hsk2.0', 'hsk3.0',
]

HSK3_0_FILENAME = 'hsk_words_list.csv'


def merge_to_csv(csv_cedict_file, csv_cfdict_file, chinese_charfreq_file,
                 hsk2_0_wordlist_file, hsk3_0_wordlist_file):
    cedict_df = pandas.read_csv(csv_cedict_file, sep='\t')
    cfdict_df = pandas.read_csv(csv_cfdict_file, sep='\t')
    charfreq_df = pandas.read_csv(chinese_charfreq_file, sep=',')
    hsk2_0_wordlist_df = pandas.read_csv(
        hsk2_0_wordlist_file, sep='\t', dtype={'hsk2.0': str}
    )
    hsk3_0_wordlist_df = pandas.read_csv(hsk3_0_wordlist_file, sep='\t')

    # Merge HSK levels
    hsk_levels_df = pandas.merge(
        hsk3_0_wordlist_df[
            [
                'hsk3.0',
                'simplified',
                'pinyin',
            ]
        ],
        hsk2_0_wordlist_df[
            [
                'hsk2.0',
                'simplified',
                'pinyin',
            ]
        ],
        on='simplified', how='left'
    )

    # Merge cedict merge with hsk levels
    cxdict_df = pandas.merge(
        cedict_df,
        cfdict_df[
            [
                'translation_fr-FR',
                'pinyin',
                'simplified',
            ]
        ],
        on=['pinyin', 'simplified'], how='left'
    )

    # Merge cedict with frequencies
    cxdict_freq_df = pandas.merge(
        cxdict_df,
        charfreq_df[
            [
                'serial_number',
                'simplified',
                'individual_raw_frequency',
                'cumulative_frequency_in_percentile',
            ]
        ],
        on='simplified', how='left'
    )

    # Merge cedict merge with hsk levels
    cxdict_freq_hsk_df = pandas.merge(
        cxdict_freq_df,
        hsk_levels_df[
            [
                'hsk2.0',
                'hsk3.0',
                'simplified',
            ]
        ],
        on='simplified', how='left'
    )

    cxdict_freq_hsk_df = cxdict_freq_hsk_df.sort_values(
        by=["cumulative_frequency_in_percentile"], ascending=True
    )
    cxdict_freq_hsk_df = cxdict_freq_hsk_df.drop_duplicates(
        subset=['simplified', 'translation_en-US'], keep='last'
    )
    cxdict_freq_hsk_df.to_csv(MERGE_FILEPATH, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process hsk data files to merge them.'
    )
    parser.add_argument(
        '-ce',
        '--csv_cedict_file', nargs='?',
        help='Path to csv_cedict_file file.',
        default="./revised/cedict_ts.csv",
    )
    parser.add_argument(
        '-cf',
        '--csv_cfdict_file', nargs='?',
        help='Path to csv_cfdict_file file.',
        default="./revised/cfdict_ts.csv",
    )
    parser.add_argument(
        '-cfrq',
        '--chinese_charfreq', nargs='?',
        help='Path to chinese_charfreq file.',
        default="./originals/chinese_charfreq_simpl_trad.csv",
    )
    parser.add_argument(
        '-hsk3wl',
        '--hsk3_0_wordlist_file', nargs='?',
        help='Path to hsk wordlist words directory.',
        default="./revised/hsk3_0_wordlist.csv",
    )
    parser.add_argument(
        '-hsk2wl',
        '--hsk2_0_wordlist_file', nargs='?',
        help='Path to hsk wordlist words directory.',
        default="./originals/hsk2_0_wordlist.csv",
    )

    args = parser.parse_args()
    csv_cedict_file = args.csv_cedict_file
    csv_cfdict_file = args.csv_cfdict_file
    chinese_charfreq_file = args.chinese_charfreq
    hsk3_0_wordlist_file = args.hsk3_0_wordlist_file
    hsk2_0_wordlist_file = args.hsk2_0_wordlist_file

    merge_to_csv(
        csv_cedict_file,
        csv_cfdict_file,
        chinese_charfreq_file,
        hsk2_0_wordlist_file,
        hsk3_0_wordlist_file
    )
