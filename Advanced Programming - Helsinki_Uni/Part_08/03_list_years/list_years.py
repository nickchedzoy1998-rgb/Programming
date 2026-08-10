from datetime import date

def list_years(dates: list):
    years = []

    for x in dates:
        years.append(x.year)
    years = sorted(years)

    return years