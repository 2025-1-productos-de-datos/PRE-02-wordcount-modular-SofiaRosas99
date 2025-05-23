# obtain a list of files in the input directory
import os

from homework.src._internals.count_words import count_words
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_in_words
from homework.src._internals.write_word_counts import write_count_words


def main():

    input_folder = "data/input/"
    output_folder = "data/output/"

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_in_words(all_lines)
    counter = count_words(words)
    write_count_words(counter, output_folder)


if __name__ == "__main__":
    main()
