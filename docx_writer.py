import datetime
from docx import Document
from docx.shared import Inches

__author__ = 'Albert Yu'

# Date: 10-15-15


def create_document(current_date):
    """
    Creates the word document
    :param current_date, a datetime object
    :return: none
    """
    document = Document()
    date_as_string = current_date.month.__str__() + "-" + current_date.day.__str__() + "-" + current_date.year.__str__()
    document.add_heading('CONFLICTS ' + date_as_string, 0)
    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Name'
    hdr_cells[1].text = 'Instr'
    hdr_cells[2].text = 'Reason'
    document.save('Conflicts ' + date_as_string + '.docx')

# def edit_document(): # edits the document of the given date





