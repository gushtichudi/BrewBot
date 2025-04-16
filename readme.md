# BrewBot

### Instructions to run bot:

1.  **Run these commands:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt # if haven't done so 
    ```

2.  **Run the shell script in sh/ to give your token**
    ```
    source sh/token.sh 
    source ~/.zshrc 
    source venv/bin/activate # IS REQUIRED OTHERWISE VENV WON'T LET THE BOT FIND THE TOKEN
    ```
    > [!WARNING]
    > THIS IS NOT AN EXAMPLE ON HOW YOU CAN RUN THE SCRIPT. YOU 
    > **ARE** REQUIRED TO RUN IT EXACTLY HOW IT'S SAID ESPECIALLY
    > IF YOU USE A DIFFERENT SHELL.

3.  **Start the bot**
    ```
    python3 runner.py 
    ```

4.  **If you've done everything correctly, write `run` in interface.**
    ```
    # python3 runner.py 
    !!!! BREWBOT RUNNER !!!!
    Copyright (c) 2025 Lamb. All Rights Reserved.
    Type `help` to show available commands.

    bbot >> run 
    Starting BrewBot in 2 seconds... Press CTRL+C to stop
    [INFO % ...]:: Starting BrewBot...
    ...
    ```
