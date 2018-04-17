import csv


class Parser:

    days = ['mon', 'tue', 'wed', 'thu', 'fri']

    def __init__(self, csv_file):
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # NOTE: Assuming the csv will always have two lines, one line
            # for the headers and one row of values
            self.data = row

    def _get_days_in_data(self):
        """
        Helper method.

        Returns a list of tuples in the format (day, header), where day is
        a string representation of the day and header is the csv header
        under which the day data can be found (for example 'tue',
        'wed-thu' etc.).
        """
        day_header_dict = {}

        for header in self.data.keys():
            if header in self.days:
                # Header and day are the same, for example 'fri'
                day_header_dict[header] = header
            elif '-' in header:
                # Contains a hyphen, so might be a day range like 'mon-wed'
                days = header.split('-')
                if len(days) == 2 and days[0] in self.days and days[1] in self.days:
                    # It is indeed a day range, not a random column with
                    # a hyphen
                    index_start = self.days.index(days[0])
                    index_end = self.days.index(days[1]) + 1
                    for day in self.days[index_start:index_end]:
                        # Create an entry in the dict for each day in
                        # the range
                        day_header_dict[day] = header

        # Using a list because we want the days to be ordered correctly
        return [
            (day, day_header_dict[day])
            for day in self.days
            if day in day_header_dict
        ]

    def parse(self):
        """
        Parse the csv file. This is the method that should be called
        by external functions and classes.
        """
        parsed = []

        for day, header in self._get_days_in_data():
            value = int(self.data[header])
            day_dict = {
                'day': day,
                'value': value
            }

            if day in ['mon', 'tue', 'wed']:
                day_dict['square'] = value * value
                day_dict['description'] = '{desc} {value}'.format(
                    desc=self.data['description'],
                    value=day_dict['square'])

            else:
                day_dict['double'] = value * 2
                day_dict['description'] = '{desc} {value}'.format(
                    desc=self.data['description'],
                    value=day_dict['double'])

            parsed.append(day_dict)

        return parsed
