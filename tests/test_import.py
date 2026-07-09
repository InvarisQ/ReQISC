import invaris_reqisc


def test_import_has_version() -> None:
    assert invaris_reqisc.__version__ == "0.1.0"
