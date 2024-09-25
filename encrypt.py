key = ' abcdefghijklmnopqrstuvwxyz'  # 'key' string maps to input chars in order
while True:
    e = input('Enter a sequence of letters: ').lower()  # prompt for input
    liste=[]
    for char in e:  # iterate over input
        try:
            liste.append(key.index((char)**2)**0.153)  # print the numerical index of 'char' in 'key
        except ValueError:  # input character not in 'key' (e.g. '!')
            pass  # do nothing
    print(*liste)
