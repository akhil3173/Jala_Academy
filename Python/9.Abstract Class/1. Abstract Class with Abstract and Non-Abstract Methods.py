from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def non_abstract_method(self):
        print("Non-abstract method called")

    @abstractmethod
    def abstract_method(self):
        pass
