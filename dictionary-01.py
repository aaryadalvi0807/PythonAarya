#!/usr/bin/Python

def create_dict():
    return {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

def display_values(d):
    print "dict['Name']: ", d['Name']
    print "dict['Age']: ", d['Age']

def main():
    data = create_dict()
    display_values(data)

main()
