def read_data(files, total_records):
    records = []
    while len(records) < total_records:
        # Rotate the files queue
        files.rotate(1)
        with open(files[0]) as handle:
            data = json.load(handle)
            for record in data:
                records.append(record)
            If len(records) >= total_records:
                break
     return records
