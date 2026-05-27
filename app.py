from flask import Flask,render_template, request
import os
import time

from algorithms.naive import naive_search
from algorithms.kmp import kmp_search
from algorithms.rabin_karp import rabin_karp_search

from utils.file_reader import read_file
from utils.graph_generator import generate_graph

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():

    file = request.files["file"]
    pattern = request.form["pattern"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = read_file(filepath)

    results = {}

    # NAIVE
    start = time.time()
    naive_result = naive_search(text, pattern)
    naive_time = time.time() - start

    # KMP
    start = time.time()
    kmp_result = kmp_search(text, pattern)
    kmp_time = time.time() - start

    # RABIN KARP
    start = time.time()
    rk_result = rabin_karp_search(text, pattern)
    rk_time = time.time() - start

    results["Naive"] = naive_time
    results["KMP"] = kmp_time
    results["Rabin-Karp"] = rk_time

    graph_path = generate_graph(results)

    return render_template(
        "result.html",
        pattern=pattern,
        naive=naive_result,
        kmp=kmp_result,
        rk=rk_result,
        naive_time=round(naive_time, 6),
        kmp_time=round(kmp_time, 6),
        rk_time=round(rk_time, 6),
        graph=graph_path
    )

if __name__ == "__main__":
    app.run(debug=True)