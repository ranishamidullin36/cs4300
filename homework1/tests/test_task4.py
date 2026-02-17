from src.task4 import calculate_discount

# test if the logic can properly calculate the total discount
def test_calculate_discount():
    assert calculate_discount(100, 50) == 50
    assert calculate_discount(65, 50) == 32.5
    assert calculate_discount(38, 20) == 30.40