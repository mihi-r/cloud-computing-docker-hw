import glob
import os
import re
import socket


def main():
    """Writes statistics about the text files in the /home/data directory."""
    with open('/home/output/results.txt', 'w+') as result_file:
        text_file_names = [f for f in glob.glob('/home/data/*.txt') if os.path.basename(f) != 'results.txt']

        result_file.write('All text files present: \n')
        for text_file_name in text_file_names:
            result_file.write(f'{os.path.basename(text_file_name)} \n')

        total_word_count = 0
        max_word_count = 0
        max_word_file = "None"

        result_file.write('Word count of each file: \n')
        for text_file_name in text_file_names:
            with open (text_file_name) as text_file:
                word_count = len(re.findall(r'\w+', text_file.read()))
                result_file.write(f'{os.path.basename(text_file_name)} = {word_count} \n')

                total_word_count += word_count

                if word_count >= max_word_count:
                    max_word_count = word_count
                    max_word_file = text_file_name

        result_file.write(f'Total number of words in all files: {total_word_count} \n')

        result_file.write('Filename with max words: \n')
        result_file.write(f'{os.path.basename(max_word_file)} \n')

        result_file.write(f'IP: {socket.gethostbyname(socket.gethostname())} \n')

        result_file.seek(0)
        print(result_file.read())


if __name__ == '__main__':
    main()