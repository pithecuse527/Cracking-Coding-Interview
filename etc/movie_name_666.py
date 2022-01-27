N = int(input())
movie_names = [0] * (N+1)
movie_names[1] = 666

runner = 2
while runner <= N:
    next_name = str(movie_names[runner-1]+1)

    while '666' not in next_name:
        next_name = str(int(next_name)+1)
    movie_names[runner] = int(next_name)
    runner += 1
print(movie_names[-1])
