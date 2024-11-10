from observer import Observer
from userstatus import UserState

class UIComponent(Observer):
    def update(self, subject: UserState) -> None:
        print(f"UIComponent: Status użytkownika zmieniony na {subject.get_status()}. Zmiana w UI...")

class NotificationSystem(Observer):
    def update(self, subject: UserState) -> None:
        print(f"NotificationSystem: przesłanie notyfikacji o zmianie statusu na {subject.get_status()}")

class AdminDashboard(Observer):
    def update(self, subject: UserState) -> None:
        print(f"AdminDashboard: Notyfikacja admina o zmianie statusu {subject.get_status()}")
