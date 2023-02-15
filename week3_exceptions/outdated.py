months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input('Date: ').strip().title()

        #what are separators (. / , - and so on)

        #for checking are separetors already assigned or not
        first_sep = 0
        second_sep = 0

        #if date contains alphabetical characters(e.g. september) format shold be like this 'September 10, 2001'
        #that means it should contain ', '
        #all months contain r, a or u,    if one of this letters is in date that means month is written with letters
        if 'r' in date or 'a' in date  or 'u' in date:
            if ', ' not in date:
                continue

        #if user separates date with ", " we will get into trouble, tahts why we need to remove ',' with nothing(replace)
        #after that mm dd yy are still separated with space
        if ',' in date:
            date = date.replace(',', '')


        for i in date:
            #search by ascii values ord('a') = 97  #ordinal,    all that stuff is between 32 and 48
            if 31 < ord(i) < 48:
                if first_sep == 0:
                    first_sep = i
                    #skip the rest of this iteration to not assign the same 'i' to second_sep
                    continue
                if second_sep == 0:
                    second_sep = i
                    #if second one is assigned, we are done
                    break
        #if first and second seps are the same we got lucky
        if first_sep == second_sep:
            month, day, year = date.split(first_sep)
        #else do it all manually :(
        else:
            month , day_and_year = date.split(first_sep)
            day, year = day_and_year.split(second_sep)

        #let's make our strings ints, for printing '8' like '08'
        day = int(day)
        year = int(year)

        #day should be less or equal to 31
        if day > 31 or day < 0:
            continue


        #month could be a not number i.g. september
        if month.isalpha():
            #if its alpha, its also should be in legit month name
            if month in months:
                month = months.index(month) + 1
                pass
            else:
                continue
        else:
            #hey month please became an int
            month = int(month)
            #month should be less or equal to 12
            if month < 1 or month > 12:
                continue

    except:
        pass
    else:
        #02 won't hurt string, it will affect the string if str will be 1 character, e.g. 'a' will become 'a0'
        print(f'{year}-{month:02}-{day:02}')
        break
