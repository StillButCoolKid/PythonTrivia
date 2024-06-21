from random import *

def addQ():
    q = input("Enter Q: ")
    noA = int(input("Enter no of options: "))
    options = []
    
    for i in range(noA):
        options.append(input(f"Enter option {i+1}: "))
    correctOption = int(input("Enter correct option: "))

    questions[q] = [correctOption] + options
    c = open('c.txt', 'w')
    for i,v in questions.items():
        c.write(f'{i}\n{v}\n')
    c.close()

def QRand(noQ):
    l = []
    while len(l) < noQ:
        a = randrange(0, len(questions))
        if a not in l:
            l.append(a)
    return l

def pyrnt():
    noQ = int(input("How many Qs? "))
    assert noQ <= len(questions)
    q = list(questions.keys())
    a = list(questions.values())
    QRandomizer = QRand(noQ)
    for i in range(noQ):
        print(f"Q: {q[QRandomizer[i]]}")
        for j in range(1,len(a[QRandomizer[i]])):
             print(a[QRandomizer[i]][j])
        option = int(input("Your Answer: "))

        if option - 1 == a[QRandomizer[i]][0]:
            print("You're right!!!\n")
        else:
            print("Whoops! Try again.")

questions = {}

c = None
def readFile():
    global questions
    global c
    c = open('c.txt', 'r')
    r = (c.read().split('\n'))
    #print(r)
    for i in range(0,int((len(r)+1)/2),2):
        questions[r[i]] = eval(r[i+1])

readFile()

print('''
What do you wanna do?
1. Quiz
2. Add Q
''')
do = input('(1/2)')
if do == '1':
    pyrnt()
if do == '2':
    addQ()

c.close()
