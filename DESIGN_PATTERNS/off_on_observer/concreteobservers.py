from observer import Observer
from userstatus import UserState

class UIComponent(Observer):
    def upadate(self, subject: UserState) -> None:
        print(f"UIComponent: Status użytkownika zmieniony na {subject.get_status()}. Zmiana w UI...")
        
class NotificationSystem(Observer):
    def upadate(self, subject: UserState) -> None:
        print(f"NotificationSystem: przesłanie notyfikacji o zmianie statusu na {subject.get_status()}")
        
class AdminDashboard(Observer):
    def upadate(self, subject: UserState) -> None:
        print(f"AdminDashboard: Notyfikacja admina o zmianie statusu {subject.get_status()}")
