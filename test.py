import itertools

lst = ('A', 'B', 'C', 'D')

possible = list(itertools.permutations(lst))
st = set(possible)
print(lst[-1])
left, right = lst[-1], lst[1]
adjacentPairs = sorted((left, right))
adjacentPairs.append(sorted((lst[0], lst[2])))
for i in possible:
    ind = i.index('A')
    l, r = i[(ind-1) % 4], i[(ind+1) % 4]
    p = sorted((l, r))
    ind = i.index('B')
    p.append(sorted((i[(ind-1) % 4], i[(ind+1) % 4])))
    if adjacentPairs == p:
        st.remove(i)
print(len(st))