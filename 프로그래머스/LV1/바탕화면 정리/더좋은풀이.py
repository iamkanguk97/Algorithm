def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                a.append(i)
                b.append(j)
    
    return [min(a), min(b), max(a)+1, max(b)+1]