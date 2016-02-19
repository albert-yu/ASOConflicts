from docx import Document
from parser import *

__author__ = 'Albert Yu'


def main():
    date = datetime.date.today()
    document = Document()
    date_as_string = date.month.__str__() + "-" + date.day.__str__() + "-" + date.year.__str__()
    document.add_heading('CONFLICTS ' + date_as_string, 0)
    table = document.add_table(rows=1, cols=4)
    headings = table.rows[0].cells
    headings[0].text = 'Name'
    headings[1].text = 'Instrument'
    headings[2].text = 'Time'
    headings[3].text = 'Reason'
    file_name = 'Conflicts ' + date_as_string + '.docx'

    # add ongoing conflicts first
    ongoing = store_conflicts('ongoing.csv')
    for conflict in ongoing:
        if conflict.date[:len(conflict.date) - 1] == int_to_weekday[date.weekday()]:
            row = table.add_row().cells
            row[0].text = conflict.name
            row[1].text = conflict.instrument
            row[2].text = conflict.time
            row[3].text = conflict.reason

    # iterate through the list of conflicts and add them to the document table one by one
    conflicts = store_conflicts('Conflicts.csv')
    for conflict in conflicts:
        if string_to_datetime(conflict.date) == date:
            row = table.add_row().cells
            row[0].text = conflict.name
            row[1].text = conflict.instrument
            row[2].text = conflict.time
            row[3].text = conflict.reason
    document.save(file_name)  # this will overwrite the existing file, which is what we want

if __name__ == "__main__":
    main()
