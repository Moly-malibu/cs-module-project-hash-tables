#re.sub(pattern, repl, string[, count, flags])
#Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; if it is a string, any backslash escapes in it are processed. That is, \n is converted to a single newline character, \r is converted to a linefeed, and so forth. Unknown escapes such as \j are left alone. Backreferences, such as \6, are replaced with the substring matched by group 6 in the pattern. For example:
#re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\)
#https://docs.python.org/3.1/library/re.html
import re

def word_count(s):
    s = s.lower()
    s = re.sub('[^a-z\ \']+', " ", s)
    words = s.split()
    word_count = {} #Dictionary
    word_group = set(words)
    for word in word_group:
        word_count[word] = words.count(word)
    return word_count
    
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))