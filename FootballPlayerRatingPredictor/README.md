This code predicts the player ratings for upcoming fixture. Can be used to create fantasy team on apps like dream11.  
It uses free apis from rapidapi platform - it supports up-to 100 requests (of any type) a day, which is sufficient to predict at-least 3-4 fixtures using this code.  
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

fixture:  Lazio_home   Bologna_away  Date:  2022-08-14T16:30:00+00:00  
fixture:  Sassuolo_home   Lecce_away  Date:  2022-08-20T18:45:00+00:00  
fixture:  Lazio_home   Inter_away  Date:  2022-08-26T18:45:00+00:00  
fixture:  Napoli_home   Lecce_away  Date:  2022-08-31T18:45:00+00:00  
fixture:  Lazio_home   Napoli_away  Date:  2022-09-03T18:45:00+00:00  
fixture:  Torino_home   Lecce_away  Date:  2022-09-05T18:45:00+00:00  
fixture:  Lazio_home   Verona_away  Date:  2022-09-11T16:00:00+00:00  
fixture:  Salernitana_home   Lecce_away  Date:  2022-09-16T18:45:00+00:00  
fixture:  Lazio_home   Spezia_away  Date:  2022-10-02T10:30:00+00:00  
fixture:  AS Roma_home   Lecce_away  Date:  2022-10-09T18:45:00+00:00  
fixture:  Lazio_home   Udinese_away  Date:  2022-10-16T13:00:00+00:00  
fixture:  Bologna_home   Lecce_away  Date:  2022-10-23T13:00:00+00:00  
fixture:  Lazio_home   Salernitana_away  Date:  2022-10-30T17:00:00+00:00  
fixture:  Udinese_home   Lecce_away  Date:  2022-11-04T19:45:00+00:00  
fixture:  Lazio_home   Monza_away  Date:  2022-11-10T19:45:00+00:00  
fixture:  Sampdoria_home   Lecce_away  Date:  2022-11-12T17:00:00+00:00  
fixture:  Lazio_home   Empoli_away  Date:  2023-01-08T14:00:00+00:00  
fixture:  Spezia_home   Lecce_away  Date:  2023-01-08T14:00:00+00:00  
fixture:  Verona_home   Lecce_away  Date:  2023-01-21T14:00:00+00:00  
fixture:  Lazio_home   AC Milan_away  Date:  2023-01-24T19:45:00+00:00  
fixture:  Lazio_home   Fiorentina_away  Date:  2023-01-29T17:00:00+00:00  
fixture:  Cremonese_home   Lecce_away  Date:  2023-02-04T14:00:00+00:00  
fixture:  Lazio_home   Atalanta_away  Date:  2023-02-11T19:45:00+00:00  
fixture:  Atalanta_home   Lecce_away  Date:  2023-02-19T11:30:00+00:00  
fixture:  Lazio_home   Sampdoria_away  Date:  2023-02-27T19:45:00+00:00  
fixture:  Inter_home   Lecce_away  Date:  2023-03-05T17:00:00+00:00  
fixture:  Fiorentina_home   Lecce_away  Date:  2023-03-19T14:00:00+00:00  
fixture:  Lazio_home   AS Roma_away  Date:  2023-03-19T17:00:00+00:00  
fixture:  Empoli_home   Lecce_away  Date:  2023-04-03T16:30:00+00:00  
fixture:  Lazio_home   Juventus_away  Date:  2023-04-08T18:45:00+00:00  
fixture:  Lazio_home   Torino_away  Date:  2023-04-22T16:00:00+00:00  
fixture:  AC Milan_home   Lecce_away  Date:  2023-04-23T16:00:00+00:00  
fixture:  Juventus_home   Lecce_away  Date:  2023-05-03T16:00:00+00:00  
fixture:  Lazio_home   Sassuolo_away  Date:  2023-05-03T19:00:00+00:00  
total number of fixtures read:  34  
[('Mattia Zaccagni_pos_F', 7.511301391338877), ('Luis Alberto_pos_M', 7.315266608697479), ('Felipe Anderson_pos_F', 7.187335367315599), ('Marcos Antônio_pos_M', 7.150478091064174), ('Sergej Milinković-Savić_pos_M', 7.118027571953047), ('Nicolò Casale_pos_D', 7.0898888809188), ('Alessio Romagnoli_pos_D', 7.055867190229467), ('Ivan Provedel_pos_G', 7.002290460011757), ('Rémi Oudin_pos_F', 6.9925783349012445), ('Federico Baschirotto_pos_D', 6.9822641686469264), ('Gabriel Strefezza_pos_F', 6.960757233986591), ('Wladimiro Falcone_pos_G', 6.942698327800748), ('Patric_pos_D', 6.910897568686379), ('Mario Gila Fuentes_pos_D', 6.9), ('Tommaso Cassandro_pos_D', 6.9), ('Adam Marušić_pos_D', 6.875901152692491), ('Pedro_pos_F', 6.859913843033918), ('Manuel Lazzari_pos_D', 6.856831804285729), ('Simone Romagnoli_pos_D', 6.840958278604131), ('Toma Bašić_pos_M', 6.837667933431977), ('Antonino Gallo_pos_D', 6.820470063458589), ('Danilo Cataldi_pos_M', 6.818422703813204), ('Alexis Blin_pos_M', 6.815012221681428), ('Marin Pongračić_pos_D', 6.811067733222301), ('Assan Ceesay_pos_F', 6.808817985622024), ('Alessandro Tuia_pos_D', 6.76964578221165), ('Samuel Umtiti_pos_D', 6.754248432003945), ('Valentin Gendrey_pos_D', 6.737220679091451), ('Matteo Cancellieri_pos_F', 6.714523502977877), ('Elseid Hysaj_pos_D', 6.69912945521541), ('Giuseppe Pezzella_pos_D', 6.699016959129187), ('Matías Vecino_pos_M', 6.696516981520347), ('Kristoffer Askildsen_pos_M', 6.676392900984924), ('Ciro Immobile_pos_F', 6.673558949242208), ('Federico Di Francesco_pos_F', 6.664997172310134), ('Pablo Rodríguez_pos_F', 6.629923672481328), ('Joel Voelkerling Persson_pos_F', 6.623670662671587), ('Marcos Antonio_pos_M', 6.601134080212358), ('Pietro Ceccaroni_pos_D', 6.6), ('Luca Pellegrini_pos_D', 6.6), ('Kristijan Bistrović_pos_M', 6.580530772941977), ('Þórir Jóhann Helgason_pos_M', 6.552112410557426), ('Lorenzo Colombo_pos_F', 6.549954519712526), ('Joan González_pos_M', 6.540776389355378), ('Morten Hjulmand_pos_M', 6.520960536017701), ('Luka Romero_pos_M', 6.490203560415916), ('Marcin Listkowski_pos_F', 6.4675203773636385), ('Lameck Banda_pos_F', 6.459361624722312), ('Youssef Maleh_pos_M', 6.454964162103228), ('Kastriot Dermaku_pos_D', 6.2), ('Luis Maximiano_pos_G', 3.0)]
[Finished in 56.6s]  


