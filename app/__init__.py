from flask import Flask


def create_app():
  app = Flask(__name__)
  register_blueprints(app)
  
  return app
  
  
def register_blueprints(app):
  from app.routes import route
  app.register_blueprint(route.blueprint, url_prefix='/api/v1')
  