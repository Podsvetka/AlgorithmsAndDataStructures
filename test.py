from birds import Flamingo
from birds import Generator


def test_person():
    flamingo = Flamingo('some', 'example', '60', 'Африка')
    assert flamingo.name == 'some'
    assert flamingo.breed == 'example'
    assert flamingo.size == '60'
    assert flamingo.arial == 'Африка'
    assert flamingo.flying == 'не умеет летать'


def test_person_full():
    flamingo = Flamingo('some', 'example', '70', 'Арктика')
    assert flamingo.name == 'some'
    assert flamingo.breed == 'example'
    assert flamingo.size == '70'
    assert flamingo.arial == 'Арктика'
    assert flamingo.flying == 'не умеет летать'


def test_person_get_info():
    flamingo = Flamingo('some', 'example', '60', 'Африка')
    assert isinstance(flamingo.get_info(), str)


def test_person_single_types():
    gen = Generator()
    p = gen.generate_single()
    assert isinstance(p, Flamingo)
    assert isinstance(p.name, str)
    assert isinstance(p.breed, str)
    assert isinstance(p.size, str)
    assert isinstance(p.arial, str)
    assert isinstance(p.flying, str)


def test_person_1000_type():
    g = Generator()
    plist = g.generate_1000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Flamingo)
    assert len(plist) == 1000


def test_person_10000_type():
    g = Generator()
    plist = g.generate_10000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Flamingo)
    assert len(plist) == 10000