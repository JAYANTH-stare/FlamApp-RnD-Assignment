import json


def save_parameters(theta, M, X, error):
    with open("../outputs/parameters.txt", "w") as f:
        f.write(f"Theta : {theta:.8f}\n")
        f.write(f"M     : {M:.8f}\n")
        f.write(f"X     : {X:.8f}\n")
        f.write(f"Average Error : {error:.10f}\n")


def save_json(theta, M, X, error):
    result = {
        "theta": float(theta),
        "M": float(M),
        "X": float(X),
        "average_error": float(error),
    }

    with open("../outputs/results.json", "w") as f:
        json.dump(result, f, indent=4)