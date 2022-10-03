#!/usr/bin/env python3
#New file created
import os
import sys  
import argparse
from multiprocessing import Pool




#create the parser 
my_parser = argparse.ArgumentParser(description="List the content of the folder", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#add arguments
#example syntax, my_parser.add_argument('-c', '--create', action='store_true', help="X should equal one, hey we are learnign here")

#basic math
my_parser.add_argument('-m', '--multiply', action='store_true', help="This will multiply x + y")
my_parser.add_argument('-a', '--add', action='store_true', help="This will add x + y")
my_parser.add_argument('-s', '--subtract', action='store_true', help="this will subtract x from y")
my_parser.add_argument('-d', '--divide', action='store_true', help="This will divide x by y.")

my_parser.add_argument('--square',action='store_true', help="Square x")

args = my_parser.parse_args()

def mult(x, y):
        num = x * y

        return num
def add(x, y):
    num = x + y
    return num
def subtract(x, y):
    num = x - y
    return num

def divide(x, y):
    num = x / y
    return num

def square(x):
    return x*x
       
# command line interface

if args.multiply:
   print(mult(x=int(input("enter a value for x\n")), y=int(input("enter a value for y \n"))))

if args.divide:
    print(divide(x=int(input("enter value for x\n")), y=int(input("Enter a value for y\n"))))

if args.add:
    print(add(x=int(input("Enter value for x\n")),y=int(input("Enter a value for y\n"))))

if args.subtract:
    print(subtract(x=int(input("Enter a value for x\n")),y=int(input("Enter a value for y\n"))))


if args.square:
    print(square(x=int(input("Enter value to sqaure\n"))))

def main():
    print('Welcome to my first cli')

    pass


if __name__=='__main':
    #todo's ---add multiprocesser with pool cpu cores below-----
    main()













