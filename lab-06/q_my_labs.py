#!/usr/bin/env python3

import datetime

def main():
    """
    Create a datetime object for today's date
    """

    # COMPLETE IMPLEMENTATION
    todays_date = datetime.date.today()

    lab_dates = every_lab(todays_date, datetime.date(2023, 12, 4))
    for lab_date in lab_dates:
        print(lab_date.strftime("%a, %d %B %y"))


    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 19 November 23"
    """

    # COMPLETE IMPLEMENTATION

    


def every_lab(todays_date, last_date):

    """
    Classes for the current semester end on Dec 4, 2023.

    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """

    lab_dates = []
    while todays_date <= last_date:
        lab_dates.append(todays_date)
        todays_date += datetime.timedelta(days = 7)
    return lab_dates

if __name__ == "__main__":
    main()
