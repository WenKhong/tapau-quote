from quote import landed_cost_myr, quote_order
from pathlib import Path
import subprocess
import sys
import pytest

HERE = Path(__file__).parent
SAMPLE_CSV = HERE / "tests" / "sample_order.csv"

def test_normal_case():
    assert landed_cost_myr(100, 10, 0.65, 0.2) == 90

def test_zero_margin_case():
    assert landed_cost_myr(100, 10, 0.65, 0) == 72

def test_bad_margin_case():
    with pytest.raises(ValueError, match="Margin percentage must be between 0 and 1."):
        landed_cost_myr(100, 10, 0.65, -0.1)

def test_bigger_margin_case():
    with pytest.raises(ValueError, match="Margin percentage must be between 0 and 1."):
        landed_cost_myr(100, 10, 0.65, 1.5)

def test_one_margin_case():
    with pytest.raises(ValueError, match="Margin percentage must be between 0 and 1."):
        landed_cost_myr(100, 10, 0.65, 1)

def test_zero_fx_rate_case():
    with pytest.raises(ValueError, match="Exchange rate must be greater than 0."):
        landed_cost_myr(100, 10, 0, 0.2)

def test_negative_price_case():
    with pytest.raises(ValueError, match="Price must be non-negative."):
        landed_cost_myr(-100, 10, 0.65, 0.2)

def test_zero_price_case():
    with pytest.raises(ValueError, match="Price cannot be zero."):
        landed_cost_myr(0, 10, 0.65, 0.2)

def test_big_order():
    assert landed_cost_myr(1000000, 10000, 0.65, 0.2) == 820625

def test_quote_order_from_csv():
    assert quote_order(SAMPLE_CSV) == [("Tee", 90), ("Socks", 72)]

def test_csv_cli_prints_items_and_total():
    result = subprocess.run(
        [sys.executable, str(HERE / "quote.py"), "--csv", str(SAMPLE_CSV)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert result.stdout == "Tee: RM90\nSocks: RM72\nOrder total: RM162\n"
