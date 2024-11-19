from typing import List

from split.splitter.split import SplitStrategy


class EqualSplit(SplitStrategy):
    def split(self, users: List[int], total_amount: float, amounts=None):
        per_user = total_amount / len(users)
        splits = {}
        for user in users:
            splits.update({user: per_user})
        return splits
