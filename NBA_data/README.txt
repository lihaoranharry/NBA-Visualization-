All the information is from 2016-2017 NBA regular season

NAME_TEAM.csv: 
'Name' column records the name of the player
'Team_Name' column records the team of the player(2016-2017 season), it is sorted by 'Name'.


pts_df.csv: this csv file records the POINTS each player made in clutch time. 
	'overall' means the average points for the player per game, 
	'10sec_down_3' means the average points points for the player in the games that the player's team DOWN 3 OR LESS 	 than 3 points to the opposite in last 10 seconds;  
	... 
	'30sec_plusminus_5' means the average points points for the player in the games that the player's team UP or 	DOWN 3 or LESS than 3 points to the opposite in last 30 seconds;


这个文件记录的是得分， overall是每场比赛的平均分（无论是否是clutch的比赛），'10sec_down_3' 记录的是球员在最后10秒钟主队（即此球员所在队伍）落后三分以内的平均得分； '30sec_plusminus_5' 记录的是球员在最后30秒主队领先或落后五分以内的平均得分。这些在其他的csv的文档中也是一样的意思我就不重复了

fgm_df.csv: this csv file records the field goal made for each player.
此文件记录命中球数

3fgm_df.csv: this csv file records the 3 points field goal made for each player.
此文件记录三分球命中球数


pct_df.csv: this csv file records the PERCENTAGE of shoots
此文件记录命中率（命中率是全部的投篮的命中率）

3pct_df.csv: this csv file records the 3points percentage of shoots
此文件记录三分命中率（三分命中率是仅算三分投篮的命中率）

fct_df.csv: this csv file records free throw percentage of shoots
此文件记录罚球命中率