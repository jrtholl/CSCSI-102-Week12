def fib():
    fibs = [1,2]

    for i in range(1,99):
        Fn = fibs[i-1] + fibs[i]
        fibs.append(Fn)


    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
