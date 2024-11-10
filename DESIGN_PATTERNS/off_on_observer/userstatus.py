from abc import ABC, abstractmethod

class UserState(ABC):
    @abstractmethod
    def attach(self,observer) -> None:
        pass
    
    @abstractmethod
    def detach(self,observer) -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass
