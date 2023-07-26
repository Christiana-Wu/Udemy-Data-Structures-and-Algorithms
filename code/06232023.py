language = 'python'
new_list = [letter for letter in language]
print(new_list)


def set_value(a, l):
    a = 0
    l[0]=0
    # l=[0]*3

a = 100
l=[100]*3
set_value(a,l)
print(a, l)
