import requests
import json
import math 

'''
T_Loc - [win percent]
    [goal scored * win percent : goal conceded * loss percent]
'''

def main() :

	#with open('SerieAFixtures.json') as f:
	#	fixtures = json.load(f)

	url = "https://api-football-beta.p.rapidapi.com/fixtures"

	# UCL - 2
	# Europa League - 3
	# Bundesliga - 78
	# La liga - 140
	# Premier League - 39
	# serie a - 135
	# Ligue 1 - 61
	querystring = {"to":"2023-05-13","league":"135","season":"2022","from":"2023-02-13"}

	headers = {
		"X-RapidAPI-Key": key,
		"X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	fixtures = response.json()

	teamRatings = GetTeamsWithRatings(fixtures)

	team1 = "Juventus"
	team2 = "Cremonese"
	playerRatings = GetPlayerRatings(teamRatings, fixtures, team1, team2)

	print(*playerRatings,sep='\n')


@staticmethod
def CalcSimilarity(teamRatings, team_h, team_a) :

	x1 = teamRatings[team_h][0]
	y1 = teamRatings[team_h][1]
	x2 = teamRatings[team_a][0]
	y2 = teamRatings[team_a][1]

	offset = 0.000001 # to avoid div by zero 
	x_max = max(x1, x2) + offset
	y_max = max(y1, y2) + offset

	# cannot return 0
	x_min = min(x1, x2) + offset
	y_min = min(y1, y2) + offset

	return ( x_min / x_max ) * (y_min / y_max)


@staticmethod
def GetPlayerRatings(teamRatings, fixtures, team1, team2) :

	team1 = team1 + "_home"
	team2 = team2 + "_away"

	team1Rating = teamRatings[team1]
	team2Rating = teamRatings[team2]

	playerRatings = {}
	playerFixtureSim = {}
	playerPos = {}
	motmPlayers = []

	cnt = 0

	for fixture in fixtures["response"] :

		team_h = fixture["teams"]["home"]["name"] + "_home"
		team_a = fixture["teams"]["away"]["name"] + "_away"

		r = 0

		if team_h == team1 and team_a == team2 :
			r = 1
		elif team_h == team1 and team_a != team2 :
			r = CalcSimilarity(teamRatings, team_a, team2)
		elif team_h != team1 and team_a == team2 :
			r = CalcSimilarity(teamRatings, team_h, team1)
		else :
			continue

		cnt += 1

		fixtureStats = GetFixtureDetails(fixture["fixture"]["id"])

		team_h = fixtureStats[0]["team"]["name"] + "_home"
		team_a = fixtureStats[1]["team"]["name"] + "_away"

		motmPlayerName = ""
		motmRating = 0

		print ("fixture: ", team_h, " ", team_a, " Date: ", fixture["fixture"]["date"])

		if team_h == team1 :

			for player in fixtureStats[0]["players"] :

				name = player["player"]["name"]
				rating = player["statistics"][0]["games"]["rating"]

				if rating == None or rating == "-":
					continue

				if name not in playerRatings :
					playerRatings[name] = []
				if name not in playerFixtureSim :
					playerFixtureSim[name] = []

				playerRatings[name].append(rating)
				playerFixtureSim[name].append(r)
				playerPos[name] = player["statistics"][0]["games"]["position"]

				if float(rating) > motmRating :
					motmRating = float(rating)
					motmPlayerName = name + "_pos_" + player["statistics"][0]["games"]["position"]


			for player in fixtureStats[1]["players"] :

				name = player["player"]["name"]
				rating = player["statistics"][0]["games"]["rating"]

				if rating == None or rating == "-":
					continue

				if float(rating) > motmRating :
					motmRating = float(rating)
					motmPlayerName = name + "_pos_" + player["statistics"][0]["games"]["position"]

		if team_a == team2 :

			for player in fixtureStats[1]["players"] :

				name = player["player"]["name"]
				rating = player["statistics"][0]["games"]["rating"]

				if rating == None :
					continue

				if name not in playerRatings :
					playerRatings[name] = []
				if name not in playerFixtureSim :
					playerFixtureSim[name] = []

				playerRatings[name].append(rating)
				playerFixtureSim[name].append(r)
				playerPos[name] = player["statistics"][0]["games"]["position"]

				if float(rating) > motmRating :
					motmRating = float(rating)
					motmPlayerName = name + "_pos_" + player["statistics"][0]["games"]["position"]


			for player in fixtureStats[0]["players"] :

				name = player["player"]["name"]
				rating = player["statistics"][0]["games"]["rating"]

				if rating == None or rating == "-":
					continue

				if float(rating) > motmRating :
					motmRating = float(rating)
					motmPlayerName = name + "_pos_" + player["statistics"][0]["games"]["position"]


		if motmPlayerName not in motmPlayers :
			motmPlayers.append(motmPlayerName)


	print("total number of fixtures read: ", cnt)

	playersRes = {}

	for pl in playerRatings :

		rsum = 0
		rcnt = 0
		for i in range(len(playerRatings[pl])) :

			rsum += float(playerRatings[pl][i]) * playerFixtureSim[pl][i]
			rcnt += playerFixtureSim[pl][i]

		name = pl + "_pos_" + playerPos[pl]
		playersRes[name] = rsum / rcnt

		if name in motmPlayers :
			playersRes[name] += 1

	# sort with ratings
	playersRes = sorted(playersRes.items(), key=lambda x:x[1], reverse=True)

	return playersRes


@staticmethod
def GetFixtureDetails(fixtureId) :

	url = "https://api-football-beta.p.rapidapi.com/fixtures/players"

	querystring = {"fixture":fixtureId}

	headers = {
		"X-RapidAPI-Key": key,
		"X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	responseJson = response.json()

	return responseJson["response"]



@staticmethod
def GetTeamsWithRatings(fixtures) :

	# (teamname : [matchCount, winCount, loseCount, GoalCount, GoalConcededCount])
	teamStats = {}

	for fixture in fixtures["response"]:

		team1Name = fixture["teams"]["home"]["name"] + "_home"
		team2Name = fixture["teams"]["away"]["name"] + "_away"

		if team1Name not in teamStats :
			teamStats[team1Name] = [0, 0, 0, 0, 0]

		if team2Name not in teamStats :
			teamStats[team2Name] = [0, 0, 0, 0, 0]

		if fixture["teams"]["home"]["winner"] == False :
			teamStats[team1Name][2] += 1
		else :
			teamStats[team1Name][1] += 1

		if fixture["teams"]["away"]["winner"] == False :
			teamStats[team2Name][2] += 1
		else :
			teamStats[team2Name][1] += 1

		teamStats[team1Name][0] += 1
		teamStats[team2Name][0] += 1

		teamStats[team1Name][3] += fixture["goals"]["home"]
		teamStats[team2Name][3] += fixture["goals"]["away"]

		teamStats[team1Name][4] += fixture["goals"]["away"]
		teamStats[team2Name][4] += fixture["goals"]["home"]

	teamRatings = {}

	for name in teamStats :

		goalCountPt =          ( teamStats[name][3] / teamStats[name][0] ) * ( teamStats[name][1] / teamStats[name][0] )
		goalConcededCountPt =  ( teamStats[name][4] / teamStats[name][0] ) * ( teamStats[name][2] / teamStats[name][0] )

		teamRatings[name] = [goalCountPt, goalConcededCountPt]

	return teamRatings


if __name__ == "__main__" :	
	main()