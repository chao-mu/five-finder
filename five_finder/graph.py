from collections import deque

def generate_paths(start, target, q, operations):
    q.put([(start, "START")])

    paths = {}
    exits = set()
    seen = set()
    while not q.empty():
        path = q.get()
        a = path[-1][0]

        seen.add(a)

        for b in seen:
            for op in operations:
                new_path = list(path)
                res, symbol = op(a, b)
                if res is None or res == 0:
                    continue

                if res in seen:
                    continue

                pair = (res, f"{symbol} {b}")
                new_path.append(pair)
                if res == target:
                    yield shift_path(new_path)
                    continue

                q.put(new_path)

def shift_path(path):
    path = deque(path)
    new_path = [path.popleft()]
    while path:
        x, op = path.popleft()
        last_x, last_op = new_path[-1]
        new_path[-1] = (last_x, op)
        new_path.append((x, ""))

    return new_path

