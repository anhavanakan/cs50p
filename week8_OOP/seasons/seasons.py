from datetime import date
import sys
import inflect


def main():
    birth_date = input("Date Of birth: ")
    print(f'{date_to_words(birth_date)} minutes')

def date_to_words(birth_date):
    p = inflect.engine()
    try:
        #user should write her/his birth date in YYYY-MM-DD format
        year, month, day = birth_date.split('-')

        #make that int
        year, month, day = int(year), int(month), int(day)

        #todays date
        today = date.today()

        #create object of person's birth date
        birth_date = date(year, month, day)

        #gap between today and birth day
        tdelta = today - birth_date

        #turn it into minutes
        minutes_lived = tdelta.days * 24 * 60
        
        #turn it into words
        #without 'and'
        #first letter capitalized
        words = p.number_to_words(minutes_lived, andword="").capitalize()
        return words


    except ValueError:
        sys.exit('Invalid date')




if __name__ == "__main__":
    main()
