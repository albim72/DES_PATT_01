from userstatus import UserState

class ConcreteUserStatus(UserState):
    _status:str = "offline"
    _observers = []

    def attach(self, observer) -> None:
        print(f"UserStatus: dodano obserwatora {observer.__class__.__name__}")
        self._observers.append(observer)

    def detach(self, observer) -> None:
        print(f"UserStatus: usunięto obserwatora {observer.__class__.__name__}")
        self._observers.remove(observer)

    def notify(self) -> None:
        print("UserStatus: Żaden obserwator nie odbiera zmian statusu....")
        for observer in self._observers:
            observer.update(self)

    def change_status(self,status:str) -> None:
        print(f"\nUserStatus: Zamiana statusu -> {status}")
        self._status = status
        self.notify()
    
    def get_status(self) -> str:
        return self._status
