t, h = 0, 1
while S[t] != S[h]:
    t += 1
    h += 2
i = 0
while S[i] != S[t + i]:
    i += 1