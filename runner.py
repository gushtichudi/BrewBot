from brewbot.bot import Bot
from brewbot.log import Log, Level

from time import sleep

import argparse as ap
import subprocess as sp 

import os
import sys

ps = ap.ArgumentParser(
        prog="Runner",
        description="Runner script for BrewBot"
)

ps.add_argument("--token", help="Bot's token")

def todo(msg):
    sys.stderr.write(f"!! not implemented yet - {msg}\n")

def get_token_from_env() -> str:
    if not os.getenv("BREWBOT_TOKEN"):
        raise Exception("Please declare your token environment variable as `BREWBOT_TOKEN` in order to auto infer tokens. `./sh/token.sh` will help you with that if you don't have expertise")

    return os.getenv("BREWBOT_TOKEN")

BOT_TOKEN = get_token_from_env()

def start_prompt():
    # BOT_TOKEN = get_token_from_env()

    b = Bot(BOT_TOKEN)
    status = 0

    while status == 0:
        # print("\n")
        cmd = input("bbot >> ").split(" ")

        match cmd[0]:
            case "help":
                print("List of available commands:")
                print("     run [-l, -s] - run bot")
                print("         -l [file] -   log to file")
                print("         -s        -   say f*ck you to this interface and let discord.py take over tty\n")
                print("     slp - suspend bot")
                print("    stop - stop bot")
                print("    back - run bot in background to free current tty (not implemented yet)")
                print("     sig - exit this interface")
            
            case "run":
                token = BOT_TOKEN

                if len(cmd) > 1:
                    match cmd[1]:
                        case "-l":
                            if not cmd[2]:
                                sys.stderr.write("ERROR! `run -l` needs a value!\n")

                            b.change_log_descriptor(cmd[2])

                        case "-s":
                            b.change_log_descriptor("/dev/stdout")

                        case _:
                            sys.stderr.write(f"`{cmd[1]}` is not a valid flag. Type `help` to see correct usage.")
                else:
                    b.change_log_descriptor("/dev/stdout")

                print("Starting BrewBot in 2 seconds... Press CTRL+C to stop")
                sleep(2)
                
                if not token:
                    sys.stderr.write("-- BrewBot: Token is stil (nil!) Fetching it now\n")

                    token = get_token_from_env()
                    b.run(token)
                
                b.run()
                #todo("b.run()")

            case "slp":
                print("Putting BrewBot to sleep in 2 seconds... Press CTRL+C to stop")
                sleep(2)

                # b.suspend()
                todo("b.suspend()")

            case "stop":
                print("Stopping BrewBot in 2 seconds... Press CTRL+C to stop")
                sleep(2)

                # b.stop()
                todo("b.stop()")

            case "back":
                # b.bg()
                todo("b.bg()")

            case "sig":
                status = 1

            case _:
                sys.stderr.write(f"`{cmd[0]}` is not a valid command. Type `help` for a list of available commands.\n")

def main():
    args = ps.parse_args()
    BOT_TOKEN = args.token 

    if not args.token:
        BOT_TOKEN = get_token_from_env()
   
    x = input(f"token correct?: {BOT_TOKEN}")
    if x == 'y':
        print("ok")

    if not BOT_TOKEN:
        raise ValueError("Bot token is still empty for some reason!")

    print("!!!! BREWBOT RUNNER !!!!")
    print("Copyright (c) 2025 Lamb. All Rights Reserved.\n")
    print("Type `help` to show available commands.")

    start_prompt()

if __name__ == '__main__':
    main()
