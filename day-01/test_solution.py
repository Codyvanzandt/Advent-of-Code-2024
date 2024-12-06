from solution import solve_part_1

def test_nothing():
    assert True

def test_solve_part_1_simple_case():
    test_input = """1 4
2 5
3 6"""
    assert solve_part_1(test_input) == 9  # |1-4| + |2-5| + |3-6| = 3 + 3 + 3 = 9
