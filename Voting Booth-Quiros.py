# Assignment 6: Voting Booth
# Julian Quiros

from tkinter import *

top = Tk()

fr1 = Frame(top, bg = 'blue')
fr1.grid()

lbl1 = Label(fr1, text = 'Who are you voting for President?', fg = 'red')
lbl1.grid(row = 0, column = 0, padx = 10, pady = 10)

fr2 = Frame(top)
fr2.grid()

   
hil_votes = 0
def hil_vote_count():
    global hil_votes
    hil_votes += 1
    return hil_votes

def hil_label():
    hil_vote_count()
    lbl4 = Label(fr2, text = str(hil_votes))
    lbl4.grid(row = 1, column = 10)
    winner_label()

don_votes = 0    
def don_vote_count():
    global don_votes
    don_votes += 1
    return don_votes

def don_label():
    don_vote_count()
    lbl5 = Label(fr2, text = str(don_votes))
    lbl5.grid(row = 2, column = 10)
    winner_label()

gar_votes = 0 
def gar_vote_count():
    global gar_votes
    gar_votes += 1
    return gar_votes

def gar_label():
    gar_vote_count()
    lbl6 = Label(fr2, text = str(gar_votes))
    lbl6.grid(row = 3, column = 10)
    winner_label()

jil_votes = 0  
def jil_vote_count():
    global jil_votes
    jil_votes += 1
    return jil_votes

def jil_label():
    jil_vote_count()
    lbl7 = Label(fr2, text = str(jil_votes))
    lbl7.grid(row = 4, column = 10)
    winner_label()


def winner_label():
    winner_list = []
    winner_list.append(jil_votes)
    winner_list.append(hil_votes)
    winner_list.append(don_votes)
    winner_list.append(gar_votes)
    winner_list.sort()
    result = StringVar()
    lbl20 = Label(fr2, textvariable = result)
    lbl20.grid(row = 6, column = 0)
    if jil_votes > hil_votes and jil_votes > don_votes and jil_votes > gar_votes:
        result.set('     Winner: Jill Stein     ')
    if hil_votes > jil_votes and hil_votes > don_votes and hil_votes > gar_votes:
        result.set('Winner: Hillary Clinton')
    if don_votes > hil_votes and don_votes > gar_votes and don_votes > jil_votes:
        result.set('Winner: Donald Trump')
    if gar_votes > hil_votes and gar_votes > don_votes and gar_votes > jil_votes:
        result.set('Winner: Gary Johnson')
    if winner_list[-1] == winner_list[-2]:
        result.set('     The Race is Tied!     ')

    # text variable w/in label code from: effbot.org/tkinterbook/label.htm
    

lbl2 = Label(fr2, text = 'Candidate:')
lbl2.grid(row = 0, column = 0)

lbl3 = Label(fr2, text = 'Votes:')
lbl3.grid(row = 0, column = 10)

Button(fr2, text = 'Hillary Clinton', fg = 'blue', command = hil_label).grid(row = 1, column = 0)
Button(fr2, text = 'Donald Trump', fg = 'red', command = don_label).grid(row = 2, column = 0)
Button(fr2, text = 'Gary Johnson', fg = 'black', command = gar_label).grid(row = 3, column = 0)
Button(fr2, text = 'Jill Stein', fg = 'green', command = jil_label).grid(row = 4, column = 0)



mainloop()
