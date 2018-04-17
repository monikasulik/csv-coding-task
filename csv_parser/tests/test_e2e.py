import os

from .. import Parser


CSV_FILE_DIR = os.path.join(
    os.path.dirname(__file__), os.pardir, 'data')


def test_csv_1():
    csv_file = open(os.path.join(CSV_FILE_DIR, '1.csv'))
    parser = Parser(csv_file)

    results = parser.parse()

    expected_results = [
        {'day': 'mon', 'description': 'first_desc 1', 'square': 1, 'value': 1},
        {'day': 'tue', 'description': 'first_desc 25', 'square': 25, 'value': 5},
        {'day': 'wed', 'description': 'first_desc 4', 'square': 4, 'value': 2},
        {'day': 'thu', 'description': 'first_desc 6', 'double': 6, 'value': 3},
        {'day': 'fri', 'description': 'first_desc 6', 'double': 6, 'value': 3}
    ]
    assert results == expected_results


def test_csv_2():
    csv_file = open(os.path.join(CSV_FILE_DIR, '2.csv'))
    parser = Parser(csv_file)

    results = parser.parse()

    expected_results = [
        {'day': 'mon', 'description': 'second_desc 4', 'square': 4, 'value': 2},
        {'day': 'tue', 'description': 'second_desc 4', 'square': 4, 'value': 2},
        {'day': 'wed', 'description': 'second_desc 4', 'square': 4, 'value': 2},
        {'day': 'thu', 'description': 'second_desc 4', 'double': 4, 'value': 2},
        {'day': 'fri', 'description': 'second_desc 6', 'double': 6, 'value': 3}
    ]
    assert results == expected_results


def test_csv_3():
    csv_file = open(os.path.join(CSV_FILE_DIR, '3.csv'))
    parser = Parser(csv_file)

    results = parser.parse()

    expected_results = [
        {'day': 'mon', 'description': 'third_desc 9', 'square': 9, 'value': 3},
        {'day': 'tue', 'description': 'third_desc 9', 'square': 9, 'value': 3},
        {'day': 'wed', 'description': 'third_desc 4', 'square': 4, 'value': 2},
        {'day': 'thu', 'description': 'third_desc 4', 'double': 4, 'value': 2},
        {'day': 'fri', 'description': 'third_desc 2', 'double': 2, 'value': 1}
    ]
    assert results == expected_results
