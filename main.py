import os
from dotenv import load_dotenv
load_dotenv()
def print_author():
    author = os.getenv(AUTHOR)
    print (fАвтор проекта: {author})
