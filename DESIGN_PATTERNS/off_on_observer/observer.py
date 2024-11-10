from abc import ABC, abstractmethod
from userstatus import UserState

class Observer(ABC):
    @abstractmethod
    def upadate(self,subject:UserState) -> None:
        pass
