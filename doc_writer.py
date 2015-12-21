import datetime
from docx import Document
from docx.shared import Inches
from parser import *

__author__ = 'Albert Yu'


date = datetime.date.today()
document = Document()
date_as_string = date.month.__str__() + "-" + date.day.__str__() + "-" + date.year.__str__()
document.add_heading('CONFLICTS ' + date_as_string, 0)
table = document.add_table(rows=0, cols=4)
file_name = 'Conflicts ' + date_as_string + '.docx'

conflicts = store_conflicts('Conflicts.csv')
for conflict in conflicts:
    row = table.add_row().cells
    row[0].text = conflict.name
    row[1].text = conflict.instrument
    row[2].text = conflict.time
    row[3].text = conflict.reason
document.save(file_name)  # this will overwrite the existing file, which is what we want
