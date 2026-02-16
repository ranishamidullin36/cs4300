from src.task3 import totalSum, primeNums, pos_neg_zero

def test_for_pos_neg_zero():
    assert pos_neg_zero(0) == "zero"
    assert pos_neg_zero(10) == "positive"
    assert pos_neg_zero(-10) == "negative"

def test_totalSum():
    assert totalSum == 5050

def test_primeNums():
    assert len(primeNums) == 10
    assert primeNums == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

