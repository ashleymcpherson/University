#!/usr/bin/env python3

import datetime

def main():
    """
    Florence is a nurse in a clinic. She is caring for 4 patients on
    different medication schedules

    * Mark needs medication every 5 hours
    * Susan needs medication every 3 hours
    * Chloe needs medication every 8 hours
    * Alexander needs medication every 10 hours

    Starting with your current day and time, make a care schedule
    for the next 14 days that Florence can use to schedule
    who needs medication at what time.

    Follow the steps provided.

    STEP 1: Use function patient_schedule to get a list of
    medication times for every patient

    mark_schedule = <...........COMPLETE..................>
    susan_schedule = <...........COMPLETE..................>
    chloe_schedule = <...........COMPLETE..................>
    alexander_schedule = <...........COMPLETE..................>


    STEP 2: Combine all the lists and then form a master list of
    when medication is required by which patient.

    Print the medication schedule sorted by time in the format below:

      Friday, 25 03 2023, 09:24:27 Time to give medication to Alexander
      Friday, 25 03 2023, 10:24:27 Time to give medication to Chloe

    Refer to care_required.txt to see what the final output
    should look like. You are not required to write this information
    to a file. Simply output to console is enough.

    Note that care_required.txt does not contain the required output for
    this program. It only shows what the output should look like.

    HINT: You will need to keep track of who needs medication when.
    One way of doing this is with a dictionary. You may choose to
    use other ways.
    """
    # COMPLETE YOUR IMPLEMENTATION

    current = datetime.datetime.now()
    end = current + datetime.timedelta(days = 14)

    mark_schedule = patient_schedule("Mark", 5)
    susan_schedule = patient_schedule("Susan", 3)
    chloe_schedule = patient_schedule("Chloe", 8)
    alexander_schedule = patient_schedule("Alexander", 10)

    medication_schedule = []
    medication_schedule.extend(mark_schedule)
    medication_schedule.extend(susan_schedule)
    medication_schedule.extend(chloe_schedule)
    medication_schedule.extend(alexander_schedule)
    medication_schedule.sort(key = lambda x: x[1])

    while current < end:
        for patient, time in medication_schedule:
            if time >= current:
                print("{} Time to give medication to {}".format(current.strftime('%A, %d %m %Y, %H:%M:%S'), patient))
                break
        current += datetime.timedelta(hours = 1)


def patient_schedule(patient_name, interval_in_hours):
    
    ''' This function will take a patient name and corresponding medication
     interval and return a list of tuples where each tuple contains the
     patient name and medication time in datetime object format)
    '''
    # COMPLETE YOUR IMPLEMENTATION

    medication_times = []
    current = datetime.datetime.now()
    end = current + datetime.timedelta(days = 14)

    while current < end:
        medication_times.append((patient_name, current))
        current += datetime.timedelta(hours = interval_in_hours)

    return medication_times

if __name__ == "__main__":
    main()
