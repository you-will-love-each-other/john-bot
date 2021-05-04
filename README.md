This repo has the files for musik, JohnBot and HEALTH BOT used in the surprise event to announce HEALTH's collaboration track with Nine Inch Nails.
I will begin to describe how the bots work together and what happens in the event.

### 1. johnflag == True
What is presented to the server members is that there is a new feature - JohnBot - which just means whenever a user types in #health-hotline, a new bot will reply the same way John Famiglietti would. This feature is fake, however, so I'll explain what really is going on.

When JohnBot is started, the variable ``johnflag`` has a True value. This flag will become False whenever we type ``anh start [number_of_seconds]`` to start the actual event.
While ``johnflag`` is true, all the messages sent in #health-hotline will be replicated and sent to a secret channel where John will reply to them. Once John replies, that reply is sent back to #health-hotline by the bot, making it seem like it's the bot replying.

### 2. anh start [number_of_seconds]
This command starts the real event. What the users sees is that HEALTH BOT seems to be glitching and starts to send out a hate message continuously. ``number_of_seconds`` indicates how many seconds the bot will wait before sending the hate message again.

Once this command is triggered, HEALTH BOT saves to the dictionary ``oldperm`` the permissions in every channel of the server and sends out ``anh realstart`` in the #mod-chat then triggering musik bot.

Musik bot once receiving that command, starts saving to the dictionary ``oldperm`` the permissions and hiding all the channels for every user. When this cycle ends, musik bot sends ``anh endcycle`` in the #mod-chat.

### 3. anh endcycle
The user will now see JohnBot ceasing to send the repeated messages. Musik bot comes in, mutes HEALTH BOT and sends a few messages, the last one asking the HEALTHcord members to help it saving the server. The members will then have the opportunity to react to that message with a :cacopog: until it reaches 69 reacts (the number desired by musik bot). When a member reacts, they get the SAVIOR II role, which will mark their participation in this event.

### 4. Trivia
After reaching 69 reacts, musik bot will send some trivia. All the questions are stored in a list of tuples named ``trivia``, each tuple having the following structure: ``("initial_title","word_to_be_completed","empty_word","final_title","description","final_description","image_url")``
So, as it's noticeable, every trivia question follows the same hangman type of algorithm. The members will have to react to the embed sent by musik bot with the correct letters to fill the word. The bot choosed the letter with the most reacts every 3 seconds.

### 5. Secret link and channels reappear
Once the trivia is properly solved by the users, musik bot will have successfully recovered all the necessary data and will spill out a link. The link will contain a video announcement of the collaboration. After the link is sent, musik and HEALTH bot will start changing the channel permissions back to normal using the ``oldperm`` dictionary

## variables.py

```py
# variables.py should look like this

healthbot = 'health_bot_token'
johnbot = 'johnbot_token'
musik = 'musik_bot_token'

hotlineID = 837639467413274663
modchatID = 837639469195853833
johnchannelID = 837639469452492855

killereliteID = 837639467313397812
patron1 = 837639467313397813
patron2 = 837639467313397814
patron3 = 837639467313397815
eliteID = 837639467313397816
nightmareID = 837639467170660395
hurtID = 837639467170660394
imtooID = 837639467170660393
torquefestID = 837639467187306526
adventurerID = 837639467185960392
ndaID = 837639467170660396

new_saviorID = 837639467229118470

react_number = 69
```
