import itertools

squares = map(pow, range(5), itertools.repeat(2))  # iterable(also iterator) obj, list(squares) -> [0, 1, 4, 9, 16, 25]

letters = ['a', 'b', 'c']
comb_result = itertools.combinations(letters, 2)   # list(comb_result) -> [('a', 'b'), ('a', 'c'), ('b', 'c')]
perm_res = itertools.permutations(letters, 3)      # list(perm_res) -> [('a', 'b'), ('b', 'a'), ...] (order matters)
pass