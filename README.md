# ByteGate

![logo_1_31](https://user-images.githubusercontent.com/85664683/173884413-701a006b-122b-4b45-a3ca-d16dc353bcea.png)

ByteGate is the world first github public reverse shell discord bot release that can perform command through discord server.

## Commands

| Command  | Argument | Description |
| ------------- | ------------- | ------------- |
| $lvnp  | [port] [private or public]  | with no argument it will listen on default port and private commander|
| $clean  | [number]  | with no argument it will clean 100 messages on specific channel|

`$lvnp` --> *Start listener with default port on private user*

`$lvnp help` --> *Get guide "how to use advance command"*

`$lvnp 1234` --> *Start listener with port 1234 on private user*

`$lvnp 1234 public` --> *Start listener with port 1234 on public user 

[ Anyone with whitelist role will be able to perform command on the reverse shell ] while public

`$bot_ip` --> To get the host IPv4 information

`$clean` --> Clean the channel message default set to 100 without argument

`$clean 200` --> remove 200 messages from the current channel

`bg.stop` --> while reverse shell connected use this to stop the port listener and end the session

`.b` --> while reverse shell connected use this to send blank space message

`bg.clear` --> while reverse shell connected use this to clear the channel message







#### Review:

https://user-images.githubusercontent.com/85664683/173884542-6083c44e-f5fe-4d50-bb77-a111cf17ddd3.mp4

#### Config.json:
```
Required the Channel-ID can be 1 or more channel the channel ID for config the bot react to specific channel.
Required the Role-ID can be 1 or more role. Only the user that have the specify role are allowed to use bot.
```
```
Default port is set to 25565 for legit minecraft reverse-shell that i created but you can chage it any port you wish.
The delay between command default is set to 2 seconds
The port listener timeout default is set to 120 seconds
```
![config](https://user-images.githubusercontent.com/85664683/173884739-9e1e1ca4-fe54-47e9-a97f-c5107bef60be.png)


