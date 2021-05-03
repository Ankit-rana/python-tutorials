# Factory is a structural Python design pattern aimed at creating 
# new objects, hiding the instantiation logic from the user. But 
# creation of objects in Python is dynamic by design, so additions 
# like Factory are not necessary. Of course, you are free to implement 
# it if you want to. There might be cases where it would be really 
# useful, but they’re an exception, not the norm.
# we also use when we want to close classes for modification

# from wikipedia
from abc import ABC, abstractmethod
from sys import platform


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

    def factory(self, platform):
        if platform == "linux":
            factory = LinuxButton
        elif platform == "darwin":
            factory = MacOSButton
        elif platform == "win32":
            factory = WindowsButton
        else:
            raise NotImplementedError(
                f'Not implemented for your platform: {platform}'
                )

class LinuxButton(Button):
    def paint(self):
        return 'Render a button in a Linux style'


class WindowsButton(Button):

    def paint(self):
        return 'Render a button in a Windows style'


class MacOSButton(Button):

    def paint(self):
        return 'Render a button in a MacOS style'

platform = 'darwin'
button = Button.factory(platform)
result = button.paint()
print(result)

# but suppose you want to close button and its sub-hierarchies 
# for modification. then take out only variable logic from the 
# button class

def factory(platform):
    if platform == "linux":
        factory = LinuxButton
    elif platform == "darwin":
        factory = MacOSButton
    elif platform == "win32":
        factory = WindowsButton
    else:
        raise NotImplementedError(
            f'Not implemented for your platform: {platform}'
            )
