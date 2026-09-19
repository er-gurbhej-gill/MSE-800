from abc import ABC, abstractmethod


# abstract button
class button(ABC):

    @abstractmethod
    def click(self):
        pass


# abstract checkbox
class checkbox(ABC):

    @abstractmethod
    def check(self):
        pass


# windows products
class windows_button(button):

    def click(self):
        print("windows_button_clicked")


class windows_checkbox(checkbox):

    def check(self):
        print("windows_checkbox_checked")


# mac products
class mac_button(button):

    def click(self):
        print("mac_button_clicked")


class mac_checkbox(checkbox):

    def check(self):
        print("mac_checkbox_checked")


# linux products
class linux_button(button):

    def click(self):
        print("linux_button_clicked")


class linux_checkbox(checkbox):

    def check(self):
        print("linux_checkbox_checked")


# abstract factory
class gui_factory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# windows factory
class windows_factory(gui_factory):

    def create_button(self):
        return windows_button()

    def create_checkbox(self):
        return windows_checkbox()


# mac factory
class mac_factory(gui_factory):

    def create_button(self):
        return mac_button()

    def create_checkbox(self):
        return mac_checkbox()


# linux factory
class linux_factory(gui_factory):

    def create_button(self):
        return linux_button()

    def create_checkbox(self):
        return linux_checkbox()


# client
def create_ui(factory):

    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.click()
    checkbox.check()


# windows ui
print("windows_ui:")
create_ui(windows_factory())

# mac ui
print("\nmac_ui:")
create_ui(mac_factory())

# linux ui
print("\nlinux_ui:")
create_ui(linux_factory())