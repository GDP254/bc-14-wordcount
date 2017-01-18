#coding=utf-8

def words(sentence):
    sent_list = sentence.split()
    print ("Split given sentence into a list (word_list)")
    sent_set = set(sent_list)
    print ("Eliminate duplicate values in the word_list by converting it to a set (word_set)")
    word_count = {}
    print ("For each item in the word_set:")
    print ("    Check if the item resembles a number and if it does convert the item to integer")
    print ("    Populate a dictionary with elements of the word_set as keys and their respective counts in the word_list")
    for si in sent_set:
        sikey = si
        if si.isdigit():
            sikey = int(si)
        word_count[sikey] = sent_list.count(si)
    return word_count

