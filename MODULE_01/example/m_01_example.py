# from abc import ABC, abstractmethod


# class Creator(ABC):
#     @abstractmethod
#     def create(self):
#         pass

#     def send_messages(self) -> str:
#         product = self.create()
#         result = product.sending()
#         return result


# class SendingMessages(ABC):
#     @abstractmethod
#     def sending(self) -> str:
#         pass


# class CreatorPush(Creator):
#     def create(self) -> SendingMessages:
#         return SendingPushMessages()


# class CreatorSMS(Creator):
#     def create(self) -> SendingMessages:
#         return SendingSMSMessages()


# class SendingPushMessages(SendingMessages):
#     def sending(self) -> str:
#         return "Push mailing has been completed"


# class SendingSMSMessages(SendingMessages):
#     def sending(self) -> str:
#         return "SMS mailing has been completed"


# def client_code(creator: Creator) -> None:
#     print("We know nothing about the creator code that works")
#     result = creator.send_messages()
#     print(f"Result: {result}")


# if __name__ == "__main__":
#     print("The application performs Push mailing lists.")
#     client_code(CreatorPush())
#     print("\n")

#     print("The application performs SMS mailing.")
#     client_code(CreatorSMS())


import random


class Singleton:
    """Classic singleton"""

    __instance = None

    def __init__(self):
        self.number = random.randint(1, 10)

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Singleton)
        return cls.__instance


class Regular:
    """Simple class to compare behavior"""

    def __init__(self, *args, **kwargs):
        self.number = random.randint(1, 10)


def testing():
    print("Singleton instances")
    list_singleton = [Singleton() for i in range(0, 5)]
    for index, element in enumerate(list_singleton):
        print(f"Element: {index}  number : {element.number}")

    print("Instances of a regular class")
    list_regular = [Regular() for i in range(0, 5)]
    for index, element in enumerate(list_regular):
        print(f"Element: {index}  number : {element.number}")


if __name__ == "__main__":
    testing()