# -*- coding: utf-8 -*-
import string
from collections import Counter
import csv
import json
import pickle


def main(filename):
    # read file into lines
    #name = str(input("Please enter the path of file you want to open: "))
    txtfile = open(filename)
    lines = txtfile.readlines()

    # declare a word list
    all_words = []

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        line = line.strip()
        words = line.split()

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            word = word.strip(string.punctuation)
            # check if word is not empty
            if word.isalpha and word != '':
                # append the word to "all_words" list
                all_words.append(word)

    # compute word count from all_words
    counter = Counter(all_words)
    counter.most_common()
    for ch, count in counter.most_common(): 
        print(ch, count)
    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open("wordcount.csv", "w" ) as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(counter.most_common())


    # dump to a json file named "wordcount.json"
    f = open("wordcount.json", 'w')
    json.dump(counter.most_common(), f)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    pickle.dump(counter.most_common(), open("wordcount.pkl", 'wb'))


if __name__ == '__main__':
    main("i_have_a_dream.txt")
