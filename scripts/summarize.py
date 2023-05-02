import sys
import json
import collections

def find_label(labeling, n):
    for [node, label] in labeling:
        if node == n:
            return label
    return None

def find_labels(n):
    return [l for l in list(set([find_label(solution['labeling'], n) for solution in data['solutions']])) if l]

def migration(tree, labeling):
    return [(find_label(labeling, u), find_label(labeling, v)) for [u, v] in tree]

def migration_nodups(tree, labeling):
    return list(set(migration(tree, labeling)))

def migration_summary(solutions):
    G = [migration_nodups(solution['tree'], solution['labeling']) for solution in solutions]
    G = [element for array in G for element in array]
    G = [[u, v] for [u, v] in G if (u != v and u and v)]
    G = [tuple(e) for e in G]
    G = collections.Counter(G)
    return [[u, v, w] for (u, v), w in G.items()]

# Example JSON file path
json_file = sys.argv[1]

# Open the JSON file and load the data as a Python object
with open(json_file, 'r') as f:
    data = json.load(f)

data['summary'] = {
    'migration': migration_summary(data['solutions'])
}

with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)
