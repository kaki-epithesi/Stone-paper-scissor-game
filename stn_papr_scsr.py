#!/usr/bin/env python3
#! -*- coding: 'utf-8' -*-

import random
import time

def selector(choice):
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    else:
        return 'Scissor'

print ('Rules :\n1>Rock Vs Paper => Paper Wins')
print ('2>Rock Vs Scissor => Rock Wins')
print ('3>Paper Vs Scissor => Scissor Wins')
name = input('Enter you name : ')

while True:
    print ('1:ROCK      2:PAPER       3:SCISSOR')
    usr_chc = int(input('{}, Enter Your Choice : '.format(name)))

    while usr_chc > 3 or usr_chc < 1 :
        usr_chc = int(input('Enter Valid Choice : '))

    usr_chc_name = selector(usr_chc)

    print ('{} choice : {}'.format(name,usr_chc_name))

    print ('Computer\'s  turn')
    comp_chc = random.randint(1,3)
    time.sleep(2)
    while comp_chc == usr_chc:
        comp_chc = random.randint(1,3)

    comp_chc_name = selector(comp_chc)
    print ('Computer\'s choice : {}'.format(comp_chc_name))

    print ('{} Vs {}'.format(usr_chc_name,comp_chc_name))
    time.sleep(2)
    if usr_chc*comp_chc == 2:
        result = 'Paper'
    elif usr_chc*comp_chc == 3:
        result = 'Rock'
    else:
        result = 'Scissor'

    if result == usr_chc_name:
        print ('{} wins'.format(name))
    else:
        print ('Computer Wins')

    chc = input('Play Again? y or n : ')

    if chc == 'n' or chc == 'N':
        break

print ('Thanks for playing , {}'.format(name))
