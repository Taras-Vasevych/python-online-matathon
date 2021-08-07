def day_of_week(day):
    try:
        return {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }[int(day)]
    except ValueError:
        return 'You did not enter a number! Please try again.'
    except KeyError:
        return 'There is no such day of the week! Please try again.'
