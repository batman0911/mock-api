import sys
from flask import Flask
from app import create_app


app = create_app()


if __name__ == '__main__':

  port = sys.argv[1]
 
  app.run(host='localhost', port=port)