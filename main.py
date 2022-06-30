import discord
import os

"""
- reminder to pay rent @ing each person specifially when they don't pay
- automatic printing
- trash/recycle day 
"""


def main():
    client = discord.Client()
    # load_dotenv()
    client.run(os.getenv('TOKEN'))
    print("testing")

if __name__ == "__main__":
    main()