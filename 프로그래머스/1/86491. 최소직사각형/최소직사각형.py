def solution(sizes):
    lmax = 0
    rmax = 0
    for l, r in sizes:
        lmax = max(lmax, max(l, r))
        rmax = max(rmax, min(l, r))
    return lmax * rmax