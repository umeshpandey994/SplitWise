from split.splitter.split import SplitStrategy


class ExpenseSplitter:
    def __init__(
        self,
        users,
        total_amount,
        amounts,
        split_strategy: SplitStrategy,
    ):
        self.users = users
        self.total_amount = total_amount
        self.split_strategy = split_strategy
        self.amounts = amounts or []

    def split(self):
        return self.split_strategy.split(self.users, self.total_amount, self.amounts)
