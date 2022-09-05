from datetime import datetime
import requests, json, sys
from datetime import datetime, timedelta

def get_data() -> dict:
    return process_data()

    # yesterday = datetime.today() - timedelta(1)
    # yesterday_date = yesterday.isoformat("|").split("|")[0]
    # print(f"Yesterday's date: {yesterday_date}")

    # url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    # querystring = {"date":yesterday_date}

    # headers = {
    #     "X-RapidAPI-Key": "0d59535b05msh9f26363d6435b75p1a4bd3jsn6d5c86f7815d",
    #     "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)

    # original_stdout = sys.stdout
    # with open('Football_Api_Results.txt', 'w') as f:
    #     sys.stdout = f
    #     print(response.text)
    #     sys.stdout = original_stdout


# remember to pass in some data
def process_data() -> dict:
    file_data = ''
    with open('Football_Api_Results.txt') as f:
        file_data = f.readlines()
    
    data = file_data[0]
    json_data = json.loads(data)
    response_data = json_data['response']
    england, spain, france, italy = [], [], [], []

    # print(f'Type: {type(response_data)}')
    # test_match = response_data[0]

    count = 0
    for response in response_data:
        count = count + 1
        teams = response['teams']
        league = response['league']

        if league['country'] == 'England':
            league_name = league['name']
            home_team = teams['home']['name']
            away_team = teams['away']['name']
            home_goals = response['goals']['home']
            away_goals = response['goals']['away']
            final_score = {'League': league_name, home_team: home_goals, away_team: away_goals}
            england.append(final_score)
        elif league['country'] == 'Spain':
            league_name = league['name']
            home_team = teams['home']['name']
            away_team = teams['away']['name']
            home_goals = response['goals']['home']
            away_goals = response['goals']['away']
            final_score = {'League': league_name, home_team: home_goals, away_team: away_goals}
            spain.append(final_score)
        elif league['country'] == 'France':
            league_name = league['name']
            home_team = teams['home']['name']
            away_team = teams['away']['name']
            home_goals = response['goals']['home']
            away_goals = response['goals']['away']
            final_score = {'League': league_name, home_team: home_goals, away_team: away_goals}
            france.append(final_score)
        elif league['country'] == 'Italy':
            league_name = league['name']
            home_team = teams['home']['name']
            away_team = teams['away']['name']
            home_goals = response['goals']['home']
            away_goals = response['goals']['away']
            final_score = {'League': league_name, home_team: home_goals, away_team: away_goals}
            italy.append(final_score)
        else:
            pass

    # for score in spain:
    #     print(score)

    # print(f'Count: {count}')

    # for fixture in organize_data(spain)['La Liga']:
    #     print(fixture)

    england_league_fixtures = organize_data(england)
    spain_league_fixtures = organize_data(spain)
    france_league_fixtures = organize_data(france)
    italy_league_fixtures = organize_data(italy)
    cleaned_data = {'England': england_league_fixtures, 
                    'Spain': spain_league_fixtures, 
                    'France': france_league_fixtures, 
                    'Italy': italy_league_fixtures}
    
    return cleaned_data


# organize the fixture for a country into a dictionary with the leagues as keys
def organize_data(data: list) -> dict:

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
            if count == 0:
                fixture_string = fixture_string + key2 + ' ' + str(value2) + ' : '
            else:
                fixture_string = fixture_string + str(value2) + ' ' + key2
            count = count + 1
        print(fixture_string)
        league_fixtures.append(fixture_string)

    return league_dict

# {'League': 'La Liga (Spain)', 'Valencia': 5, 'Getafe': 1}