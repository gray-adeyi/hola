"""
 _   _  _____  __      __      ___   ___  ____  ____  ____  ____ 
( )_( )(  _  )(  )    /__\    / __) / __)(  _ \(_  _)(  _ \(_  _)
 ) _ (  )(_)(  )(__  /(__)\   \__ \( (__  )   / _)(_  )___/  )(  
(_) (_)(_____)(____)(__)(__)  (___/ \___)(_)\_)(____)(__)   (__) 

version 0.1.0
author: Gbenga Adeyi <adeyigbenga005@gmail.com>
"""
ENABLE_COLOR = True
COLOR = "\033[0;37;42m"

def run() -> None:
    with open("data.txt","r") as f:
        if ENABLE_COLOR:
            print_text = COLOR + f.read()
        else:
            print_text = f.read()
        print(print_text)


if __name__ == "__main__":
    run()
