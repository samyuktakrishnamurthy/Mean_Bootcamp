from mean import *
#fid is intended to be a list of functions you might want to use to test mean

def test_ints():
    num = [4, 3, 6]
    obs = mean(num)
    exp = 4
    assert obs == exp

def test_zero():
    num = [4, 0, 6]
    obs = mean(num)
    exp = 3
    assert obs == exp
    
def test_neg():
    num = [4, -3, 5]
    obs = mean(num)
    exp = 2
    assert obs == exp
    
