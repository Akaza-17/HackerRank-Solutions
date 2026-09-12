import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    width= 4*size - 3
    lines = []
    for i in range(size):
        chars= [alpha[size-j-1] for j in range(i+1)]
        row_letters = chars + chars [:-1][::-1]
        row_string="-".join(row_letters).center(width,'-')
        lines.append(row_string)
        
    print('\n'.join(lines+lines[:-1][::-1]))
    # your code goes here

