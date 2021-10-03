abc = 'abcdefghijklmnopqrstuvwxyz'
ABC= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
txt = input('enter the text it will be encrypted by the length of the word').split()
string=''
for e in txt:
    step= len([i for i in e if i.isalpha()])
    for c in e:
        if c in abc:
            string+=abc[(abc.find(c)+step)%26]
        elif c in ABC:
            string+=ABC[(ABC.find(c)+step)%26]
        else:
            string+=c
    string+=' '
print(string,end='')


