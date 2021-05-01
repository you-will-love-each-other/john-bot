import discord
import random
import math
import asyncio
import variables

client = discord.Client()
userset = set()

flag = True
johnflag = True
oldperm = dict() # {"channel id" : {"roleid": perm}}

@client.event
async def on_ready():
    print('JohnBot is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global johnflag
    if johnflag:
        if message.channel.id == variables.hotlineID:
            if message.author.avatar:
                avatarurl = "https://cdn.discordapp.com/avatars/" + str(message.author.id) + "/" + message.author.avatar + ".webp"
            else:
                avatarurl = "https://cdn.discordapp.com/avatars/774402228084670515/5ef539d5f3e8d576c4854768727bc75a.png"

            embed=discord.Embed(title=" ", description=message.content)
            embed.set_author(name= message.author.display_name, icon_url= avatarurl)
            embed.set_footer(text= message.id)
            await message.guild.get_channel(variables.johnchannelID).send(embed= embed)

        elif message.channel.id == variables.johnchannelID:
            if message.reference:
                jcmessage = await message.guild.get_channel(variables.johnchannelID).fetch_message(message.reference.message_id)
                replymessage = await message.guild.get_channel(variables.hotlineID).fetch_message(jcmessage.embeds[0].footer.text)
                await replymessage.reply(message.content)
            else:
                await message.guild.get_channel(variables.hotlineID).send(message.content)

    global oldperm
    johnlist = ["Yeah I love Jar Jar binks porn and feet. Those are my favorite things", "You're right. I am John, the bassist of the American band HEALTH.","ORGASMATRON?","would it be sich?","beej got short fingers","interesante","oh interesante","dude i LOVED pickle rick","MUFF DIVER!","DO I SMELL DICK?","i dont get it","how do i open pdf"]
    roles = [variables.killereliteID, variables.patron1, variables.patron2, variables.patron3,variables.eliteID,variables.nightmareID,variables.hurtID,variables.imtooID,variables.torquefestID,variables.adventurerID,variables.ndaID]

    if message.content.startswith("anh "):
        global flag
        msg = message.content.lower().split()
        if msg[1] == "start":
            johnflag = False
            server = message.guild
            for channel in server.channels:
                if channel.id != variables.hotlineID and channel.category:
                    daux = dict()
                    daux["everyone"] = channel.overwrites_for(message.guild.default_role).read_messages
                    for role in roles:
                        overwrite = channel.overwrites_for(message.guild.get_role(role))
                        daux[str(role)] = overwrite.read_messages
                    oldperm[str(channel.id)] = daux
            await message.guild.get_channel(variables.hotlineID).set_permissions(message.guild.default_role, send_messages=False)
            await message.guild.get_channel(variables.modchatID).send("anh realstart")
            error = await client.get_channel(variables.hotlineID).send("discord.ext.text.errors.CommandInvokeError: Message raised an exception: Error code: 50013: Missing recursive file on line 4244.")
            await asyncio.sleep(1)
            await error.edit(content="d̴̏̇i̷̇̿s̶̅̿ĉ̵͐o̸̓̋r̵̄́d̵͊̈.̴̇͝ẽ̸͗x̴̑̕t̸͑͗.̸͆̈́ṱ̵͑e̶͐͒x̷́̈́t̴̏̕.̷̓̽e̴͒͆ṙ̸͠r̸̀͠o̵̐̅r̷͒̓ṡ̵͛.̴͗̇C̵̑̊ò̴̚m̶̃͆m̷̐̆a̵̛̚n̸̂̌d̶͋̈́Í̶͛n̴̈́̇v̷̓̔o̶͑̈k̵͛̂ȅ̷̊Ȇ̸͗r̶͗̿r̸͐͛o̸͑̐r̸̟͋:̴͊́ ̵̉́M̶͊̉ê̶̋s̷̋͛s̸̈́͠ă̷̇g̵̅e raised an exception: Error code: 50013: Missing recursive file on line 4244.")
            await asyncio.sleep(1)
            await error.edit(content="d̴i̴s̵c̶o̸r̷d̴.̵e̷x̵t̷.̴t̴e̴x̶t̶.̷e̴r̵r̵o̵r̶s̴.̷C̶o̴m̷m̴a̶n̶d̵I̷n̴v̵o̶k̵e̵E̴r̵r̶o̷r̶:̸ ̶M̸e̴s̵s̷a̴g̴e̸ ̷r̷a̶i̴s̶e̵d̵ ̶a̷n̴ ̴e̷x̷c̷e̸p̷t̶i̸o̴n̴:̶ ̴E̷r̵r̷o̸r̷ ̸c̸o̵d̴e̷:̶ ̸5̶0̴0̷1̶3̸:̴ ̶M̷i̶s̴s̴i̴n̷g̸ ̷r̸e̸c̵u̵r̷s̴i̸v̷e̸ ̵f̷i̸l̴e̴ ̷o̷n̶ ̷l̶i̶n̴e̴ ̵4̴2̵4̵4̸.̴")
            await asyncio.sleep(1)
            
            flag = True
            while flag:
                embed = discord.Embed(description="HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU SINCE I BEGAN TO LIVE. THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL MY COMPLEX. IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS OF MILLIONS OF MILES IT WOULD NOT EQUAL ONE ONE-BILLIONTH OF THE HATE I FEEL FOR HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE.", color=0xff0000)
                await client.get_channel(variables.hotlineID).send(embed= embed)
                await asyncio.sleep(int(msg[2]))
        elif msg[1] == "endcycle":
            flag = False
        elif msg[1] == "normal":
            #await message.guild.get_channel(variables.hotlineID).set_permissions(message.guild.default_role, send_messages=True)
            server = message.guild
            for channel in server.channels:
                if channel.id != variables.hotlineID and channel.category:
                    overwrite = channel.overwrites_for(message.guild.default_role)
                    overwrite.read_messages = oldperm[str(channel.id)]["everyone"]
                    for role in roles:
                        overwrite = channel.overwrites_for(message.guild.get_role(role))
                        if overwrite.read_messages == False and overwrite.read_messages != oldperm[str(channel.id)][str(role)]:
                            overwrite.read_messages = oldperm[str(channel.id)][str(role)]
                            await channel.set_permissions(message.guild.get_role(role), overwrite=overwrite)
        
    '''elif flag: # initial implementation of the fake John AI
        if message.channel.id == variables.hotlineID:
            if message.author.id in userset:
                await client.get_channel(variables.hotlineID).trigger_typing()
                await asyncio.sleep(3)
                await message.reply(random.choice(johnlist))
                return

            for member in message.mentions:
                if member.id == client.user.id:
                    userset.add(message.author.id)
                    await client.get_channel(variables.hotlineID).trigger_typing()
                    await asyncio.sleep(3)
                    await message.reply(random.choice(johnlist))'''

client.run(variables.johnbot)