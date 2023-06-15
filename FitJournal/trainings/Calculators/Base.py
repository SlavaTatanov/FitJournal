from abc import ABC, abstractmethod


class Calculator(ABC):
    """
    Абстрактный базовый класс которые должны наследовать все калькуляторы
    """
    @abstractmethod
    def calculate(self):
        pass


class Dispatcher(ABC):
    """
    Абстрактный класс который является основой для классов диспетчеров
    """
    @abstractmethod
    def get(self):
        pass
