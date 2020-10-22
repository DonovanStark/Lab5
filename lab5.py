# Donovan Stark-drs474@nau.edu and Taya Patnoe-
a = [' # ', '# #', '###', '# #', '# #']
b = ['## ', '# #', '## ', '# #', '## ']
c = [' ##', '#  ', '#  ', '#  ', ' ##']
d = ['## ', '# #', '# #', '# #', '## ']
e = ['###', '#  ', '## ', '#  ', '###']
f = ['###', '#  ', '## ', '#  ', '#  ']
g = [' ##', '#  ', '# #', '# #', ' ##']
h = ['# #', '# #', '###', '# #', '# #']
i = ['###', ' # ', ' # ', ' # ', '###']
j = [' ##', '  #', '  #', '# #', ' # ']
k = ['# #', '# #', '## ', '# #', '# #']
L = ['#  ', '#  ', '#  ', '#  ', '###']
m = ['# #', '###', '###', '# #', '# #']
n = ['###', '# #', '# #', '# #', '# #']
o = [' # ', '# #', '# #', '# #', ' # ']
p = ['## ', '# #', '## ', '#  ', '#  ']
q = [' # ', '# #', '# #', ' ##', '  #']
r = ['## ', '# #', '## ', '# #', '# #']
s = [' ##', '#  ', ' # ', '  #', '## ']
t = ['###', ' # ', ' # ', ' # ', ' # ']
u = ['# #', '# #', '# #', '# #', '###']
v = ['# #', '# #', '# #', '# #', ' # ']
w = ['# #', '# #', '###', '###', '# #']
x = ['# #', '# #', ' # ', '# #', '# #']
y = ['# #', '# #', ' # ', ' # ', ' # ']
z = ['###', '  #', ' # ', '#  ', '###']
sp = ['   ', '   ', '   ', '   ', '   ']
ASCII_dict = {
    'a': a,
    'b': b,
    'c': c,
    'd': d,
    'e': e,
    'f': f,
    'g': g,
    'h': h,
    'i': i,
    'j': j,
    'k': k,
    'l': L,
    'm': m,
    'n': n,
    'o': o,
    'p': p,
    'q': q,
    'r': r,
    's': s,
    't': t,
    'u': u,
    'v': v,
    'w': w,
    'x': x,
    'y': y,
    'z': z,
    ' ': sp
}


def letter_to_ASCII(word):
    word = word.lower()
    ASCII = []
    for i in range(len(word)):
        ASCII += [ASCII_dict[str(word[i])]]
    return ASCII


def print_horizontal(word):
    line = ''
    for i in range(5):
        for c in range(len(word)):
            line += word[c][i] + ' '
        print(line)
        line = ''


def print_vertical(word):
    for i in range(len(word)):
        for c in range(5):
            print(word[i][c])
        print('   ')


def main():
    inpt = input('Word: ')
    ASCII = letter_to_ASCII(inpt)
    orientation = input('Vertical(v) or Horizontal(h)?: ').lower()
    if orientation == 'v' or orientation == 'vertical':
        print_vertical(ASCII)
    elif orientation == 'h' or orientation == 'horizontal':
        print_horizontal(ASCII)
    else:
        print('Try Again')


main()
