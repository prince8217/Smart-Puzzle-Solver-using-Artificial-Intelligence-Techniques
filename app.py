from flask import Flask, request, jsonify
from flask_cors import CORS
from algorithms.astar import astar
from algorithms.bfs import bfs
from algorithms.dfs import dfs

app = Flask(__name__)
CORS(app)

@app.route("/solve", methods=["POST"])
def solve():
    data = request.json
    state = tuple(data["state"])
    algo = data["algorithm"]

    if algo == "bfs":
        solution = bfs(state)
    elif algo == "dfs":
        solution = dfs(state)
    else:
        solution = astar(state)

    if solution:
        return jsonify({
            "steps": len(solution)-1,
            "solution": solution
        })
    else:
        return jsonify({"error": "No solution"})

if __name__ == "__main__":
    app.run(debug=True)
