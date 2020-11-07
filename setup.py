import os
import argparse


class BaseSettings():
    def __init__(self):
        self.ENV: str = None
        self.PORT: int = None
        self.HOST: str = None

    def start(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-env", default="dev",
                            help="Set environment's variables")
        args = parser.parse_args()

        if args.env == "dev":
            print("\n- detected development environment\n\n")
            return DevSettings()
        if args.env == "prod":
            print("\n- detected production environment\n\n")
            return ProdSettings()


class DevSettings():
    def __init__(self):
        self.ENV = "development"
        self.PORT = 5000
        self.HOST = '127.0.0.1'
        self.GO_SERVER = "https://verte-auth-server.herokuapp.com/"


class ProdSettings(BaseSettings):
    def __init__(self):
        self.ENV = "production"
        self.PORT = os.environ.get('PORT')
        self.HOST = '0.0.0.0'
        self.GO_SERVER = "https://verte-auth-server.herokuapp.com/"
