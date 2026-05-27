import matplotlib.pyplot as plt

def generate_graph(results):

    algorithms = list(results.keys())
    times = list(results.values())

    plt.figure(figsize=(6,4))

    plt.bar(algorithms, times)

    plt.xlabel("Algorithms")
    plt.ylabel("Execution Time")
    plt.title("Algorithm Performance")

    graph_path = "static/charts/graph.png"

    plt.savefig(graph_path)

    plt.close()

    return graph_path