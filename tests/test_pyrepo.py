from pyrepo import do_a_thing


def test_something():
    assert do_a_thing() is True


def test_qt(qtbot):
    from qtpy.QtWidgets import QWidget

    widget = QWidget()
    qtbot.addWidget(widget)

    widget.show()
    assert widget.isVisible()
