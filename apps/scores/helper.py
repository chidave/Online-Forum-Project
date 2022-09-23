from datetime import datetime
import requests, json, sys, os
from datetime import datetime, timedelta


def get_data(date: str, date_code: int) -> dict:
    # yesterday = datetime.today() - timedelta(1)
    # yesterday_date = yesterday.isoformat("|").split("|")[0]
    print(f"Request date: {date}")

    # create a file with yesterday's date or today's date
    cache_filename = ''
    if date_code == 0:
        cache_filename = 'yesterday_cache/' + date + '.txt'
    elif date_code == 1:
        cache_filename = 'today_cache/' + date + '.txt'
    else:
        pass

    data = ''

    # so first check if there is already a cache file for the date 
    # (in this case, yesterday's date)
    if os.path.exists(cache_filename):
        print("READ FROM CACHE!!!")
        # use the data from here instead of pulling from the API
        file_data = ''
        with open(cache_filename) as f:
            file_data = f.readlines()
            data = file_data[0]
    # else get the data from the api, then save to the cache
    else:
        print("READ FROM API!!!")
        url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
        querystring = {"date":date}
        headers = {
            "X-RapidAPI-Key": "0d59535b05msh9f26363d6435b75p1a4bd3jsn6d5c86f7815d",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text

        # now save the data to the cache file
        original_stdout = sys.stdout
        with open(cache_filename, 'w') as f:
            sys.stdout = f
            print(response.text)
            sys.stdout = original_stdout

    return process_data(data, date_code)


# remember to pass in some data
def process_data(data, date_code: int) -> dict:
    
    json_data = json.loads(data)
    response_data = json_data['response']
    england, spain, france, italy = [], [], [], []

    count = 0
    for response in response_data:
        count = count + 1
        teams = response['teams']
        league = response['league']
        league_name = league['name']
        home_team = teams['home']['name']
        away_team = teams['away']['name']
        home_goals = response['goals']['home']
        away_goals = response['goals']['away']
        final_score = {'League': league_name, home_team: home_goals, away_team: away_goals}

        # print(f'Away goals: {away_goals}, Type: {type(away_goals)}')
        # only take fixtures that have results
        if date_code == 0:
            if home_goals != None and away_goals != None:
                if league['country'] == 'England':
                    england.append(final_score)
                elif league['country'] == 'Spain':
                    spain.append(final_score)
                elif league['country'] == 'France':
                    france.append(final_score)
                elif league['country'] == 'Italy':
                    italy.append(final_score)
                else:
                    pass
        else:
            if league['country'] == 'England':
                england.append(final_score)
            elif league['country'] == 'Spain':
                spain.append(final_score)
            elif league['country'] == 'France':
                france.append(final_score)
            elif league['country'] == 'Italy':
                italy.append(final_score)
            else:
                pass

    england_league_fixtures = organize_data(england, date_code)
    spain_league_fixtures = organize_data(spain, date_code)
    france_league_fixtures = organize_data(france, date_code)
    italy_league_fixtures = organize_data(italy, date_code)
    cleaned_data = {'England': england_league_fixtures, 
                    'Spain': spain_league_fixtures, 
                    'France': france_league_fixtures, 
                    'Italy': italy_league_fixtures}
    
    return cleaned_data


# organize the fixtures for a country into a dictionary with the leagues as keys
def organize_data(data: list, date_code: int) -> dict:

    league_dict = {}

    for fixture in data:
        key = fixture['League']
        if key not in league_dict: 
            league_dict[key] = []

        league_fixtures = league_dict[key]
        fixture.pop('League')
        fixture_string = ''
        count = 0
        for key2, value2 in fixture.items():
            if date_code == 0:
                if count == 0:
                    fixture_string = fixture_string + key2 + ' ' + str(value2) + ' : '
                else:
                    fixture_string = fixture_string + str(value2) + ' ' + key2
            else:
                if count == 0:
                    fixture_string = fixture_string + key2 + '&emsp;<em>VS</em>&emsp;'
                else:
                    fixture_string = fixture_string + key2
            count = count + 1
        # print(fixture_string)
        league_fixtures.append(fixture_string)

    return league_dict

# {'League': 'La Liga (Spain)', 'Valencia': 5, 'Getafe': 1}