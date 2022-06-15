# ByteGate

![logo_1_31](https://user-images.githubusercontent.com/85664683/173884413-701a006b-122b-4b45-a3ca-d16dc353bcea.png)

**ByteGate** is the world first github public reverse shell listener discord bot release that can perform command through discord server. Written in Py3 and free to use developed by me and hope you guys **CTF** community enjoy this project ;) and rate us so i will release more project in the future

## Installation and usage:
To install libraries
```
git clone https://github.com/OnTheCodeOfficial/ByteGate.git
cd ByteGate/
pip install -i requirements.txt
```
And then setup your **config.json** file

To run

- **Windows** : `python ByteGate.py`
- **Linux** : `python3 ByteGate.py`


## Bot commands

| Command  | Argument |
| ------------- | ------------- |
| $lvnp  | [port] [private or public]  |
| $clean  | [number]  |
| $bot_ip  | None  |

Both `$lvnp` and `$clean` commands can perform with no argument it will use default setting

## Example:

`$lvnp` --> *Start listener with default port on private user*

`$lvnp help` --> *Get guide "how to use advance command"*

`$lvnp 1234` --> *Start listener with port 1234 on private user*

`$lvnp 1234 public` --> *Start listener with port 1234 on public user 

[ Anyone with whitelist role will be able to perform command on the reverse shell ] while perform shell as public

`$bot_ip` --> To get the bot-host IPv4 information

`$clean` --> Clean the channel message default set to 100 without argument

`$clean 200` --> remove 200 messages from the current channel

`bg.stop` --> while reverse shell connected use this to stop the port listener and end the session

`.b` --> while reverse shell connected use this to send blank space message

`bg.clear` --> while reverse shell connected use this to clear the channel message

## Review:

https://user-images.githubusercontent.com/85664683/173884542-6083c44e-f5fe-4d50-bb77-a111cf17ddd3.mp4

## Config.json:
```
Required the Channel-ID can be 1 or more channel the channel ID for config the bot react to specific channel.
Required the Role-ID can be 1 or more role. Only the user that have the specify role are allowed to use bot.
```
```
Default port is set to 25564 for legit minecraft reverse-shell that i created but you can chage it any port you wish.
The delay between command default is set to 2 seconds
The port listener timeout default is set to 120 seconds
```
![config](https://user-images.githubusercontent.com/85664683/173884739-9e1e1ca4-fe54-47e9-a97f-c5107bef60be.png)

## Support

> **How to get the role ID?** : 
https://www.youtube.com/watch?v=Q8eOA9ZYyGw

> **How to get the channel ID ?** : 
https://www.youtube.com/watch?v=YjiQ7CajAgg

> **How to edit & modify json file ?** : 
https://www.youtube.com/watch?v=iiADhChRriM

## If you downloaded this project please rate us.

![Rate-Us-Transparent-Images-PNG](https://user-images.githubusercontent.com/85664683/173891419-c3169cd2-69a4-4dd6-9a24-5c16103b9d24.png)




