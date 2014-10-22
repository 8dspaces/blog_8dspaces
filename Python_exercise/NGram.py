class NGram(object):
    def __init__(self, text, n=3):
        self.length = None
        self.n = n
        self.table = {}
        self.parse_text(text)
 
    def parse_text(self, text):
        chars = ' ' * self.n # initial sequence of spaces with length n
 
        for letter in (" ".join(text.split()) + " "):
            chars = chars[1:] + letter # append letter to sequence of length n
            self.table[chars] = self.table.get(chars, 0) + 1 # increment count
            
my_text = "This is a simple testing for NGram" 
ng = NGram(my_text)
for x in ng.table:
    print "%s: %d" % (x, ng.table[x])