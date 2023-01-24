"""
made by zenci 
"""
print("""
                                                                                                 
                         _                            _        
                       (_)               _          | |       
 ____    ____   ___     _   ____   ____ | |_      _ | | _ _ _ 
|  _ \  / ___) / _ \   | | / _  ) / ___)|  _)    / || || | | |
| | | || |    | |_| |  | |( (/ / ( (___ | |__   ( (_| || | | |
| ||_/ |_|     \___/  _| | \____) \____) \___)   \____| \____|
|_|                  (__/                                                          
                                    Made by zenci#0192
                                  Github: huryyryrs
""")

from dhooks import Webhook
import time

message = input("what do you want to spam nigga: ")
webhookurl = Webhook(input("enter webhook nigga its not hard: "))

while True:
    webhookurl.send(message)
    print("Sent.")
