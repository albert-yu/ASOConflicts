from doc_writer import *
from dateutil import rrule

__author__ = 'Albert Yu'


# Previews upcoming conflicts for the coming week. Run this every Sunday before rehearsal.


def store_week_conflicts(csv_filename):
    conflicts = []
    date = datetime.date.today()
    end_of_week = date + datetime.timedelta(days=7)
    date_range = [dt.date() for dt in rrule.rrule(rrule.DAILY, dtstart=date, until=end_of_week)]
    with open(csv_filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != "Timestamp":
                if string_to_datetime(row[3]) in date_range:
                    conflicts.append(create_conflict(row))
    return conflicts


def main():
    date = datetime.date.today()
    date_as_string = date.month.__str__() + "-" + date.day.__str__() + "-" + date.year.__str__()

    document = Document()
    document.add_heading('CONFLICTS for the week of ' + date_as_string, 0)

    # add table for Tuesday conflicts
    document.add_heading('Tuesday', level=2)
    table_tues = document.add_table(rows=1, cols=4)
    # headings_tues = table_tues.rows[0].cells
    # create_headings(headings_tues)

    # add table for Wednesday conflicts
    document.add_heading('Wednesday', level=2)
    table_wed = document.add_table(rows=1, cols=4)

    # add table for Thursday conflicts
    document.add_heading('Thursday', level=2)
    table_thurs = document.add_table(rows=1, cols=4)
    # headings_thurs = table_thurs.rows[0].cells
    # create_headings(headings_thurs)

    document.add_heading('Friday', level=2)
    table_fri = document.add_table(rows=1, cols=4)

    # first iterate through ongoing conflicts
    ongoing = store_conflicts('ongoing.csv')
    for conflict in ongoing:
        if conflict.date[:len(conflict.date) - 1] == "Tuesday":
            row = table_tues.add_row().cells
            add_conflict_row(conflict, row)
        elif conflict.date[:len(conflict.date) - 1] == "Thursday":
            row = table_thurs.add_row().cells
            add_conflict_row(conflict, row)

    conflicts = store_week_conflicts('Conflicts.csv')
    for conflict in conflicts:
        # if the weekday falls on a Tuesday, append it to the Tuesday table
        if string_to_datetime(conflict.date).weekday() == 1:
            row = table_tues.add_row().cells
            add_conflict_row(conflict, row)

        # if the weekday falls on a Wednesday, append it to the Tuesday table
        if string_to_datetime(conflict.date).weekday() == 2:
            row = table_wed.add_row().cells
            add_conflict_row(conflict, row)

        # if Thursday, append to Thursday table
        elif string_to_datetime(conflict.date).weekday() == 3:
            row = table_thurs.add_row().cells
            add_conflict_row(conflict, row)
        # if Friday, append to Friday table
        elif string_to_datetime(conflict.date).weekday() == 4:
            row = table_fri.add_row().cells
            add_conflict_row(conflict, row)

    file_name = 'Conflicts week of ' + date_as_string + '.docx'
    document.save(file_name)


if __name__ == main():
    main()
