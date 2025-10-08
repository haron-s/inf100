def get_endpoints(i,n,x_lo,x_hi):
    i, n = int(i), int (n)
    x_lo, x_hi = float(x_lo), float(x_hi)

    length = x_hi - x_lo
    n_length = length / n

    i_lo = x_lo + n_length*i
    i_hi = i_lo + n_length

    return i_lo, i_hi

def almost_equals(a, b):
    return abs(a - b) < 0.000000001

def main():
    x_lo = float(input())
    x_hi = float(input())
    n = int(input())

    print(f'x_lo =')
    print(f'x_hi =')
    print(f'n =')

    for i in range (0,n):
        i_lo, i_hi = get_endpoints(i,n,x_lo,x_hi)
        print(i_lo,i_hi)

if __name__ == "__main__":
    main()
    