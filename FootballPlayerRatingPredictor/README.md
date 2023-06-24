This code predicts the player ratings for upcoming fixture. Can be used to create fantasy team on apps like dream11.  
It uses free apis from rapidapi platform - it supports up-to 100 requests (of any type) a day, which is sufficient to predict at-least 3-4 fixtures per day using this code.  
https://rapidapi.com/api-sports/api/api-football-beta  

Code requires a few parameters to be set:  
| Params | Description |  
| ------|-----------|  
| league Id | Each league has unique Id. Can be checked with this api: https://www.api-football.com/documentation-beta#tag/Countries/operation/get-countries. This is needed for one time and can be cached to avoid extra calls. Hence not included in the code.  
| from date | to check past fixtures for each team in this league starting from this date to compute ratings for new fixture. It makes api call to get player ratings for each fixture. Avoid setting this to very old date to ensure api quota does not exhaust.    
| to date | can be set as present date  
| home team | name of home team  
| away team | name of away team 

Sample response for a fixture:  

The result format is: playerName_playerPosition_IsCaptain predictedRating MinRatingOnD11

Running in Test Mode  
New params:  
global motm_mul  
motm_mul =  0.7934919639127407  
global team_ratePt_mul  
team_ratePt_mul =  1.9479577755147233  
global r_gk_mul  
r_gk_mul =  1.4243600836780737  
global r_def_mul  
r_def_mul =  0.5797622033938612  
global r_mid_mul  
r_mid_mul =  0.34365455307123133  
global r_fwd_mul  
r_fwd_mul =  1.223603462902595  
home_adv:  True  
fixture:  Viking_home   Lillestrom_away  Date:  2023-04-15T16:00:00+00:00  
fixture:  ODD Ballklubb_home   Brann_away  Date:  2023-04-16T15:00:00+00:00  
fixture:  Bodo/Glimt_home   Brann_away  Date:  2023-04-29T16:00:00+00:00  
fixture:  Viking_home   Ham-Kam_away  Date:  2023-04-30T15:00:00+00:00  
fixture:  Viking_home   Stromsgodset_away  Date:  2023-05-07T15:00:00+00:00  
fixture:  Sarpsborg 08 FF_home   Brann_away  Date:  2023-05-13T15:00:00+00:00  
fixture:  Viking_home   ODD Ballklubb_away  Date:  2023-05-16T16:00:00+00:00  
fixture:  Aalesund_home   Brann_away  Date:  2023-06-04T15:00:00+00:00  
fixture:  Viking_home   Molde_away  Date:  2023-06-04T17:15:00+00:00  
fixture:  Rosenborg_home   Brann_away  Date:  2023-05-03T16:00:00+00:00  
total number of fixtures read:  10  
Mathias Rasmussen_pos_M  C   7.39043631698108   6.1  
Ulrik Mathisen_pos_M  N   7.150435655493292   6.2  
Bård Finne_pos_F  C   7.050436370596514   6.3  
Japhet Sery Larsen_pos_D  C   7.017636967399713   6.4  
Niklas Castro_pos_F  N   6.950436701334322   6.5  
Ole Didrik Blomberg_pos_F  C   6.870436272182952   6.6  
Felix Horn Myhre_pos_M  C   6.8704362429500145   6.7  
Svenn Crone_pos_D  C   6.79470896328215   6.8  
Isak Hjorteseth_pos_M  N   6.75043658682485   6.9  
Sivert Heltne Nilsen_pos_M  C   6.750436273995295   7.0  
Rasmus Holten_pos_D  N   6.7504361211580965   7.1  
Zlatko Tripić_pos_F  C   6.742054317000034   7.2  
Niklas Jensen_pos_F  C   6.701699824685278   7.3  
Ruben Kristiansen_pos_D  C   6.627297567611718   7.4  
Frederik Børsting_pos_M  C   6.604152034408694   7.5  
Thore Baardsen Pedersen_pos_D  N   6.550435655493293   7.6  
Aune Selland Heggebø_pos_F  C   6.48376964272442   7.7  
David Möller Wolfe_pos_D  C   6.405897348648857   7.8  
Marius Trengereid_pos_M  N   6.350437052491713   7.9  
Nicholas D'Agostino_pos_F  C   6.342053016978553   8.0  
Sondre Flem Bjørshol_pos_D  C   6.337653276201977   8.1  
Fredrik Knudsen_pos_D  C   6.309979157449058   8.2  
Matias Dyngeland_pos_G  C   6.304735775490378   8.3  
Sander Svendsen_pos_F  C   6.262053271885093   8.4  
David Brekalo_pos_D  C   6.254702718263442   8.5  
Harald Tangen_pos_M  C   6.122053724650287   8.6  
Eirik Johansen_pos_G  N   6.050437052491713   8.7  
David Tufekcic_pos_M  N   6.050436121158097   8.8  
Lars-Jørgen Salvesen_pos_F  C   6.042053858168743   8.9  
Niklas Sandberg_pos_M  C   6.01538725109514   9.0  
Yann-Erik de Lanlay_pos_M  C   5.941722164720181   9.1  
Patrick Yazbek_pos_M  C   5.932053367042837   9.2  
Edvin Austbø_pos_F  N   5.882053493379944   9.3  
Gianni Stensness_pos_D  C   5.724452338136709   9.4  
Birkir Bjarnason_pos_M  C   5.7153871945793195   9.5  
Markus Solbakken_pos_M  C   5.702053610559035   9.6  
Shayne Pattynama_pos_D  C   5.632696057207108   9.7  
Patrik Sigurdur Gunnarsson_pos_G  C   5.461190028945144   9.8  
Herman Johan Haugen_pos_D  C   5.3066250849928815   9.9  
Djibril Diop_pos_D  N   5.18205465592667   10.0  
