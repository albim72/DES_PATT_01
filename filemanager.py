class Filemanager:
    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with Filemanager('test.txt','w','utf-8') as f:
    f.write("to jest pierwsza linia - kilka słów\n")

print(f.closed)

with open("abc.txt","w",encoding="utf-8") as g:
    g.write("abcąźż - alfabet polski....")

print(g.closed)


