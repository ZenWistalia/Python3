string = input("Text: ")

def isClosure(c):
    if c=='(':
        return True
    elif c==')':
        return True
    elif c==']':
        return True
    elif c=='[':
        return True
    elif c=='}':
        return True
    elif c=='{':
        return True
    else:
        return False

def isOpenClosure(c):
    if c=='(':
        return True
    elif c=='{':
        return True
    elif c=='[':
        return True
    else:
        return False

def isCloseClosure(c):
    if c==')':
        return True
    elif c=='}':
        return True
    elif c==']':
        return True
    else:
        return False

Closures ={
    '(':')',
    '[':']',
    '{':'}'
}

def Remove(string):
    if(len(string)%2 == 1):
        return False
    while(string!=""):
        print(string)
        i = 0
        for i in range(0,len(string)):
            if(Closures[string[i]]==string[i + 1]):
                break
        else:
            break
        string = string[:i] + string[i + 2:]
    else:
        return True
    return False



string = ''.join(c for c in string if isClosure(c))

print(Remove(string))