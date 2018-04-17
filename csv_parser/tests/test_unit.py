from io import StringIO

from .. import Parser


def test_handles_monday():
    parser = Parser(StringIO('mon,description\n5,desc'))

    results = parser.parse()

    expected_results = [
        {'day': 'mon', 'description': 'desc 25', 'square': 25, 'value': 5}
    ]
    assert results == expected_results


def test_handles_tuesday():
    parser = Parser(StringIO('tue,description\n5,desc'))

    results = parser.parse()

    expected_results = [
        {'day': 'tue', 'description': 'desc 25', 'square': 25, 'value': 5}
    ]
    assert results == expected_results


def test_handles_wednesday():
    parser = Parser(StringIO('wed,description\n5,desc'))

    results = parser.parse()

    expected_results = [
        {'day': 'wed', 'description': 'desc 25', 'square': 25, 'value': 5}
    ]
    assert results == expected_results


def test_handles_thursday():
    parser = Parser(StringIO('thu,description\n5,desc'))

    results = parser.parse()

    expected_results = [
        {'day': 'thu', 'description': 'desc 10', 'double': 10, 'value': 5}
    ]
    assert results == expected_results


def test_handles_friday():
    parser = Parser(StringIO('fri,description\n5,desc'))

    results = parser.parse()

    expected_results = [
        {'day': 'fri', 'description': 'desc 10', 'double': 10, 'value': 5}
    ]
    assert results == expected_results


def test_handles_day_range():
    parser = Parser(StringIO('tue-thu,description\n5,desc'))

    results = parser.parse()

    expected_results = [
        {'day': 'tue', 'description': 'desc 25', 'square': 25, 'value': 5},
        {'day': 'wed', 'description': 'desc 25', 'square': 25, 'value': 5},
        {'day': 'thu', 'description': 'desc 10', 'double': 10, 'value': 5}
    ]
    assert results == expected_results
