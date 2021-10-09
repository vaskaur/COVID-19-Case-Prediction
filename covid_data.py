import requests

import json

class Covid:
    def __init__(self, daily_date, daily_dailyconfirmed, daily_dailydeceased, daily_dailyrecovered):
        self.daily_date = daily_date
        self.daily_dailyconfirmed = daily_dailyconfirmed
        self.daily_dailydeceased = daily_dailydeceased
        self.daily_dailyrecovered = daily_dailyrecovered

    def __str__(self):
        return "{} , {} , {} , {}\n".format(self.daily_date, self.daily_dailyconfirmed,  self.daily_dailydeceased, self.daily_dailyrecovered)


class fetchdata:

    def fetch(self, save_data):

        url = "https://api.covid19india.org/data.json"
        response = requests.get(url)
        covid_data = json.loads(response.text)
        covid_data_daily = covid_data['cases_time_series']
        i = 0
        covid_data_date = []
        covid_data_dailyconfirmed = []
        covid_data_dailydeceased = []
        covid_data_dailyrecovered = []

        for i in range(0, len(covid_data_daily)):
            covid_data_date.append(covid_data_daily[i]['date'])

        for i in range(0, len(covid_data_daily)):
            covid_data_dailyconfirmed.append(covid_data_daily[i]['dailyconfirmed'])

        for i in range(0, len(covid_data_daily)):
            covid_data_dailydeceased.append(covid_data_daily[i]['dailydeceased'])

        for i in range(0, len(covid_data_daily)):
            covid_data_dailyrecovered.append(covid_data_daily[i]['dailyrecovered'])

        covid_csv = []
        for i in range(0, len(covid_data_date)):
            data = Covid(covid_data_date[i], covid_data_dailyconfirmed[i], covid_data_dailydeceased[i], covid_data_dailyrecovered[i])
            covid_csv.append(data)
        if save_data:
            file = open('Covid_Confirmed_Data.csv', 'a')
            for row in covid_csv:
               file.write(str(row))
            print("Data saved!")


def main():
    data = fetchdata()
    data.fetch(True)


if __name__ == '__main__':
    main()