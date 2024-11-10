from concreteuserstatus import ConcreteUserStatus
from concreteobservers import UIComponent, NotificationSystem, AdminDashboard


def main():
    #utworzenie obiektu podmiotu
    user_status = ConcreteUserStatus()

    #obiekty obserwatorów
    ui_component = UIComponent()
    notification_system = NotificationSystem()
    admin_dashboard = AdminDashboard()

    #dodanie obserwatorów do podmiotu
    user_status.attach(ui_component)
    user_status.attach(notification_system)
    user_status.attach(admin_dashboard)

    #zmiana statusu użytkownika
    user_status.change_status("online")
    user_status.change_status("away")
    user_status.change_status("offline")

    #usuwamy jednego z obserwatorów
    user_status.detach(admin_dashboard)

    #ponowna zmiana statusu
    user_status.change_status("busy")

if __name__ == '__main__':
    main()
