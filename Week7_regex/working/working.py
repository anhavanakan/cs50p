import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # input should be one of following versions
    # 9 AM to 5 PM
    # 9:00 AM to 5:00 PM
    work_hours = re.search(
        "((?:1[012]|[1-9])(?::[0-5][0-9])?) ([AP]M) (to) ((?:1[012]|[1-9])(?::[0-5][0-9])?) ([AP]M)",
        s,
    )
    # if there is something wrong raise error
    if not work_hours:
        raise ValueError

    # for convinience
    start_time = work_hours.group(1)
    start_am_pm = work_hours.group(2)
    to = work_hours.group(3)
    end_time = work_hours.group(4)
    end_am_pm = work_hours.group(5)

    # 7:12 PM will become 19:12 PM
    if start_am_pm == "PM":
        if ":" in start_time:
            hour, minute = start_time.split(":")
            start_time = str(int(hour) + 12) + ":" + minute
        # 8 PM will become 20 PM
        else:
            start_time = str(int(start_time) + 12)
    # the same with ending hour
    if end_am_pm == "PM":
        if ":" in end_time:
            hour, minute = end_time.split(":")
            end_time = str(int(hour) + 12) + ":" + minute
        else:
            end_time = str(int(end_time) + 12)

    # array of all text, just for convinience
    work_hours = []
    work_hours.append(start_time)
    work_hours.append(start_am_pm)
    work_hours.append(to)
    work_hours.append(end_time)
    work_hours.append(end_am_pm)

    # hence 9:12 will become 09:12 we need to add '0' before 1 digit hours
    # we will use 0th index of list of splitted string
    # if str is '9:12' or '9' 0th element is
    start_time_hour = int(work_hours[0].split(":")[0])
    end_time_hour = int(work_hours[3].split(":")[0])
    if start_time_hour < 10:
        work_hours[0] = "0" + work_hours[0]
    if end_time_hour < 10:
        work_hours[3] = "0" + work_hours[3]

    result = ""
    for i in work_hours:
        # in 24 hour format we dont need AM or PM
        if "M" in i:
            continue
        # if str does not contain ':', its a numeric
        # that means we should add ':00' to make it real time
        if i.isnumeric():
            i += ":00"
        # we added 12 only to PM times, but 12:00 AM should become 00:00
        # thats why this should be done manually
        if i == "12:00":
            i = "00:00"
        # the same with 12:00 PM, we added 12 and made it 24:00
        # it should become 00:00
        if i == "24:00":
            i = "12:00"
        # after all changes or without changes we should add list elements to result
        result += i + " "
    #we dont need the last ' '
    result = result.rstrip()
    # finally return it
    return result


if __name__ == "__main__":
    main()
