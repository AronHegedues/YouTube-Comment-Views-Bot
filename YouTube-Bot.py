from lib import bot

art = """
 __   __       _____     _             ___      _   
 \ \ / /__ _  |_   _|  _| |__  ___ ___| _ ) ___| |_ 
  \ V / _ \ || || || || | '_ \/ -_)___| _ \/ _ \  _|
   |_|\___/\_,_||_| \_,_|_.__/\___|   |___/\___/\__|
   
YouTube-Bot v0.2 by Simplicitus                                              
"""

print(art)

# arguments are:
# comment?, view?, minimal viewtime, maximal viewtime, path of accounts, path of urls
bot.start(comment=True, view=True)
