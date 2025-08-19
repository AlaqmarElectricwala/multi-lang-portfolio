import pytest
from main import add_transaction, view_transaction, set_budget

# Fixture to capture print output
@pytest.fixture
def capsys(monkeypatch):
    from io import StringIO
    import sys
    capsys = StringIO()
    monkeypatch.setattr(sys, 'stdout', capsys)
    yield capsys
    sys.stdout = sys.__stdout__

# Test add_transaction with valid input
def test_add_transaction(monkeypatch, capsys):
    inputs = iter(["income", "salary", "100.0", "17-08-2025"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_transaction()
    captured = capsys.readouterr()
    assert "--TRANSACTION ADDED--" in captured.out

# Test view_transaction with valid data
def test_view_transaction(monkeypatch, capsys):
    # Mock a file with one transaction
    mock_data = "\n".join([",".join(["date", "type", "category", "amount"]), ",".join(["17-08-2025", "income", "salary", "100.0"])])
    monkeypatch.setattr('os.path.exists', lambda x: True)
    monkeypatch.setattr('builtins.open', lambda *args, **kwargs: mock_open(read_data=mock_data)())
    monkeypatch.setattr('builtins.input', lambda _: "1")
    view_transaction()
    captured = capsys.readouterr()
    assert "Date         Type        Category        Amount" in captured.out
    assert "17-08-2025  income      salary          100.0" in captured.out

# Test set_budget with valid input
def test_set_budget(monkeypatch, capsys):
    inputs = iter(["food", "200.0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    set_budget()
    captured = capsys.readouterr()
    assert "--BUDGET SET--" in captured.out
