from abc import ABCMeta, abstractmethod
import urllib.request
import urllib.parse

#abstrakcja i rozszerzona abstrakcja
class ResourceContent:
    def __init__(self,imp):
        self._imp = imp

    def show_content(self,path):
        self._imp.fetch(path)from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self,observer:Observer) -> None:
        pass

    @abstractmethod
    def detach(self,observer:Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass



class ConcreteSubject(Subject):
    _state:int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer!")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self)->None:
        print("\nSubject: I'm doing something important!")
        self._state = randrange(0,10)
        print(f"Subject: My state just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self,subject:Subject) -> None:
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state>=2:
            print("ConcreteObserverB: Reacted to the event")

if __name__ == '__main__':
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)
    subject.some_business_logic()

class ResourceContentFetcher(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self,path):
        pass


#konkretna implementacja
class URLFetcher(ResourceContentFetcher):
    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                this_page = response.read()
                print(this_page)

class LocalFileFetcher(ResourceContentFetcher):
    def fetch(self, path):
        with open(path,encoding='utf-8') as f:
            print(f.read())

def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')

    print("_"*60)

    local_fetcher = LocalFileFetcher()
    iface = ResourceContent(local_fetcher)
    iface.show_content('info.txt')

if __name__ == '__main__':
    main()
