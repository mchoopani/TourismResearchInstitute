from abc import ABC, abstractmethod
from typing import List


class Dictable:
    @abstractmethod
    def to_dict(self):
        pass


class Utils:

    @staticmethod
    def serialize_array(arr: List[Dictable]) -> List[dict]:
        return [element.to_dict() for element in arr]

