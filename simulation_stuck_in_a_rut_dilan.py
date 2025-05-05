n = int(input())
cows = []
for _ in range(n):
    d, x, y = input().split()
    cows.append({'dir': d, 'x': int(x), 'y': int(y), 'id': _, 'stopped': False, 'stop_time': float('inf'), 'stops': []})

# comparar pares de vacas
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a = cows[i]
        b = cows[j]
        if a['dir'] == b['dir']:
            continue

        # A va al norte y B al este
        if a['dir'] == 'N' and b['dir'] == 'E':
            if a['x'] > b['x'] and a['y'] < b['y']:
                dx = a['x'] - b['x']
                dy = b['y'] - a['y']
                if dx < dy and dy < a['stop_time'] and b['stop_time'] > dx:
                    a['stopped'] = True
                    a['stop_time'] = dy
                    b['stops'].append(a['id'])
                elif dy < dx and dx < b['stop_time'] and a['stop_time'] > dy:
                    b['stopped'] = True
                    b['stop_time'] = dx
                    a['stops'].append(b['id'])

        elif a['dir'] == 'E' and b['dir'] == 'N':
            if b['x'] > a['x'] and b['y'] < a['y']:
                dx = b['x'] - a['x']
                dy = a['y'] - b['y']
                if dx < dy and dy < b['stop_time'] and a['stop_time'] > dx:
                    b['stopped'] = True
                    b['stop_time'] = dy
                    a['stops'].append(b['id'])
                elif dy < dx and dx < a['stop_time'] and b['stop_time'] > dy:
                    a['stopped'] = True
                    a['stop_time'] = dx
                    b['stops'].append(a['id'])

from collections import defaultdict

tree = defaultdict(list)
for c in cows:
    for stopped in c['stops']:
        tree[c['id']].append(stopped)

def dfs(i):
    total = 0
    for j in tree[i]:
        total += 1 + dfs(j)
    return total

for i in range(n):
    print(dfs(i))
