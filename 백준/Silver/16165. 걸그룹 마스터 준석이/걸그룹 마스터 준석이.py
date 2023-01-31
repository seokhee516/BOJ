n, m = map(int, input().split())
hash = {}
for _ in range(n):
    team = input().strip()
    team_num = int(input())
    for _ in range(team_num):
        member = input().strip()
        if team not in hash:
            hash[team] = hash.get(team, [])
        hash[team].append(member)

for _ in range(m):
    question = input().strip()
    op = int(input())
    if op:
        for team in hash:
            if question in hash[team]:
                res = hash[team]
                break
        print(team)
    else:
        sort_team = sorted(hash[question])
        for mem in sort_team:
            print(mem)