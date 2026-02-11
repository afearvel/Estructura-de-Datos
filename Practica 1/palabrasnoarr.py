palabra = "Parangaricutirimicuaro"

xa = xb = xc = xd = xe = xf = xg = xh = xi = xj = xk = xl = xm = xn = xo = xp = xq = xr = xs = xt = xu = xv = xw = xx = xy = xz = 0

ya = yb = yc = yd = ye = yf = yg = yh = yi = yj = yk = yl = ym = yn = yo = yp = yq = yr = ys = yt = yu = yv = yw = yx = yy = yz = False

for l in palabra:

    if l == "a" or l == "A":
        xa += 1
        if l == "A":
            ya = True

    if l == "b" or l == "B":
        xb += 1
        if l == "B":
            yb = True

    if l == "c" or l == "C":
        xc += 1
        if l == "C":
            yc = True

    if l == "d" or l == "D":
        xd += 1
        if l == "D":
            yd = True

    if l == "e" or l == "E":
        xe += 1
        if l == "E":
            ye = True

    if l == "f" or l == "F":
        xf += 1
        if l == "F":
            yf = True

    if l == "g" or l == "G":
        xg += 1
        if l == "G":
            yg = True

    if l == "h" or l == "H":
        xh += 1
        if l == "H":
            yh = True

    if l == "i" or l == "I":
        xi += 1
        if l == "I":
            yi = True

    if l == "j" or l == "J":
        xj += 1
        if l == "J":
            yj = True

    if l == "k" or l == "K":
        xk += 1
        if l == "K":
            yk = True

    if l == "l" or l == "L":
        xl += 1
        if l == "L":
            yl = True

    if l == "m" or l == "M":
        xm += 1
        if l == "M":
            ym = True

    if l == "n" or l == "N":
        xn += 1
        if l == "N":
            yn = True

    if l == "o" or l == "O":
        xo += 1
        if l == "O":
            yo = True

    if l == "p" or l == "P":
        xp += 1
        if l == "P":
            yp = True

    if l == "q" or l == "Q":
        xq += 1
        if l == "Q":
            yq = True

    if l == "r" or l == "R":
        xr += 1
        if l == "R":
            yr = True

    if l == "s" or l == "S":
        xs += 1
        if l == "S":
            ys = True

    if l == "t" or l == "T":
        xt += 1
        if l == "T":
            yt = True

    if l == "u" or l == "U":
        xu += 1
        if l == "U":
            yu = True

    if l == "v" or l == "V":
        xv += 1
        if l == "V":
            yv = True

    if l == "w" or l == "W":
        xw += 1
        if l == "W":
            yw = True

    if l == "x" or l == "X":
        xx += 1
        if l == "X":
            yx = True

    if l == "y" or l == "Y":
        xy += 1
        if l == "Y":
            yy = True

    if l == "z" or l == "Z":
        xz += 1
        if l == "Z":
            yz = True


if xa > 0:
    print(("A" if ya else "a"), "=", xa)
if xb > 0:
    print(("B" if yb else "b"), "=", xb)
if xc > 0:
    print(("C" if yc else "c"), "=", xc)
if xd > 0:
    print(("D" if yd else "d"), "=", xd)
if xe > 0:
    print(("E" if ye else "e"), "=", xe)
if xf > 0:
    print(("F" if yf else "f"), "=", xf)
if xg > 0:
    print(("G" if yg else "g"), "=", xg)
if xh > 0:
    print(("H" if yh else "h"), "=", xh)
if xi > 0:
    print(("I" if yi else "i"), "=", xi)
if xj > 0:
    print(("J" if yj else "j"), "=", xj)
if xk > 0:
    print(("K" if yk else "k"), "=", xk)
if xl > 0:
    print(("L" if yl else "l"), "=", xl)
if xm > 0:
    print(("M" if ym else "m"), "=", xm)
if xn > 0:
    print(("N" if yn else "n"), "=", xn)
if xo > 0:
    print(("O" if yo else "o"), "=", xo)
if xp > 0:
    print(("P" if yp else "p"), "=", xp)
if xq > 0:
    print(("Q" if yq else "q"), "=", xq)
if xr > 0:
    print(("R" if yr else "r"), "=", xr)
if xs > 0:
    print(("S" if ys else "s"), "=", xs)
if xt > 0:
    print(("T" if yt else "t"), "=", xt)
if xu > 0:
    print(("U" if yu else "u"), "=", xu)
if xv > 0:
    print(("V" if yv else "v"), "=", xv)
if xw > 0:
    print(("W" if yw else "w"), "=", xw)
if xx > 0:
    print(("X" if yx else "x"), "=", xx)
if xy > 0:
    print(("Y" if yy else "y"), "=", xy)
if xz > 0:
    print(("Z" if yz else "z"), "=", xz)
