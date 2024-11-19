from split.splitter.split import SplitStrategy


class PercentageSplit(SplitStrategy):
    def split(self, users, total_amount, amounts=None):
        if not amounts or sum(amounts) != 100:
            raise ValueError("The sum of percentages must be 100.")

        splits = []
        for user, percent in zip(users, amounts):
            owes = (percent / 100) * total_amount
            splits.append({user: owes})
        return splits
