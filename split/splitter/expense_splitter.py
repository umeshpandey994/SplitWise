from split.splitter.split import SplitStrategy


class ExpenseSplitter:
    def __init__(
        self, expense, users, total_amount, split_strategy: SplitStrategy, amounts
    ):
        self.expense = expense
        self.users = users
        self.total_amount = total_amount
        self.split_strategy = split_strategy
        self.amounts = amounts or []

    def split(self):
        return self.split_strategy.split(self.users, self.total_amount, self.amounts)
