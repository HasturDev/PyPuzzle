import os, pathlib
import pytest

os.chdir(pathlib.Path.cwd() / 'beginner_tests')

pytest.main()

def starter_test(x):
    assert x == 4
    assert x != 5
    assert x == 5