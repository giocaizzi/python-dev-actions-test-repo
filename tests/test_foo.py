from test_package_root.foo import Foo


def test_foo():
    f = Foo(2, 3)
    assert f.add() == 5
