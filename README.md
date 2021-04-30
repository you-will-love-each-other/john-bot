# HEALTHcord Anniversary Event 2021
This repo has the files for musik and HEALTH BOT used in the surprise event for the HEALTHcord's first anniversary.
I will begin to describe how the bots work together and what happens in the event.

### 1. johnflag == True
What is presented to the server members is that HEALTH BOT has a new feature - AI John - which just means whenever a user types in #health-hotline, HEALTH BOT will reply the same way John Famiglietti would. This feature is fake, however, so I'll explain what really is going on.

When HEALTH BOT is started, the variable ``johnflag`` has a True value. This flag will become False whenever we type ``anh start [number_of_seconds]`` to start the actual event.
While ``johnflag`` is true, all the messages sent in #health-hotline will be replicated and sent to a secret channel where John will reply to them. Once John replies, that reply is sent back to #health-hotline by the bot, making it seem like it's the bot replying.

### 2. anh start [number_of_seconds]
This command starts the real event. What the uses sees is that HEALTH BOT seems to be glitching and starts to send out a hate message continuously. ``number_of_seconds`` indicates how many seconds the bot will wait before sending the hate message again.

Once this command is triggered, HEALTH BOT saves to the dictionary ``oldperm`` the permissions in every channel of the server and sends out ``anh realstart`` in the #mod-chat then triggering musik bot.

Musik bot once receiving that command, starts saving to the dictionary ``oldperm`` the permissions and hiding all the channels for every user. When this cycle ends, musik bot send ``anh endcycle`` in the #mod-chat.

### 3. anh endcycle
The user will now see HEALTH BOT ceasing to send the repeated messages. Musik bot comes in, mutes HEALTH BOT and sends a few messages, the last one asking the HEALTHcord members to help it saving the server. The members will then have the opportunity to react to that message with a :cacopog: until it reaches 69 reacts (the number desired by musik bot). When a member reacts, they get the SAVIOR II role, which will mark their participation in this event.

### 4. Trivia
After reaching 69 reacts, musik bot will send some trivia. All the questions are stored in a list of tuples named ``trivia``, each tuple having the following structure: ``("initial_title","word_to_be_completed","empty_word","final_title","description","final_description","image_url")``
So, as it's noticeable, every trivia question follows the same hangman type of algorithm. The members will have to react to the embed sent by musik bot with the correct letters to fill the word. The bot choosed the letter with the most reacts every 3 seconds.

### 5. El secreto and channels reappear
Once the trivia is properly solved by the users, musik bot will have successfully recovered all the necessary data and will spill out a link. The link will contain "el secreto". After the link is sent, musik and HEALTH bot will start changing the channel permissions back to normal using the ``oldperm`` dictionary
