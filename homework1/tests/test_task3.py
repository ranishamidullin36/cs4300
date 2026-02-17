from src.task3 import totalSum, primeNums, pos_neg_zero

# test the function can tell what number it is
def test_for_pos_neg_zero():
    assert pos_neg_zero(0) == "zero"
    assert pos_neg_zero(10) == "positive"
    assert pos_neg_zero(-10) == "negative"

# test is the sum does add up to 5050
def test_totalSum():
    assert totalSum == 5050

# test if the prime numbers allign with the logic
def test_primeNums():
    assert len(primeNums) == 10
    assert primeNums == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

