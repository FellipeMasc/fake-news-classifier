from jose import jwe
import os
import dotenv
dotenv.load_dotenv()


def main():
    jwe.encrypt("Hello, World!", os.environ["encrypt_key"])