from typing import List


def calculate_split(expense, users, split_type, amounts):
    total_amount = expense.total_amount
    user_count = len(users)
    split_data = {}

    if split_type == "equal":
        amount_per_user = total_amount / user_count
        split_data = {user_id: amount_per_user for user_id in users}

    elif split_type == "fixed":
        if len(amounts) != user_count:
            raise ValueError("Number of fixed amounts must match the number of users.")
        split_data = {users[i]: amounts[i] for i in range(user_count)}

    elif split_type == "percentage":
        total_percentage = sum(amounts)
        if total_percentage != 100:
            raise ValueError("The sum of percentages must be 100.")
        split_data = {
            users[i]: (total_amount * amounts[i] / 100) for i in range(user_count)
        }

    return split_data
