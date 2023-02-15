import csv
import sys

if len(sys.argv) in [1, 2] or len(sys.argv) > 3:
    sys.exit("Specify 2 files")

students = []
try:
    with open(sys.argv[1]) as initial_file:
        # if initial_file doesn't exist we won't get to this point and outcome file will not be crated
        # and don't forget to close this
        outcome_file = open(sys.argv[2], "w")
        writer = csv.DictWriter(outcome_file, fieldnames=["first", "last", "house"])

        reader = csv.DictReader(initial_file)
        writer.writeheader()
        for row in reader:
            # actually the name is name and surename sapareted by comma
            last_name, first_name = row["name"].split(", ")
            # append to our list dictionaries of name surname and house
            students.append(
                {"first": first_name, "last": last_name, "house": row["house"]}
            )
            # write that dectionary to output file
        for student in students:
            writer.writerow(student)

    # this was opened without 'with' keyword
    outcome_file.close()
except FileNotFoundError:
    sys.exit("could not read the file")
