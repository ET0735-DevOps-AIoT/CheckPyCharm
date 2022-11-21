#############################################
# -- Python script to test PyTest setup -- #
#############################################
import main


def test_dummy_func():
    assert(main.dummy_func(84, 6) == 90)