import requests
import json
import math 
import numpy as np
import random

'''
This code computes player ratings for upcoming fixture and results it in sorted order to create fantasy teams.
We can directly get player ratings from API for old fixtures.
We use ratings from API for old fixtures and calculate cumulative ratings based on various factors like: home/away advantage, type of opponent team
Like whether the opponent team is attacking / defensive / and its win probabilities.
Hence the cumulative rating of a player depends on opponent team.
Also we add some indication if a player can be selected as captain only if we have sufficient datapoints for that player to be reliably consistent.
'''

key = "<key>"

home_adv = True
run_testMode = True

# Model Params (all should be >= 0): these params gets manually trained on random updates, based on comparing team points w/o updates
motm_mul = 1
team_ratePt_mul = 1
r_gk_mul = 1
r_def_mul = 1
r_mid_mul = 1
r_fwd_mul = 1

def main() :

	if run_testMode == True :

		print ("Running in Test Mode")

		# update params :
		global motm_mul
		motm_mul =  1.2172235083029654
		global team_ratePt_mul
		team_ratePt_mul =  1.6688563483638106
		global r_gk_mul
		r_gk_mul =  1.4899173176882974
		global r_def_mul
		r_def_mul =  0.727863067708989
		global r_mid_mul
		r_mid_mul =  0.5036087927256189
		global r_fwd_mul
		r_fwd_mul =  0.8842781218918087

		# increment on no diff / decrement on diff
		ep = 7

		rand = random.random()
		motm_mul = motm_mul + (rand - 0.5) * ep / 5 # +- 0.1 for all
		rand = random.random()
		team_ratePt_mul = team_ratePt_mul + (rand - 0.5) * ep / 5
		rand = random.random()
		r_gk_mul = r_gk_mul + (rand - 0.5) * ep / 5
		rand = random.random()
		r_def_mul= r_def_mul + (rand - 0.5) * ep / 5
		rand = random.random()
		r_mid_mul = r_mid_mul + (rand - 0.5) * ep / 5
		rand = random.random()
		r_fwd_mul = r_fwd_mul + (rand - 0.5) * ep / 5

		# min-max limit
		motm_mul = max(0, motm_mul)
		motm_mul = min(2, motm_mul)
		team_ratePt_mul = max(0, team_ratePt_mul)
		team_ratePt_mul = min(2, team_ratePt_mul)
		r_gk_mul = max(0, r_gk_mul)
		r_gk_mul = min(10, r_gk_mul)
		r_def_mul = max(0, r_def_mul)
		r_def_mul = min(10, r_def_mul)
		r_fwd_mul = max(0, r_fwd_mul)
		r_fwd_mul = min(10, r_fwd_mul)

		# print new values as code
		print ("New params: ")
		print ("global motm_mul")
		print ("motm_mul = ", motm_mul)
		print ("global team_ratePt_mul")
		print ("team_ratePt_mul = ", team_ratePt_mul)
		print ("global r_gk_mul")
		print ("r_gk_mul = ", r_gk_mul)
		print ("global r_def_mul")
		print ("r_def_mul = ", r_def_mul)
		print ("global r_mid_mul")
		print ("r_mid_mul = ", r_mid_mul)
		print ("global r_fwd_mul")
		print ("r_fwd_mul = ", r_fwd_mul)



	url = "https://api-football-beta.p.rapidapi.com/fixtures"

	# Active Leagues:
	# ===================================
	# Argentinian League - 128 (2023)
	# Brizilian serie a - 71 (2023)
	# Bundesliga - 78
	# Chinese super league - 169 (2023)
	# Copa Sudamericana - 11 (2023)
	# Copa Libertadores - 13 (2023)
	# Danish League - 119
	# Dutch League - 88
	# Euro Qualifiers - 960 (2023)
	# Europa League - 3
	# FA Cup - 45
	# International Friendlies - 10
	# J League - 98 (2023)
	# La liga - 140
	# La liga 2 - 141
	# Ligue 1 - 61
	# Norweigain League - 103 (2023)
	# Polish league - 106
	# Portuguese League - 94 
	# Premier League - 39
	# Russian Premier League - 235
	# Saudi Arabian League - 307
	# Serie A - 135
	# Swedish League - 113 (2023)
	# Turkish League - 203
	# UEFA Europa Conference League - 848
	# UEFA Nations League - 5
	# UCL - 2

	# Inactive Leagues:
	# =====================================
	# AFCON Qualifiers - 36 (2023)
	# Club Friendlies
	# Hero Intercontinental Cup - 324
	# MLS
	# Murice Revello Tournament
	# U20 Football World Cup - 490 (2023)
	# US Open Cup
	
	# We need around 10-15 fixtures to get reliable player ratings
	# Set the from Date as 3 months ago for regular league matches, 6 months for others like UCL, minor leagues etc
	querystring = {"to":"2023-06-23","league":"103","season":"2023","from":"2023-01-01"}

	headers = {
		"X-RapidAPI-Key": key,
		"X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	fixtures = response.json()

	teamRatings = GetTeamsWithRatings(fixtures)

	print ("home_adv: ", home_adv)

	team1 = "Viking" # 
	team2 = "Brann" # 
	playerRatings = GetPlayerRatings(teamRatings, fixtures, team1, team2)

	plen = len(playerRatings)

	# we expect the fantasy app to rate player with atleast minRation - otherwise drop this player from the team
	for i in range(plen) :
		minRating = 6 + ((i+1)/plen) * 4
		print(playerRatings[i][0], " ", playerRatings[i][1], " ", minRating)
	


@staticmethod
def CalcSimilarity(teamRatings, team1, team2) : # team1: current fixture team, team2: base team to take ref

	offset = 0.000001 # to avoid div by zero condition
	teamRatings[team1][0] += offset
	teamRatings[team1][1] += offset
	teamRatings[team2][0] += offset
	teamRatings[team2][1] += offset

	# below is a function y = x / (x+c), min value: 0, max value = 1 as x increases
	# depends on c when it hits 0.5 as x increases
	rgk  = teamRatings[team1][0] / (teamRatings[team1][0] + r_gk_mul) 
	rdef = teamRatings[team1][0] / (teamRatings[team1][0] + r_def_mul) 
	rmid = teamRatings[team2][1] / (teamRatings[team2][1] + r_mid_mul)
	rfwd = teamRatings[team2][1] / (teamRatings[team2][1] + r_fwd_mul) 

	return rgk, rdef, rmid, rfwd

@staticmethod
# Ratings of players of team1 vs team2 are computed
# Iterate all fixture and select only those with team1 or team2
# We get a list of ratings for each players 
# The aggregated rating is the weighted average of ratings based on player's position and opposition team rating
# Man of the match players get bonus rating
def GetPlayerRatings(teamRatings, fixtures, team1, team2) :

	if home_adv == True :
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

		team_h = fixture["teams"]["home"]["name"] 
		team_a = fixture["teams"]["away"]["name"] 

		if home_adv == True :
			team_h = team_h + "_home"
			team_a = team_a + "_away"
		else :
			# swap team1/team2 
			if team_h == team2 or team_a == team1 :
				team_temp = team1
				team1 = team2 
				team2 = team_temp

		if team_h != team1 and team_a != team2 :
				continue

		fixtureStats = GetFixtureDetails(fixture["fixture"]["id"])

		if len(fixtureStats) == 0 :
			print ("fixtureStats is empty")
			continue

		cnt += 1

		# reconstructing team names again for fixture details response
		team_h = fixtureStats[0]["team"]["name"] 
		team_a = fixtureStats[1]["team"]["name"] 

		if home_adv == True :
			team_h = team_h + "_home"
			team_a = team_a + "_away"
		else :
			# swap team1/team2 
			if team_h == team2 or team_a == team1 :
				team_temp = team1
				team1 = team2 
				team2 = team_temp

		motmPlayerName = ""
		motmRating = 0

		print ("fixture: ", team_h, " ", team_a, " Date: ", fixture["fixture"]["date"])

		rdef = 1
		rmid = 1
		rfwd = 1

		if team_h == team1 :

			rgk, rdef, rmid, rfwd = CalcSimilarity(teamRatings, team_a, team2)

			for player in fixtureStats[0]["players"] :

				name = player["player"]["name"]
				rating = player["statistics"][0]["games"]["rating"]

				if rating == None or rating == "-":
					continue

				rating = float(rating) + TeamWinPt(teamRatings, team_h)

				if name not in playerRatings :
					playerRatings[name] = []
				if name not in playerFixtureSim :
					playerFixtureSim[name] = []

				playerRatings[name].append(rating)
				#playerFixtureSim[name].append(r)

				pos = player["statistics"][0]["games"]["position"]
				playerPos[name] = pos

				if pos == 'G' :
					#print ("rdef: ", rdef)
					playerFixtureSim[name].append(rgk)
				elif pos == 'D' :
					playerFixtureSim[name].append(rdef)
				elif pos == 'F' :
					#print ("rfwd: ", rfwd)
					playerFixtureSim[name].append(rfwd)
				else :
					#print ('rmid: ', rmid)
					playerFixtureSim[name].append(rmid)


				if float(rating) > motmRating :
					motmRating = float(rating)
					motmPlayerName = name + "_pos_" + pos


			for player in fixtureStats[1]["players"] :

				name = player["player"]["name"]
				rating = player["statistics"][0]["games"]["rating"]

				if rating == None or rating == "-":
					continue

				rating = float(rating) + TeamWinPt(teamRatings, team_a)

				if float(rating) > motmRating : # consider player as best only if it has heighest rating over both teams (because team2 can be different team)
					motmRating = float(rating)
					motmPlayerName = name + "_pos_" + player["statistics"][0]["games"]["position"]

		if team_a == team2 :

			rgk, rdef, rmid, rfwd = CalcSimilarity(teamRatings, team_h, team1)

			for player in fixtureStats[1]["players"] :

				name = player["player"]["name"]
				rating = player["statistics"][0]["games"]["rating"]

				if rating == None or rating == "-":
					continue

				rating = float(rating) + TeamWinPt(teamRatings, team_a)

				if name not in playerRatings :
					playerRatings[name] = []
				if name not in playerFixtureSim :
					playerFixtureSim[name] = []

				playerRatings[name].append(rating)
				#playerFixtureSim[name].append(r)

				pos = player["statistics"][0]["games"]["position"]
				playerPos[name] = pos

				if pos == 'G' :
					#print ("rdef: ", rdef)
					playerFixtureSim[name].append(rgk)
				elif pos == 'D' :
					playerFixtureSim[name].append(rdef)
				elif pos == 'F' :
					#print ("rfwd: ", rfwd)
					playerFixtureSim[name].append(rfwd)
				else :
					#print ('rmid: ', rmid)
					playerFixtureSim[name].append(rmid)

				if float(rating) > motmRating :
					motmRating = float(rating)
					motmPlayerName = name + "_pos_" + pos


			for player in fixtureStats[0]["players"] :

				name = player["player"]["name"]
				rating = player["statistics"][0]["games"]["rating"]

				if rating == None or rating == "-":
					continue

				rating = float(rating) + TeamWinPt(teamRatings, team_h)

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

		# player can be selected as captain only if he played sufficient number of matches
		cap = "N"
		if len(playerRatings[pl]) * 4 > cnt :
			cap = "C"

		name = pl + "_pos_" + playerPos[pl] + "  " + cap
		playersRes[name] = rsum / rcnt

		# man of the match bonus points
		if name in motmPlayers :
			playersRes[name] += 1 * motm_mul

	# sort with ratings
	playersRes = sorted(playersRes.items(), key=lambda x:x[1], reverse=True)

	return playersRes


# To update player ratings based on its team ratings
# because taking just few fixtures as datapoints does not reflect correct player ratings if team played against strong / weak teams
# return range [-1,1]
@staticmethod
def TeamWinPt(teamRatings, team) :
	teamRating = teamRatings[team]
	return ( teamRating[0] / (teamRating[0] + teamRating[1]) ) - ( teamRating[1] / (teamRating[0] + teamRating[1]) ) * team_ratePt_mul

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
# returns teamName : [goalsScoredPt, goalsConcededPt]
# for each fixture we compute the absolute points for goals scores / conceded 
# because it depends on win percent of opponent team
# hence first iterate through all the fixtures - and calculate win percent for all teams
# again iterate all fixtures, and absoulte values would be avg of: [ goal scored * win ratio of opponent team, goals conceded * lose ratio of opponent team ]
def GetTeamsWithRatings(fixtures) :

	# key: team name, Value: [total match, wins, absGoalsScored, absGoalsConceded]
	teamWinCnt = {} # 0.5 for draw

	for fixture in fixtures["response"] :

		if home_adv == True :
			team1Name = fixture["teams"]["home"]["name"] + "_home"
			team2Name = fixture["teams"]["away"]["name"] + "_away"
		else :
			team1Name = fixture["teams"]["home"]["name"]
			team2Name = fixture["teams"]["away"]["name"]

		if team1Name not in teamWinCnt :
			teamWinCnt[team1Name] = [0, 0, 0, 0]

		if team2Name not in teamWinCnt :
			teamWinCnt[team2Name] = [0, 0, 0, 0]

		teamWinCnt[team1Name][0] += 1
		teamWinCnt[team2Name][0] += 1

		if fixture["teams"]["home"]["winner"] == True :
			teamWinCnt[team1Name][1] += 1
		elif fixture["teams"]["away"]["winner"] == True :
			teamWinCnt[team2Name][1] += 1
		else :
			teamWinCnt[team1Name][1] += 0.5
			teamWinCnt[team2Name][1] += 0.5


	# again loop to aggregate absolute goals scored / conceded
	for fixture in fixtures["response"] :

		if home_adv == True :
			team1Name = fixture["teams"]["home"]["name"] + "_home"
			team2Name = fixture["teams"]["away"]["name"] + "_away"
		else :
			team1Name = fixture["teams"]["home"]["name"]
			team2Name = fixture["teams"]["away"]["name"]

		if fixture["goals"]["home"] == None :
			fixture["goals"]["home"] = 0

		if fixture["goals"]["away"] == None :
			fixture["goals"]["away"] = 0

		# goals cnt for team1
		mul = teamWinCnt[team2Name][1] / teamWinCnt[team2Name][0] # in range 0-1
		#mul = team2WinPer / 50
		teamWinCnt[team1Name][2] += mul * fixture["goals"]["home"]
		teamWinCnt[team1Name][3] += (1-mul) * fixture["goals"]["away"]

		# goals cnt for team2
		mul = teamWinCnt[team1Name][1] / teamWinCnt[team1Name][0]
		#mul = team1WinPer / 50
		teamWinCnt[team2Name][2] += mul * fixture["goals"]["away"]
		teamWinCnt[team2Name][3] += (1-mul) * fixture["goals"]["home"]

	# calc avg of absolute goals counts
	teamRatings = {}

	for teamName in teamWinCnt :
		teamRatings[teamName] = [0, 0]
		teamRatings[teamName][0] = teamWinCnt[teamName][2] / teamWinCnt[teamName][0]
		teamRatings[teamName][1] = teamWinCnt[teamName][3] / teamWinCnt[teamName][0]


	return teamRatings


if __name__ == "__main__" :	
	main()
