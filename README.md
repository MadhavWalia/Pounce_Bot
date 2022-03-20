# Pounce_Bot
To all the quizzers and quizmasters out there. This is the only bot you need to successfully conuduct an online quiz. 
The features:
-Add/Delete Roles ( Creation of roles with special permissions like QM, Scorekeeper etc.
-Add/Delete Voice and Text Channels( Creation of team specific channels)
-Scoresheet using Google Sheets Integration
-Facts using Reddit API
-Playing music from spotify/YouTube

### Tech Stack:
The bot has been made using discord.py and uses API integrations.

### Commands 
---
-make : Creates channels of QM, Scorekeeper and all teams and gives them required permissions
-deleteChannels : Deletes all team text channels
-deleteVoice  : Deletes all team voice channels
-clear{number of messages/all} : Deletes preceding messages in particular channel
-message {message text} : Sends announcements to all team channels 
-play {song link} : Joins the vocie channel and plays relevant song
-q : Shows the songs in queue
-skip : Skips the next song
-leave : Leaves the voice channel
-give{role name, member name} : Gives particular role to particular member
-removerole{role name, member name} : removes particular role from particular member 
-deleteAllRoles : Deletes all the team roles
-trivia : Fetches fact from subreddit r/todayilearned
-start{time duration} : Starts a timer for mentioned number of seconds
-create{number of questions, number of teams, email of QM} : Creates a google sheet for scorekeeping of required teams
-scores : fetches the scores of all the teams from Google Sheet
- pounce{question number, answer} : Notes pounce of the given team provided they answer within the window
- -open {time duration} _ Starts a timer of mentioned time duration
---
