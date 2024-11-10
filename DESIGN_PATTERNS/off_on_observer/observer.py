from abc import ABC, abstractmethod
from userstatus import UserState

class Observer(ABC):
    @abstractmethod
    def update(self,subject:UserState) -> None:
        pass
