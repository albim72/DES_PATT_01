class Memento:
    def __init__(self,file,content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self,file):
        self.file = file
        self.content = ""

    def write(self,string):
        self.content += string

    def save(self):
        return Memento(self.file,self.content)

    def undo(self,memento):
        self.content = memento.content

class FileWriterCaretaker:
    def save(self,writer):
        self.obj = writer.save()

    def undo(self,writer):
        writer.undo(self.obj)

if __name__ == '__main__':
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("info.txt")
    writer.write("Pierwsza odsłona pliku info.txt\n")

    print(writer.content + "\n")
    caretaker.save(writer)
    
    writer.write("Druga wersja tekstu... \n")
    print(writer.content + "\n")

    caretaker.undo(writer)
    print(writer.content + "\n")
