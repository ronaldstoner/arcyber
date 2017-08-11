# ARCYBER cipher text generator 
# Modified from existing code on the internet 

def subchar(a, b):
    return (((ord(b)-97) - (ord(a)-97)) % 26) + 97

def getkey(question, answer):
    assert len(question) == len(answer), 'Length mismatch'
    q = question.lower()
    a = answer.lower()
    result = []
    for i in range(len(question)):
        if question[i] == ' ':
            char = ' '
        else:
            char = chr(subchar(q[i], a[i]))
            # if uppercase
            if ord(question[i]) < 97:
                char = char.upper()
        result.append(char)
    return ''.join(result)

one = 'rstoner leet hax omg'
two = 'Ccoheal ieuw qwu tcb'

getkey(one, two)
