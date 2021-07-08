import random

from app import app
from services.FactParser import FactParser


@app.route('/', methods=["GET"])
def main():
    return random.choice(FactParser.getAllFacts())