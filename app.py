from flask import Flask,jsonify
import random

app = Flask(__name__)

facts = {
    "programming": [
        "Python was named after Monty Python.",
        "Java was initially called Oak.",
        "The first computer bug was a moth.",
    ],
    "history": [
        "Napoleon was once attacked by rabbits.",
        "The Eiffel Tower can grow taller in summer.",
        "The shortest war in history lasted 38 minutes.",
    ],
    "motivation": [
        "Dream big. Start small. Act now.",
        "Success is no accident.",
        "Push yourself, because no one else will do it for you.",
    ]
}

@app.route("/fact/<category>",methods=["GET"])
def get_fact(category):
    if category not in facts:
        return jsonify({"error": "category not found"}),404
    return jsonify({
        "category": category,
        "fact": random.choice(facts[category])
    })

@app.route("/",methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to FactZone! Try /fact/programming or /fact/motivation"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)