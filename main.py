import pathlib
path = pathlib.Path('elemnts.txt')
print(path.exists())
print(path.is_file())
def namer(mstr, age):
    print('In the  table, this element has the following number and name: ' + mstr + str(age) + ',')

if __name__ == '__main__':
    mstr = input("Enter element")
    age = float(input("His name or number elements"))
    namer(mstr, age)
