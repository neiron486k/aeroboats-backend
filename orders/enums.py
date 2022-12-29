from enum import IntEnum


class Status(IntEnum):
    NEW = 1
    PAID = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
