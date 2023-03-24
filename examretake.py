#Problem 1
# num = int(input('Enter number of iteration(s): '))

# table = num * 2

# for row in range(table):
#     for col in range(table):
#         dleft = col
#         dright = (table - col) - 1
#         dtop = row
#         dbottom = (table - row) - 1
#         distance = [dleft, dright, dtop, dbottom]
#         output = min(distance)
    
#         if (dleft == dbottom or dright == dbottom) or (dleft == dtop or dright == dtop):
#             print('*', end='')
#         else:
#             print(num - output, end='')

#     print()


#Problem 2
movies = {}
while True:
    flag = ''
    year_released = int(input("Year of movie release: "))

    director = input("director: ")
    movie_title = input("title: ")
    release_date = input("release date: ")
    genre = input("genre(s): ")
    if year_released not in movies:
        movies[year_released] = [{'director': director, 'title': movie_title, 'release_date': release_date, 'genre(s)': genre}]
    else: 
        movies[year_released].append({'director': director, 'title': movie_title, 'release_date': release_date, 'genre(s)': genre})
    while True:
        flag = input("input another movie [y/n]? ")
        if flag.lower() not in ('y', 'n'):
            print("invalid input.")
        elif flag.lower() in ('y', 'n'):
            break
    if flag.lower() == 'n':
        break

print(movies)

while True:
    code = input(" [1] all movies in given year \n [2] movies by director \n [3] oldest movie \n [4] newest movie \n [5] director with most movies")
    if code == '1':
        year = input("year: ") 
        if year in movies:
            print(movies[year])
        else:
            print("no match")
    elif code == '2':
        dir = input("name of director: ")
        result = []

        for key, movie in movies.items():
                for m in movie:
                    if m['director'] == dir:
                        result.append(m)

        if len(result) < 1:
            print("no match")
        else:
            print(result)

    elif code == '3':
        keys = list(movies.keys())
        sorted = {i: movies[i] for i in keys}
        result = movies[keys[0]]

        result.sort(key = lambda x:x['release_date'])
        print(result[0])

    elif code == '4':
        keys = list(movies.keys())
        sorted = {i: movies[i] for i in keys}
        result = sorted[keys[-1]]

        result.sort(key = lambda x:x['release_date'])
        print(result[-1])

    elif code == '5':
        directors = {}

        for key, movie in movies.items():
                for m in movie:
                    if m['director'] not in directors:
                        directors[m['director']] = 1
                    else:
                        directors[m['director']] += 1


        topD = 0
        dname = ""
        for key, d in directors.items():
            if directors[key] > topD:
                topD = d
                dname = key

        print(dname)
    elif code == 'q':
        break
    else:
        print("invalid input")