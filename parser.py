import datetime
import csv

__author__ = 'Albert Yu'
__version__ = '0.1'
# Date = 10-15-2015
# This script will parse the csv file that comes from a Google spreadsheet generated by
# http://goo.gl/forms/tIHhWWiBsd and create a Conflict object that will be interpreted by the docx_writer


def string_to_datetime(date_as_string):
    """
    Converts a string in the format "MM/DD/YYYY" to a datetime object
    :param date_as_string:
    :return: a datetime object
    """
    month = int(date_as_string[0:2])
    day = int(date_as_string[3:5])
    year = int(date_as_string[6:9])
    return datetime.date(year, month, day)


def datetime_to_string(date):
    """
    returns a nicely formatted string from a datetime object.
    e.g. Thursday, 11/19/2015
    :param date: a datetime object
    :return: a string
    """
    month = str(date.month)
    day = str(date.day)
    year = str(date.year)
    int_to_weekday = {0: "Monday",
                      1: "Tuesday",
                      2: "Wednesday",
                      3: "Thursday",
                      4: "Friday",
                      5: "Saturday",
                      6: "Sunday"
                      }

    return int_to_weekday[date.weekday()] + ", " + month + "/" + day + "/" + year


class Conflict(object):
    """
    Constructs a class with the attributes of a conflict
    name = name of person who has the conflict
    instrument = instrument person plays
    date = date the conflict is happening, a datetime object
    time = time the conflict is happening
    reason = reason for the conflict
    """
    def __init__(self, name, instrument, date, time, reason):
        self.name = name
        self.instrument = instrument
        self.date = date
        self.time = time
        self.reason = reason

    def to_string(self):
        """
        Returns the string form of the conflict, detailing the name, instrument, etc.
        :return:
        """
        return "Name: " + self.name + '\n' + \
               "Instrument: " + self.instrument + '\n' + \
               "Date absent: " + datetime_to_string(self.date) + '\n' + \
               "Time absent: " + self.time + '\n' + \
               "Reason: " + self.reason


def create_conflict(parsed_list):
    """
    Constructs a Conflict object from an appropriately formatted list of its attributes.
    :param parsed_list: format = [timestamp, name, instrument, date, time, reason]
    :return: a Conflict object
    """
    name = parsed_list[1]
    instr = parsed_list[2]
    date = parsed_list[3]
    time = parsed_list[4]
    reason = parsed_list[5]
    return Conflict(name, instr, date, time, reason)


def store_conflicts(csv_filename):
    """
    Creates a list of Conflict objects from an appropriately formatted csv file.
    (e.g. 11/15/2015 19:43:11,Test Person,Flute/Piccolo,11/17/2015,Before 8,Test)
    :param csv_filename, a string containing the name of the file in the same directory
    :return: a list of conflict objects
    """
    conflicts = []
    with open(csv_filename, "rt") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                conflicts.append(create_conflict(row))
            except:
                pass
    return conflicts

# print(store_conflicts('Conflicts.csv')[0].name)


def split_into_words(text):
    """
    Splits up a long string of text into a list of words. Probably will not be used.
    :param text:
    :return a list of words, without special chars:
    """
    words = []
    current_word = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char.lower() in alphabet:
            current_word += char
        else:
            words.append(current_word)
            current_word = ""
    return words

# test = "The cat is neither dead nor alive."
# print(split_into_words(test))


# def main():
    # print(store_conflicts('Conflicts.csv')[0].to_string())


# if __name__ == "__main__":
   #  main()







