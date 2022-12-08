import pytest

from example_pkg import ExampleClass, example_function


@pytest.mark.fast
def test_example_cls_fast():
    """Example test to be replaced with real ones."""
    cls = ExampleClass()

    actual = cls.example_method()
    expected = True

    assert actual == expected


@pytest.mark.fast
def test_example_fn_fast():
    """Example test to be replaced with real ones."""
    actual = example_function()
    expected = True

    assert actual == expected


@pytest.mark.slow
def test_example_slow():
    raise NotImplementedError("Don't run slow tests marked as slow on CI")
