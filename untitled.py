import discord
import re
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import math
Client = discord.Client()

@Client.event
async def on_ready():
        print("logged in as: ")
        print(Client.user.name)
        print("ID: ")
        print(Client.user.id)
        print("ready to use!")

@Client.event
async def on_message(message):
        if message.author == Client.user:
                return
        elif message.content == "!ping":
                await Client.send_message(message.channel,"pong!")
        elif message.content == "!":
                x = random.randint(1,20)
                await Client.send_message(message.channel,x)
        elif message.content == "!developer":
                await Client.send_message(message.channel,"Developer of this Bot is Gandalf. Here is my Discord server: https://discord.gg/3fnvP7z")
        elif message.content.startswith("(") and message.content.endswith(")"):
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                if len(a) == 2:
                        rolls = []
                        sumrolls = 0
                        while a[0] != 0:
                                x = random.randint(1,a[1])
                                sumrolls += x
                                rolls.append(x)
                                a[0] -= 1
                        if len(rolls) > 1:
                                rollsstr = "+".join(str(x) for x in rolls)+" = " + str(sumrolls)
                        else:
                                rollsstr = "+".join(str(x) for x in rolls)
                        await Client.send_message(message.channel, rollsstr)
                elif len(a) == 3:
                        if '+' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                rolls.append(mod)
                                sumrolls += mod
                                rollsstr = "+".join(str(x) for x in rolls)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, rollsstr)
                        elif '-' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls -= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"-"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, rollsstr)
                        elif '*' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls *= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"*"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, rollsstr)
                        elif '/' in message.content:
                                mod = a[2]
                                rolls = []
                                sumrolls = 0
                                while a[0] != 0:
                                        x = random.randint(1,a[1])
                                        sumrolls += x
                                        rolls.append(x)
                                        a[0] -= 1
                                sumrolls /= mod
                                rollsstr = "+".join(str(x) for x in rolls)+"/"+str(mod)+" = "+str(sumrolls)
                                await Client.send_message(message.channel, rollsstr)
        elif message.content.startswith("!"):
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                value1 = a[0]
                o = 3
                if len(a) == 4:
                        value2 = a[1]
                        value3 = a[2]
                        value4 = a[3]
                        checkfor1 = 0
                        checkfor20 = 0
                        rolls = []
                        while o != 0:
                                x = random.randint(1,20)
                                rolls.append(x)
                                if x == 1:
                                        checkfor1 += 1
                                elif x == 20:
                                        checkfor20 += 1
                                o -= 1
                        roll1 = rolls[0]
                        roll2 = rolls[1]
                        roll3 = rolls[2]
                        while roll1 > value1:
                                value4 -= 1
                                roll1 -= 1
                        while roll2 > value2:
                                value4 -= 1
                                roll2 -= 1
                        while roll3 > value3:
                                value4 -= 1
                                roll3 -= 1
                        qualitylevel = value4/3
                        qualitylevel1 = math.ceil(qualitylevel)

                        rollsstrf = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==>"+" Failed!"
                        rollsstrs = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> Succeded!" + " \nQuality Level: "+str(qualitylevel1)
                        if checkfor1 == 2 or checkfor1 == 3:
                                rollsstrc = "Your rolls: " + ",".join(str(x) for x in rolls) + " ==> CRITICAL SUCCESS!"
                                await Client.send_message(message.channel, rollsstrc)
                        elif checkfor20 == 2 or checkfor20 == 3:
                                rollsstrb = "Your rolls: " + ",".join(str(x) for x in rolls) + " ==> BOTCH!"
                                await Client.send_message(message.channel, rollsstrb)
                        elif value4 == 0:
                                qualitylevel1 = 1
                                rollsstrs = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> Succeded!" + " \nQuality Level: "+str(qualitylevel1)
                                await Client.send_message(message.channel, rollsstrs)
                        elif value4 > 0:
                                await Client.send_message(message.channel, rollsstrs)
                        elif value4 < 0:
                                await Client.send_message(message.channel, rollsstrf)

                elif len(a) == 1:
                        rolls = []
                        x = random.randint(1,20)
                        checkfor1 = 0
                        checkfor20 = 0
                        m_success = "Your roll: "+str(x)+" ==> Succeeded!"
                        m_failure = "Your roll: "+str(x)+" ==> Failed!"
                        if x < a[0] and x != 1:
                                await Client.send_message(message.channel, m_success)
                        elif x == a[0]:
                                await Client.send_message(message.channel, m_success)
                        elif x > a[0]and x!= 20:
                                await Client.send_message(message.channel, m_failure)
                        elif x == 20:
                                rolls.append(x)
                                x = random.randint(1,20)
                                rolls.append(x)
                                if  x > a[0]:
                                        rollsstr= "Your roll: " +str(rolls[0])+ " Check for Botch: " +str(rolls[1])+ " ==> BOTCH"
                                        await Client.send_message(message.channel, rollsstr)
                                else:
                                        rollsstr="Your roll: "+str(rolls[0])+" Check for Botch: "+str(rolls[1])+" ==> Failed"
                                        await Client.send_message(message.channel, rollsstr)
                        elif x == 1:
                                rolls.append(x)
                                x = random.randint(1,20)
                                rolls.append(x)
                                if  x < a[0]:
                                        rollsstr= "Your roll: " +str(rolls[0])+ " Check for Critical success: " +str(rolls[1])+ " ==> CRITICAL SUCCESS"
                                        await Client.send_message(message.channel, rollsstr)
                                else:
                                        rollsstr="Your roll: "+str(rolls[0])+" Check for Critical success: "+str(rolls[1])+" ==> Success"
                                        await Client.send_message(message.channel, rollsstr)
                elif len(a) == 5:
                        if '+' in message.content:
                                value4 = a[3]
                                att1 = a[0] + a[4]
                                att2 = a[1] + a[4]
                                att3 = a[2] + a[4]
                                checkfor1 = 0
                                checkfor20 = 0
                                rolls = []
                                while o != 0:
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if x == 1:
                                                checkfor1 += 1
                                        elif x == 20:
                                                checkfor20 += 1
                                        o -= 1
                                roll1 = rolls[0]
                                roll2 = rolls[1]
                                roll3 = rolls[2]
                                while roll1 > att1:
                                        value4 -= 1
                                        roll1 -= 1
                                while roll2 > att2:
                                        value4 -= 1
                                        roll2 -= 1
                                while roll3 > att3:
                                        value4 -= 1
                                        roll3 -= 1
                                qualitylevel = value4/3
                                qualitylevel1 = math.ceil(qualitylevel)
                                rollsstrf = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==>"+" Failed!"
                                rollsstrs = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> Succeded!" + " \nQuality Level: "+str(qualitylevel1)
                                if checkfor1 == 2 or checkfor1 == 3:
                                        rollsstrc = "Your rolls: " + ",".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> CRITICAL SUCCESS!"
                                        await Client.send_message(message.channel, rollsstrc)
                                elif checkfor20 == 2 or checkfor20 == 3:
                                        rollsstrb = "Your rolls: " + ",".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> BOTCH!"
                                        await Client.send_message(message.channel, rollsstrb)
                                elif value4 == 0:
                                        qualitylevel = 1
                                        rollsstrs = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> Succeded!" + " \nQuality Level: "+str(qualitylevel1)
                                        await Client.send_message(message.channel, rollsstrs)
                                elif value4 > 0 or value4 == 0:
                                        await Client.send_message(message.channel, rollsstrs)
                                elif value4 < 0:
                                        await Client.send_message(message.channel, rollsstrf)
                        elif '-' in message.content:
                                value4 = a[3]
                                att1 = a[0] - a[4]
                                att2 = a[1] - a[4]
                                att3 = a[2] - a[4]
                                checkfor1 = 0
                                checkfor20 = 0
                                rolls = []
                                while o != 0:
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if x == 1:
                                                checkfor1 += 1
                                        elif x == 20:
                                                checkfor20 += 1
                                        o -= 1
                                roll1 = rolls[0]
                                roll2 = rolls[1]
                                roll3 = rolls[2]
                                while roll1 > att1:
                                        value4 -= 1
                                        roll1 -= 1
                                while roll2 > att2:
                                        value4 -= 1
                                        roll2 -= 1
                                while roll3 > att3:
                                        value4 -= 1
                                        roll3 -= 1
                                qualitylevel = value4/3
                                qualitylevel1 = math.ceil(qualitylevel)
                                rollsstrf = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> Failed!"
                                rollsstrs = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> Succeded!" + " \nQuality Level: "+str(qualitylevel1)
                                if checkfor1 == 2 or checkfor1 == 3:
                                        rollsstrc = "Your rolls: " + ",".join(str(x) for x in rolls) + " ==> CRITICAL SUCCESS!"
                                        await Client.send_message(message.channel, rollsstrc)
                                elif checkfor20 == 2 or checkfor20 == 3:
                                        rollsstrb = "Your rolls: " + ",".join(str(x) for x in rolls) + " ==> BOTCH!"
                                        await Client.send_message(message.channel, rollsstrb)
                                elif value4 == 0:
                                        qualitylevel = 1
                                        rollsstrs = "Your rolls: " + ", ".join(str(x) for x in rolls) + " \nSkillpoints remaining: " + str(value4) + " ==> Succeded!" + " \nQuality Level: "+str(qualitylevel1)
                                        await Client.send_message(message.channel, rollsstrs)
                                elif value4 > 0 or value4 == 0:
                                        await Client.send_message(message.channel, rollsstrs)
                                elif value4 < 0:
                                        await Client.send_message(message.channel, rollsstrf)
                elif len(a) == 2:
                        if '+' in message.content:
                                rolls = []
                                x = random.randint(1,20)
                                newval = a[0] + a[1]
                                checkfor1 = 0
                                checkfor20 = 0
                                m_success = "Your roll: "+str(x)+" ==> Succeeded!"
                                m_failure = "Your roll: "+str(x)+" ==> Failed!"
                                if x < newval and x != 1:
                                        await Client.send_message(message.channel, m_success)
                                elif x == newval:
                                        await Client.send_message(message.channel, m_success)
                                elif x > newval and x!= 20:
                                        await Client.send_message(message.channel, m_failure)
                                elif x == 20:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x > newval:
                                                rollsstr= "Your roll: " +str(rolls[0])+ " Check for Botch: " +str(rolls[1])+ " ==> BOTCH"
                                                await Client.send_message(message.channel, rollsstr)
                                        else:
                                                rollsstr="Your roll: "+str(rolls[0])+" Check for Botch: "+str(rolls[1])+" ==> Failed"
                                                await Client.send_message(message.channel, rollsstr)
                        elif '-' in message.content:
                                rolls = []
                                x = random.randint(1,20)
                                newval = a[0] - a[1]
                                checkfor1 = 0
                                checkfor20 = 0
                                m_success = "Your roll: "+str(x)+" ==> Succeeded!"
                                m_failure = "Your roll: "+str(x)+" ==> Failed!"
                                if x < newval and x != 1:
                                        await Client.send_message(message.channel, m_success)
                                elif x == newval:
                                        await Client.send_message(message.channel, m_success)
                                elif x > newval and x!= 20:
                                        await Client.send_message(message.channel, m_failure)
                                elif x == 20:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x > newval:
                                                rollsstr= "Your roll: " +str(rolls[0])+ " Check for Botch: " +str(rolls[1])+ " ==> BOTCH"
                                                await Client.send_message(message.channel, rollsstr)
                                        else:
                                                rollsstr="Your roll: "+str(rolls[0])+" Check for Botch: "+str(rolls[1])+" ==> Failed"
                                                await Client.send_message(message.channel, rollsstr)
                                elif x == 1:
                                        rolls.append(x)
                                        x = random.randint(1,20)
                                        rolls.append(x)
                                        if  x < a[0]:
                                                rollsstr= "Your roll: " +str(rolls[0])+ " Check for Critical success: " +str(rolls[1])+ " ==> CRITICAL SUCCESS"
                                                await Client.send_message(message.channel, rollsstr)
                                        else:
                                                rollsstr="Your roll: "+str(rolls[0])+" Check for Critical success: "+str(rolls[1])+" ==> Success"
                                                await Client.send_message(message.channel, rollsstr)
        elif message.content.startswith('*'):
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                if len(message.content) in range(2,4):
                        x = random.randint(1,100)
                        hard1 = a[0]/2
                        hard = math.ceil(hard1)
                        crit1 = a[0]/5
                        crit = math.ceil(crit1)
                        if x < crit or x == crit:
                                 answer = "Your roll: "+str(x)+" ==> CRITICAL SUCCESS"
                                 await Client.send_message(message.channel, answer)
                        elif x < hard or x == crit:
                                answer = "Your roll: "+str(x)+" ==> HARD SUCCESS"
                                await Client.send_message(message.channel, answer)
                        elif x < a[0] or x == a[0]:
                                answer = "Your roll: "+str(x)+" ==> SUCCESS"
                                await Client.send_message(message.channel, answer)
                        elif x >a[0]:
                                answer = "Your roll: "+str(x)+" ==> Failed"
                                await Client.send_message(message.channel, answer)
        elif message.content.startswith('+'):
                a = [int(num) for num in re.findall(r"\d+", message.content)]
                rolls = []
                successcount = 0
                botchcount = 0
                botchcheck = a[0]/2
                while a[0] != 0:
                        x = random.randint(1,6)
                        rolls.append(x)
                        if x == 5 or x == 6:
                                successcount += 1
                        elif x == 1:
                               botchcount += 1
                        a[0] -= 1
                answer = "Your rolls: "+",".join(str(x) for x in rolls)+" ==> "+str(successcount)+" success(es)"
                if botchcount < botchcheck:
                        await Client.send_message(message.channel,answer)
                elif botchcount > botchcheck and successcount == 0:
                        answer = "Your rolls: "+",".join(str(x) for x in rolls)+" ==> CRITICAL BOTCH!"
                        await Client.send_message(message.channel,answer)
                elif botchcount > botchcheck:
                        answer = "Your rolls: "+",".join(str(x) for x in rolls)+" ==> BOTCH! "+str(successcount)+" success(es)"
                        await Client.send_message(message.channel,answer)

        elif message.content == '%help' :
                await Client.send_message(message.channel, "Common Commands: \n -`(<how many dices?>d<how many sides>)` lets you roll various dices. you can even add, multiply, subtract, or divide a number from the sum of all dices. EXAMPLE: (3d6+5) \n - `!` rolls 1d20 \n\n The Dark eye Commands:\n\n- `!<attribute>` lets you roll for a specific attribute. You can even add a modifier. EXAMPLE: !13,+2 \n- `!<attribute>,<attribute>,<attribute>,<skill value>` lets you roll for a Skill. You can even add a modifier. EXAMPLE: !13,14,13,5,-3 \n\nCall of Cthulhu Commands:\n\n- `*<Skill>` lets you roll for a skill. EXAMPLE: *50")




Client.run("NDMxNzk3MDY0MjM4NzU5OTM3.DakJXg.gu8eWyH0iwU7S842H7W2RTAjrsw")
