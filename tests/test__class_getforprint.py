from utils.class_getforprint import GetForPrint


def test__len_getjson():
    f = GetForPrint(5)
    assert len(f.get_true_file()) == 5

