from app import change


def test_change():
    assert [{5: 'quarters'}] == change(1.25)
