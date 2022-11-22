import heapq
def solution(cacheSize, cities):
    answer = 0
    dic = {}
    cache = []
    for i in range(len(cities)):
        city = cities[i].lower()
        if city in cache :
            answer+=1
            dic[city] = i
        else:
            answer+=5
            dic[city] = i
            if len(cache) < cacheSize:
                cache.append(city)
            elif cacheSize != 0:
                cache.sort(key= lambda x:dic[x])
                if dic[cache[0]] < dic[city]:
                    cache[0] = city
    return answer