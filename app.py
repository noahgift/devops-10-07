#!/usr/bin/env python

def hello(name):
    return f"Your name is: {name}"

#This catches a future bug
#1==1

if __name__ == "__main__":
    print(hello("bob"))