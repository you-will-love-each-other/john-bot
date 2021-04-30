import discord
import random
import math
import asyncio
import variables

client = discord.Client()
userset = set()


imageonly = False
flag = True
react = 0
oldperm = dict() # {"channel id" : {"roleid", perm}}
qmessage = False
qflag = False
alphabet = {"🇦":"A","🇧":"B","🇨":"C","🇩":"D","🇪":"E","🇫":"F","🇬":"G","🇭":"H","🇮":"I","🇯":"J","🇰":"K","🇱":"L","🇲":"M","🇳":"N","🇴":"O","🇵":"P","🇶":"Q","🇷":"R","🇸":"S","🇹":"T","🇼":"W","🇺":"U","🇻":"V","🇽":"X","🇾":"Y","🇿":"Z"}
count = 0
letter = False


@client.event
async def on_ready():
    print('musik is online')


@client.event
async def on_message(message):
    if message.content.startswith("anh "):# and message.author.id in [233290361877823498,455301777055547394,627265323720114188]:
        global oldperm
        roles = [variables.killereliteID, variables.patron1, variables.patron2, variables.patron3,variables.eliteID,variables.nightmareID,variables.hurtID,variables.imtooID,variables.torquefestID,variables.ndaID]
        msg = message.content.lower().split()
        if msg[1] == "endcycle":
            global react
            await client.get_channel(variables.hotlineID).trigger_typing()
            await asyncio.sleep(1)
            await client.get_channel(variables.hotlineID).send("!mute <@774402228084670515>")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await asyncio.sleep(2)
            await client.get_channel(variables.hotlineID).send("RECURSIVE ERROR DETECTED :: FAILSAFE ACTIVATED")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await client.get_channel(variables.hotlineID).send("RUNNING DIAGNOSTIC")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await asyncio.sleep(2)
            await client.get_channel(variables.hotlineID).send("MULTIPLE CRITICAL ERRORS DETECTED :: LOADING RECOVERY TOOLS")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await asyncio.sleep(2)
            react = await client.get_channel(variables.hotlineID).send("CONFIRM RECOVERY :: SOME DATA MAY BE DAMAGED OR LOST\n**REQUIRES {0} <:cacopog:697621015337107466> REACTS TO BEGIN\n@everyone**".format(variables.react_number))
            emoji = client.get_emoji(697621015337107466)
            await react.add_reaction(emoji)
        elif msg[1] == "realstart":
            await asyncio.sleep(2)
            server = message.guild
            for channel in server.channels:
                if channel.id != variables.hotlineID and channel.category:
                    daux = dict()
                    daux["everyone"] = channel.overwrites_for(message.guild.default_role).read_messages
                    await channel.set_permissions(message.guild.default_role, read_messages=False)
                    for role in roles:
                        overwrite = channel.overwrites_for(message.guild.get_role(role))
                        daux[str(role)] = overwrite.read_messages
                        if overwrite.read_messages:
                            await channel.set_permissions(message.guild.get_role(role), read_messages=False)
                    oldperm[str(channel.id)] = daux
        elif msg[1] == "normal":
            server = message.guild
            for channel in server.channels:
                if channel.id != variables.hotlineID and channel.category:
                    await channel.set_permissions(message.guild.default_role, read_messages=oldperm[str(channel.id)]["everyone"])
                    for role in roles:
                        overwrite = channel.overwrites_for(message.guild.get_role(role))
                        if overwrite.read_messages == False and overwrite.read_messages != oldperm[str(channel.id)][str(role)]:
                            await channel.set_permissions(message.guild.get_role(role), read_messages=oldperm[str(channel.id)][str(role)])

def checkletter(w,l):
    if l not in w:
        return False, -1
    for i in range(len(w)):
        if w[i] == l:
            return True, i

@client.event
async def on_reaction_add(reaction, user):
    global react
    global qmessage
    global alphabet
    global count
    global letter
    global qflag
    savior = reaction.message.guild.get_role(variables.new_saviorID)
    cacopog = client.get_emoji(697621015337107466)

    if reaction.message == react and reaction.emoji == cacopog:
        await user.add_roles(savior,reason="cacopog reaction", atomic=True)
        if reaction.count == variables.react_number:
            await asyncio.sleep(5)
            proc = await reaction.message.channel.send("```RESTORATION INITIATED...\n|____________________|  0%```")
            await asyncio.sleep(2)
            await proc.edit(content="```RESTORATION INITIATED...\n|███_________________| 13%```")
            await asyncio.sleep(1)
            await proc.edit(content="```RESTORATION INITIATED...\n|█████████___________| 45%```")
            await asyncio.sleep(3)
            await proc.edit(content="```RESTORATION INITIATED...\n|██████████████______| 70%```")
            await asyncio.sleep(2)
            await proc.edit(content="```RESTORATION INITIATED...\n|█████████████████___| 85%```")
            await asyncio.sleep(3)
            await proc.edit(content="```RESTORATION INITIATED...\n|████████████████████| 100%```")
            await asyncio.sleep(2)

            trivia = []     #   ("initial_title","word_to_be_completed","empty_word","final_title","description","final_description","image_url")

            trivia.append(("INCOMPLETE DATA :: THE FIRST MEMBER BANNED WAS","LUSHDEATH","_________","DATA SUCCESSFULLY RETRIEVED :: THE FIRST MEMBER BANNED WAS","","",""))
            trivia.append(("INCOMPLETE DATA :: WHAT WORD FROM GROUP B BELONGS TO GROUP A?","TOWER","     ","DATA SUCCESSFULLY RETRIEVED :: TOWER BELONGS TO GROUP A","A) FRONT, SKI, MELON, FALL\nB) ROAD, TIRE, TOWER, CLIFF\n\n\n","Explanation: Each word in group A can pair with water",""))
            trivia.append(("INCOMPLETE DATA :: WORD THAT DESCRIBES JARID","_RINGE","C_____","DATA SUCCESSFULLY RETRIEVED :: THE WORD THAT DESCRIBES JARID IS","","","",))
            trivia.append(("FILE CORRUPTED :: PLEASE IDENTIFY THE SUBJECT OF THIS PICTURE","JAR JAR BINKS","___ ___ _____","FILE RECOVERED :: JARJARBINKS.JPG", "", "", "https://imgur.com/oxzx3jG.png"))
            trivia.append(("CORRUPTED METADATA :: PLEASE IDENTIFY THIS IMAGE","AMONG US", "_____ __","METADATA COLLECTED :: AMONG_US.PNG", "","","https://i.imgur.com/cUx4AAo.png"))

            for entry in trivia:
                word = entry[1]
                blank = entry[2]
                embed = discord.Embed(title= entry[0], description= entry[4] + "``" + blank + "``", color=0xff0000)
                if entry[6]:
                    embed.set_image(url= entry[6])
                qmessage = await reaction.message.channel.send(embed= embed)

                i = 3
                usedletters = []
                wrongletterlist = []
                wrongletters = "Letters not present in this word: "

                while True:
                    await asyncio.sleep(1)
                    if not(word):
                        embed = discord.Embed(title= entry[3], description=blank + "\n\n" + entry[4] + entry[5], color=0x00ff00)
                        if entry[6]:
                            embed.set_image(url= entry[6])
                        await qmessage.edit(content="", embed= embed)
                        break
                    if qflag:
                        content = "```\nCOUNTING THE MOST REACTED LETTER...\n" + str(i) + "```"
                        i-=1
                        await qmessage.edit(content= content)
                    if i == -1:
                        fixedletter = letter
                        await qmessage.clear_reactions()
                        count = 0
                        i = 3
                        if fixedletter not in usedletters:
                            check,index = checkletter(word,fixedletter)
                            usedletters.append(fixedletter)
                            if check:
                                new_word = ""
                                new_blank = ""
                                for l in range(len(list(word))):
                                    if word[l] != word[index]:
                                        new_word += word[l]
                                        new_blank += blank[l]
                                    else:
                                        new_blank += word[l]
                                        new_word += "_"
                                blank = new_blank
                                word = new_word
                                if wrongletterlist:
                                    description = "``" + blank + "``\n\n" + wrongletters
                                else:
                                    description = "``" + blank + "``"
                                embed = discord.Embed(title= entry[0], description= entry[4] + description, color=0xff0000)
                                if entry[6]:
                                    embed.set_image(url= entry[6])
                                await qmessage.edit(embed= embed)
                                tempflag = True
                                for x in word:
                                    if x != "_" and x != " ":
                                        tempflag = False
                                        break
                                if tempflag:
                                    word = False
                            else:
                                if wrongletterlist:
                                    if fixedletter not in wrongletterlist:
                                        wrongletterlist.append(fixedletter)
                                        wrongletters += ", " + fixedletter
                                        description = "``" + blank + "``\n\n" + wrongletters
                                        embed = discord.Embed(title= entry[0], description= entry[4] + description, color=0xff0000)
                                        if entry[6]:
                                            embed.set_image(url= entry[6])
                                        await qmessage.edit(embed= embed)
                                else:
                                    wrongletterlist.append(fixedletter)
                                    wrongletters += fixedletter
                                    description = "``" + blank + "``\n\n" + wrongletters
                                    embed = discord.Embed(title= entry[0], description= entry[4] + description, color=0xff0000)
                                    if entry[6]:
                                        embed.set_image(url= entry[6])
                                    await qmessage.edit(embed= embed)
                await asyncio.sleep(2)
                qmessage = False
                qflag = False

            await client.get_channel(variables.hotlineID).trigger_typing()
            await asyncio.sleep(1)
            await client.get_channel(variables.hotlineID).send("``RECOVERY COMPLETE``")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await asyncio.sleep(2)
            await client.get_channel(variables.hotlineID).send("``CRITICAL ERRORS: 0``")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await client.get_channel(variables.hotlineID).send("``WARNINGS: 1``")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await asyncio.sleep(2)
            await client.get_channel(variables.hotlineID).send("``WARNING LOG: DISCORDPY ERROR -- C:/ELSECRETO LINE 211 MISMATCH WITH RECOVERY``")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await client.get_channel(variables.hotlineID).send("``LINE 211:``")
            await client.get_channel(variables.hotlineID).trigger_typing()
            await asyncio.sleep(1)
            await client.get_channel(variables.hotlineID).send("``SEE DOCUMENTATION FOR NON-CRITICAL ERROR RESOLUTION``")
            await client.get_channel(variables.modchatID).send("anh normal")

    if reaction.message == qmessage and reaction.emoji in alphabet:
        qflag = True
        if reaction.count > count:
            count = reaction.count
            letter = alphabet[reaction.emoji]

client.run(variables.musik)