#subsequent duplicate words removed
#Return string
def no_dups(s):
    #Your code here
    words = s.split()
    dict_w = {}
    for word in words:
        dict_w[word] = 1
    string = ""
    for key in dict_w:
        string = string + " " + key
    return string.strip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))