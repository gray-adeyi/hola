"""
 _   _  _____  __      __      ___   ___  ____  ____  ____  ____ 
( )_( )(  _  )(  )    /__\    / __) / __)(  _ \(_  _)(  _ \(_  _)
 ) _ (  )(_)(  )(__  /(__)\   \__ \( (__  )   / _)(_  )___/  )(  
(_) (_)(_____)(____)(__)(__)  (___/ \___)(_)\_)(____)(__)   (__) 

version 0.1.0
author: Gbenga Adeyi <adeyigbenga005@gmail.com>
"""


def main() -> None:
    with open("data.txt","r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
