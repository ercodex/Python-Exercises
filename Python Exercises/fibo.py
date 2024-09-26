def fibseq(N):
    v = [0, 1, 1]
    for i in range(N):
        v.append(sum(v[-2:]))
    print(v)

fibseq(7)