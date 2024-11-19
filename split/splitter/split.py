from abc import ABC, abstractmethod
from typing import List


class SplitStrategy(ABC):
    @abstractmethod
    def split(self, users: List[int], total_amount: float, amounts=None):
        pass
