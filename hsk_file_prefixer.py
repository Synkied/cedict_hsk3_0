"""
Input: HSK directory with hsk_x.csv/tsv files.
Output: HSK csv file with every words and their HSK level.
"""

import argparse
import os


def prefix_hsk(filepath, headers, merge_filepath):
    hsk_words_lines = []
    for (dirpath, dirnames, filenames) in os.walk(filepath):

        for filename in filenames:
            if 'wordlist' in filename:
                continue

            hsk_level = filename.split('_')[-1].split('.')[0]
            fullpath = os.path.join(dirpath, filename)
            fname, ext = os.path.splitext(filename)

            with open(fullpath) as hsk_level_file:
                lines = hsk_level_file.readlines()

                for line in lines:
                    line = '{}\t{}'.format(hsk_level, line)
                    if line[-1] != '\n':
                        line = '{}\n'.format(line)

                    hsk_words_lines.append(line)

    with open(merge_filepath, 'w') as hsk3_0_file:
        hsk3_0_file.write('{}\n'.format('\t').join(headers))
        hsk3_0_file.writelines(hsk_words_lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process hsk file without level to prefix with.'
    )
    parser.add_argument(
        'hsk_levels_filepath', nargs='?',
        help='Path to hsk levels words directory.',
        default="./originals/hsk3_0_wordlist/",
    )
    parser.add_argument(
        'hsk_version', nargs='?',
        help='Path to hsk levels words directory.',
        default='3.0',
    )

    args = parser.parse_args()
    hsk_levels_filepath = args.hsk_levels_filepath
    hsk_version = args.hsk_version

    headers = [
        'hsk{}'.format(hsk_version), 'traditional', 'simplified',
        'pinyin', 'translation',
    ]

    hsk_version = hsk_version.replace('.', '_')
    merge_filepath = './revised/hsk{}_wordlist.csv'.format(hsk_version)

    prefix_hsk(hsk_levels_filepath, headers, merge_filepath)
