from quote import landed_cost_myr
import pytest

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