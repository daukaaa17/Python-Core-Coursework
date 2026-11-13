class Cipher():
    def __init__(self, word):
        self.word = word[::-1].upper()
    def encode(self, data):
        a = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        a1 = a.split()
        b1 = a.split()
        c = ''
        for i in range(len(self.word)):
            for item in b1:
                if self.word[i] == item:
                    b1.remove(item)
            b1.insert(0, self.word[i])

        x = [k for k, ltr in enumerate(data) if ltr == ' ']
        for i in range(len(data)):
            for item in a1:
                if data[i].isupper() and data[i] == item:
                    c = c + b1[a1.index(item)]
                elif data[i].islower() and data[i].upper() == item:
                    c = c + b1[a1.index(item)].lower()
        for i in range(len(x)):
            temp = c[:(x[i])] + " " + c[(x[i]):]
            c = temp
        return c
    def decode(self, data):
        a = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        a1 = a.split()
        b1 = a.split()
        c = ''
        for i in range(len(self.word)):
            for item in b1:
                if self.word[i] == item:
                    b1.remove(item)
            b1.insert(0, self.word[i])

        x1 = [k for k, ltr in enumerate(data) if ltr == ' ']
        c1 = ''
        for i in range(len(data)):
            for item in b1:
                if data[i].isupper() and data[i] == item:
                    c1 = c1 + a1[b1.index(item)]
                elif data[i].islower() and data[i].upper() == item:
                    c1 = c1 + a1[b1.index(item)].lower()
        for i in range(len(x1)):
            temp1 = c1[:(x1[i])] + " " + c1[(x1[i]):]
            c1 = temp1
        return c1
cipher = Cipher('crypto')
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))


# a = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
# a1 = a.split()
# word = 'crypto'[::-1].upper()
# b1 = a.split()
# for i in range(len(word)):
#     for item in b1:
#         if word[i] == item:
#             b1.remove(item)
#     b1.insert(0,word[i])
#
# s = 'Kojima is genius'
# x = [k for k, ltr in enumerate(s) if ltr == ' ']
# c = ''
# for i in range(len(s)):
#     for item in a1:
#         if s[i].isupper() and s[i] == item:
#             c = c + b1[a1.index(item)]
#         elif s[i].islower() and s[i].upper() == item:
#             c = c + b1[a1.index(item)].lower()
# for i in range(len(x)):
#     temp = c[:(x[i])] + " " + c[(x[i]):]
#     c = temp
# print(c)
#
#
#
# s1 = "Fjedhc dn atidsn"
# x1 = [k for k, ltr in enumerate(s1) if ltr == ' ']
# print(x1)
# c1 = ''
# for i in range(len(s1)):
#     for item in b1:
#         if s1[i].isupper() and s1[i] == item:
#             c1 = c1 + a1[b1.index(item)]
#         elif s1[i].islower() and s1[i].upper() == item:
#             c1 = c1 + a1[b1.index(item)].lower()
# for i in range(len(x1)):
#     temp1 = c1[:(x1[i])] + " " + c1[(x1[i]):]
#     c1 = temp1
# print(temp1)









