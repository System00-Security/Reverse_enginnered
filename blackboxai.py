import sys
import requests
import re
from colorama import Fore, Back, Style
import pygments
from pygments import lexers, formatters


class BlackBoxAI:
    @staticmethod
    def send_msg(msg):
        endpoint = "https://www.useblackbox.io/chat-request-v4"
        headers = {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.useblackbox.io",
            "Referer": "https://www.useblackbox.io/chat?q=Connect%20to%20mongodb%20in%20nodejs",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9"
        }
        json_data = {
            "textInput": msg,
            "allMessages": [
                {
                    "user": msg
                }
            ],
            "stream": "",
            "clickedContinue": False
        }
        try:
            response = requests.post(endpoint, headers=headers, json=json_data)
            return response.json()["response"][0][0]
        except Exception as e:
            return "Hi, I am Not a Regular ChatBot, I only Can Generate code Based on your Instructions."


class Code:
    @staticmethod
    def highlight(code):
        lexer = lexers.guess_lexer(code, stripall=True)
        formatter = formatters.TerminalFormatter(style='monokai', bg='light', fg='green')
        highlighted_code = pygments.highlight(code, lexer, formatter)
        return highlighted_code



class MainTask:
    @staticmethod
    def process(user_msg):
        try:
            black_box_response = BlackBoxAI.send_msg(user_msg)
            lreplace = re.sub(r"```.*", "```", black_box_response)
            filter = lreplace.split("```")[1]
            print("----")
            print(Code.highlight(filter))
        except Exception as e:
            print("----")
            print("CodeAI >>> Hi, I am Not a Regular ChatBot, I only Can Generate code Based on your Instructions.")
        

class chat:
    @staticmethod
    def start():
        while True:
            print("----")
            user_msg = input(">>> ")
            if user_msg == "exit":
                sys.exit()
            else:
                MainTask.process(user_msg)

print(f"""

  _______      ___   ____
 / ___/ / ____/ _ | /  _/
/ /__/ /_/___/ __ |_/ /  
\___/____/  /_/ |_/___/ {Fore.BLUE}@system00-Security{Fore.RESET}
{Fore.CYAN}----{Fore.RESET}
-> {Fore.RED}Reversed Engineered{Fore.GREEN} Code Generation AI{Fore.RESET}
""")
chat.start()



