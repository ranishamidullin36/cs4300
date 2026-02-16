from src.task6 import word_counter

def test_word_counter():
    result = word_counter('task6_read_me.txt')
    assert result > 0
    assert isinstance(result, int)
    assert word_counter('task6_read_me.txt') == 104

    