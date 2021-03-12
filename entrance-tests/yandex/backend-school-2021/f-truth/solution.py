import argparse
import csv
import json
import urllib.request as request

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.add_argument('port', type=int)
parser.add_argument('--not_mult', type=int, default=100,
                    help='skip values that are multiples of this number')
parser.add_argument('--smallest', type=int, default=0,
                    help='process only numbers that are not less than the given number')

args = parser.parse_args()


def is_valid(num):
    return num >= args.smallest and num % args.not_mult != 0


url = f"http://{args.host}:{args.port}"
with request.urlopen(url) as response:
    source = response.read()
    records = json.loads(source)

    processed_data = {}

    for record in records:
        for key, data in record.items():
            if key not in processed_data:
                processed_data[key] = []

            processed_data[key].extend([d for d in data if is_valid(d)])

    statistics = {}
    for key, data in processed_data.items():
        sum_data = sum(data)
        statistics[key] = {
            "min": min(data),
            "max": max(data),
            "avg": round(sum_data / len(data), 2),
            "sum": sum_data
        }

    with open('truth.csv', mode='w') as csv_file:
        truth_writer = csv.writer(csv_file, delimiter=';')

        sorted_names = sorted(statistics.keys())
        for key in sorted_names:
            data = statistics[key]
            truth_writer.writerow([key, data["max"], data["min"], data["avg"], data["sum"]])
