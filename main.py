import random
def toBinary(a):
    m = bin(a)
    return m
class HamCode():
    def __init__(self, list):
        self.d = len(list[0])
        self.p = 0
        self.list = list
        self.pList = []
        while self.d + self.p > 2 ** self.p:
            self.p += 1
        for i in range(self.p):
            self.pList.append((self.p + self.d) - 2**i)
    def encode(self):
        list = []
        for i in self.list:
            code = ""
            count = self.p-1
            for x in i:
                code += x
                while len(code) == ((self.p + self.d)-(2**count)):
                    code += " "
                    count -= 1
            list.append(code)
        self.list = list
        for i in range(len(self.list)):
            for x in range(len(self.pList)):
                value = 0
                for y in range(len(self.list[i])):
                    binary = bin(y+1)[2:]
                    binary = "0"*(self.p-len(binary))+binary
                    if binary[len(binary)-x-1] == "1" and len(self.list[i])-y-1 != self.pList[x]:
                        if self.list[i][len(self.list[i])-y-1] == "1":
                            value += 1
                code = ""
                for y in range(len(self.list[i])):
                    if y == self.pList[x]:
                        if value%2 == 1:
                            code += "1"
                        else:
                            code += "0"
                    else:
                        code += self.list[i][y]
                self.list[i] = code

        return self.list
    def decode(self, str):
        received = ""
        sent = ""
        for i in range(len(self.pList)):
            value = 0
            sent += str[self.pList[i]]
            binary1 = bin(len(str) - self.pList[i])[2:]
            binary1 = "0" * (self.p - len(binary1))+binary1
            for x in range(1, len(str)+1):
                binary = bin(x)[2:]
                binary = "0" * (self.p - len(binary)) + binary
                if binary[self.p-i-1] == "1" and binary1 != binary:
                    if str[len(str)-x] == "1":
                        value += 1
            if value%2 == 1:
                received = received + "1"
            else:
                received = received + "0"
        if sent != received:
            value = 0
            for i in range(self.p):
                if received[i] != sent[i]:
                    value +=2**(i)
            string = ""
            for v in range(len(str)):
                if len(str)-value == v:
                    if str[v] == "1":
                        string += "0"
                    else:
                        string += "1"
                else:
                    string += str[v]
            str = string
        count = self.p-1
        binary = ""
        for i in range(len(str)):
            if i != self.pList[count]:
                binary += str[i]
            else:
                count -= 1
        return binary
    def decodeL(self):
        for i in range(len(self.list)):
            string = self.decode(self.list[i])
            self.list[i] = string
        return self.list
str = "01010000 01110010 01100001 01101001 01110011 01100101 00100000 01110100 01101000 01100101 00100000 01001100 01101111 01110010 01100100 00101100 00100000 01100001 01101100 01101100 00100000 01111001 01101111 01110101 00100000 01101110 01100001 01110100 01101001 01101111 01101110 01110011 00111011 00100000 01100101 01111000 01110100 01101111 01101100 00100000 01101000 01101001 01101101 00101100 00100000 01100001 01101100 01101100 00100000 01111001 01101111 01110101 00100000 01110000 01100101 01101111 01110000 01101100 01100101 01110011 00101110 00100000 01000110 01101111 01110010 00100000 01100111 01110010 01100101 01100001 01110100 00100000 01101001 01110011 00100000 01101000 01101001 01110011 00100000 01101100 01101111 01110110 01100101 00100000 01110100 01101111 01110111 01100001 01110010 01100100 00100000 01110101 01110011 00101100 00100000 01100001 01101110 01100100 00100000 01110100 01101000 01100101 00100000 01100110 01100001 01101001 01110100 01101000 01100110 01110101 01101100 01101110 01100101 01110011 01110011 00100000 01101111 01100110 00100000 01110100 01101000 01100101 00100000 01001100 01101111 01110010 01100100 00100000 01100101 01101110 01100100 01110101 01110010 01100101 01110011 00100000 01100110 01101111 01110010 01100101 01110110 01100101 01110010 00101110 00100000 01010000 01110010 01100001 01101001 01110011 01100101 00100000 01110100 01101000 01100101 00100000 01001100 01101111 01110010 01100100 00101110"

def strL(str):
    string = ""
    list = []
    for i in str:
        if i == " ":
            list.append(string)
            string = ""
        else:
            string += i
    if len(string) != 0:
        list.append(string)
    return list
def ranCor(str):
    rand = random.randint(0, len(str) - 1)
    rand2 = random.randint(0, len(str) - 1)
    string = ""
    for y in range(len(str)):
        if rand == y or rand2 == y:
            if str[y] == "1":
                string += "0"
            else:
                string += "1"
        else:
            string += str[y]
    return string
list = strL(str)
hello = HamCode(list)
print(hello.encode())
for i in range(len(hello.list)):
    hello.list[i] = ranCor(hello.list[i])
print(hello.list)
hello.decodeL()
print(hello.list)
string = ""
for i in range(len(hello.list)):
    string+= hello.list[i]+" "
print(string)