from unittest.mock import MagicMock, patch

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def mock_user():
    user = MagicMock()
    user.id = 1
    user.username = "test_user"
    return user


@pytest.mark.django_db
@patch("expenses.models.Expenses")
@patch("split.models.Split")
def test_list_expenses(mock_split, mock_expenses, api_client, mock_user):
    expense1 = MagicMock(id=1, title="Expense 1", total_amount=500.0, paid_by=mock_user)
    expense2 = MagicMock(
        id=2,
        title="Expense 2",
        total_amount=300.0,
        paid_by=MagicMock(username="other_user"),
    )

    mock_expenses.objects.all.return_value = [expense1, expense2]

    split1 = MagicMock(expense=expense1, user=mock_user, owes=250.0)
    split2 = MagicMock(expense=expense2, user=mock_user, owes=150.0)
    mock_split.objects.filter.return_value = [split1, split2]

    api_client.force_authenticate(user=mock_user)
    response = api_client.get("/api/v1/expenses/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "paid_by": "Paid by you",
            "title": "Expense 1",
            "total_amount": 500.0,
            "total_owed": 0.0,
            "total_receivable": 250.0,
        },
        {
            "paid_by": "other_user",
            "title": "Expense 2",
            "total_amount": 300.0,
            "total_owed": 150.0,
            "total_receivable": 0.0,
        },
    ]


@pytest.mark.django_db
@patch("expenses.models.Expenses")
@patch("split.models.Split")
def test_get_user_outstanding_balance(mock_split, mock_expenses, api_client, mock_user):
    # Mock data
    expense1 = MagicMock(id=1, title="Expense 1", total_amount=500.0, paid_by=mock_user)
    expense2 = MagicMock(
        id=2,
        title="Expense 2",
        total_amount=300.0,
        paid_by=MagicMock(username="other_user"),
    )

    mock_expenses.objects.all.return_value = [expense1, expense2]

    split1 = MagicMock(expense=expense1, user=mock_user, owes=250.0)
    split2 = MagicMock(expense=expense2, user=mock_user, owes=150.0)
    mock_split.objects.filter.side_effect = (
        lambda **kwargs: [split1] if kwargs["expense"] == expense1 else [split2]
    )
    api_client.force_authenticate(user=mock_user)
    response = api_client.get("/api/v1/expenses/user-outstanding/")

    assert response.status_code == 200
    assert response.json() == {
        "user": "test_user",
        "total_outstanding": 100.0,
        "breakdown": [
            {
                "expense_id": 1,
                "title": "Expense 1",
                "paid_by": "Paid by you",
                "total_amount": 500.0,
                "total_owes": 0.0,
                "total_receivable": 250.0,
            },
            {
                "expense_id": 2,
                "title": "Expense 2",
                "paid_by": "other_user",
                "total_amount": 300.0,
                "total_owes": 150.0,
                "total_receivable": 0,
            },
        ],
    }
