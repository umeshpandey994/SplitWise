from split.splitter.split import SplitStrategy


class FixedSplit(SplitStrategy):
    def split(self, users, total_amount, amounts=None):
        if not amounts or len(amounts) != len(users):
            raise ValueError(
                "Fixed amounts are required and must match the number of users."
            )

        if total_amount != sum(amounts):
            raise ValueError(
                f"The sum of split amounts ({sum(amounts)}) does not match the total expense amount ({total_amount}). "
                "Please ensure the fixed amounts provided add up to the total expense."
            )
        splits = []
        for user, amount in zip(users, amounts):
            splits.append({user: amount})
        return splits
