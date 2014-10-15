#!/usr/bin/env python

import os
import csv
import random
import string

currentdirpath = os.getcwd()
filename = 'choices.csv'

file_path = os.path.join(os.getcwd(), filename) #filepath to open

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    return file_path



path = get_file_path('choices.csv')

def get_random_string():
    rnstring = ''
    for i in range(0,4):
        rnstring += random.choice(string.ascii_letters)
    return rnstring


    

def read_csv(filepath):
    emails = {}
    i = 0
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not "Email Address" in row:
                print row[0]
                fake_email = email[:4] + get_random_string() + "@" + "gmail.com"
                print fake_email
                emails[i] = fake_email
                i += 1
    print emails
    return emails
                



def get_winner():
    emails = read_csv(path)
    #start with one
    print len(emails)
    for i in range (0, len(emails)):
        print emails[i]    
    ran_num = random.randint(0, len(emails))
    winner = emails[ran_num]
    print "And the winner is %s %s" %(winner, ran_num)


get_winner()
