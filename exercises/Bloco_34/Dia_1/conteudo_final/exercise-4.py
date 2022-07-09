from abc import ABC, abstractmethod
from datetime import datetime


class ManipuladorDeLog(ABC):
    @classmethod
    @abstractmethod
    def log(cls, msg):
        raise NotImplementedError


class LogEmArquivo(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        with open('text.txt', 'a') as file:
            print(msg, file=file)


class LogEmTela(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        print(msg)


class Log:
    def __init__(self, manipulators):
        self.__manipulators = set(manipulators)

    def add_manipulators(self, manipulator):
        self.manipulators.add(manipulator)

    def info(self, msg):
        self.__log('INFO', msg)

    def alerta(self, msg):
        self.__log('ALERTA', msg)

    def erro(self, msg):
        self.__log('ERRO', msg)

    def debug(self, msg):
        self.__log('DEBUG', msg)

    def __log(self, nivel, msg):
        for manipulator in self.__manipulators:
            manipulator.log(self.__formatar(nivel, msg))

    def __formatar(self, nivel, msg):
        formated_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return f"[{nivel} - {formated_date_time}]: {msg}"
