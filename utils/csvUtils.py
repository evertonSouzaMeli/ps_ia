import csv


def includeRows(caption):
    fields = [caption.path, caption.date, caption.time, caption.local]
    with open(r'captures_data.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(fields);
