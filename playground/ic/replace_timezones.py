import csv
import datetime


def replace_timezones_buildings():
    result = []

    with open("active im en.csv", "r") as f:
        read_dataset = csv.DictReader(f)

        for row in read_dataset:
            result.append(row)

    with open("BEYOND_MIRKOFLEKS_PROCESSED.csv", "w+") as f:
        fieldnames = result[0].keys()
        print(fieldnames)

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in result:
            timestamp = datetime.datetime.strptime(row["Timestamp"][:-4],
                                                   "%Y-%m-%d %H:%M:%S")
            timestamp = timestamp.replace(
                tzinfo=datetime.timezone.utc).isoformat()
            row["Timestamp"] = timestamp
            writer.writerow(row)


def replace_timezones_demand():
    result = []

    with open("DemandVolume.csv", "r") as f:
        read_dataset = csv.DictReader(f, delimiter=';')

        for row in read_dataset:
            result.append(row)

    with open("DEMAND_VOLUME_PROCESSED.csv", "w+") as f:
        fieldnames = result[0].keys()
        print(fieldnames)

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in result:
            timestamp = datetime.datetime.strptime(row['DeliveryStart'][:-5],
                                                   "%Y-%m-%dT%H:%M:%S")
            timestamp = timestamp.replace(
                tzinfo=datetime.timezone.utc).isoformat()
            row['DeliveryStart'] = timestamp

            value = row['DemandVolume']
            row['DemandVolume'] = float(value.replace(',', '.'))

            writer.writerow(row)


if __name__ == "__main__":
    replace_timezones_demand()
