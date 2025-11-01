# ISO Converter
# Reads Date, Time, TZ, State, Country columns and converts to ISO-8601
# Empty time is set to midnight (00:00)
# Date and time in UTC e.g. 2025-11-01T17:28:55Z

import datetime

def date_to_iso():
    """ Formats non-compliant dates to ISO YYYY-MM-DD """

def get_tz():
    """ Find the Timezone (e.g. MST) for a given State+Country """

def out_iso(date, time, tz):
    """ Returns ISO formatted string """

def read_csv():
    """ Intake a CSV via upload or cli switch and put into a datastore """

def time_to_24h():
    """ Formats time input to 24-hour ISO HH:MM:SS"""

def main():
    """ Run the program """

if __name__ == "__main__":
    main()
    