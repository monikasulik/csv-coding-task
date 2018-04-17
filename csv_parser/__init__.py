import csv


class Parser:

    days = ['mon', 'tue', 'wed', 'thu', 'fri']

    def __init__(self, csv_file):
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            self.data = row

    def _get_days_in_data(self):
        days = {}
        for key in self.data.keys():
            if key in self.days:
                days[key] = key
            elif '-' in key:
                days_in_range = key.split('-')
                if days_in_range[0] in self.days and days_in_range[1] in self.days:
                    index_start = self.days.index(days_in_range[0])
                    index_end = self.days.index(days_in_range[1]) + 1
                    for day in self.days[index_start:index_end]:
                        days[day] = key
        return [(day, days[day]) for day in self.days if day in days]

    def parse(self):
        parsed = []
        for day, key in self._get_days_in_data():
            value = int(self.data[key])
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
