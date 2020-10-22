# Donovan Stark-drs474@nau.edu and Taya Patnoe-
# The art for each letter is stored as a list of lists
# Each list is one line of the letter
# 5 lines total per letter with 3 characters per line
# Includes a space
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

# The variables are then assigned a key
# The key is just the string of the letter

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


# Stores the inputed word as a list of lists
# List of lists represents the word as ASCII art
def letter_to_ASCII(word):
    word = word.lower()
    ASCII = []
    for i in range(len(word)):
        ASCII += [ASCII_dict[str(word[i])]]
    return ASCII


# Prints each line one by one for the whole word
# Starts at the top and prints the 5 lines
def print_horizontal(word):
    line = ''
    for i in range(5):
        for c in range(len(word)):
            line += word[c][i] + ' '
        print(line)
        line = ''


# Prints the 5 lines for each letter one at a time
# With a space between each letter
def print_vertical(word):
    for i in range(len(word)):
        for c in range(5):
            print(word[i][c])
        print('   ')


# Main function that interprets user input
# Then runs the correct functions based on input
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
