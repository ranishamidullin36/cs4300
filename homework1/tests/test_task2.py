from src.task2 import myInt, myFloat, myStr, myBool

# test to make sure each variable is a type of a specific instance
def test_for_task2():
    assert isinstance(myInt, int)
    assert isinstance(myFloat, float)
    assert isinstance(myStr, str)
    assert isinstance(myBool, bool)