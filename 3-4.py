def solve_hanoi(n, start, buffer, end):
    if n == 0:
        return
    solve_hanoi(n-1, start, end, buffer)
    end.append(start.pop())
    solve_hanoi(n-1, buffer, start, end)

if __name__ == '__main__':
    hanoi_towers = [range(10, 0, -1), [], []]
    print 'Hanoi Towers of 10:', hanoi_towers
    solve_hanoi(10, hanoi_towers[0], hanoi_towers[1], hanoi_towers[2])
    print 'Now solved:', hanoi_towers
