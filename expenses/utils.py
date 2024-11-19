from split.splitter.equal_split import EqualSplit
from split.splitter.expense_splitter import ExpenseSplitter
from split.splitter.fixed_split import FixedSplit
from split.splitter.percentage_split import PercentageSplit


def calculate_split(expense, users, split_type, amounts):
    total_amount = expense.total_amount
    split_method_map = {
        "equal": EqualSplit,
        "fixed": FixedSplit,
        "percentage": PercentageSplit,
    }

    splitter = ExpenseSplitter(
        users,
        total_amount,
        amounts,
        split_method_map.get(split_type)(),
    )
    return splitter.split()
