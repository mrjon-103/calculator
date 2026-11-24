from batch_calculator import process_calculation


def test_batch_correct():
    assert process_calculation("subtract", "6", "3") == ("OK", "3", "")

def test_batch_on_error():
    assert process_calculation("divisio", "6", "2") == ("ERROR", "", "UNKNOWN_OPERATION")
    