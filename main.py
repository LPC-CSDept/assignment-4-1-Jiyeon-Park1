def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        if not start.isalpha() or not end.isalpha():
            print('Make sure its a letter')
            continue
        if start > end:
            print('The starting letter must be smaller then the ending letter')
            continue
        
        break
            
    """
    ########################################
    Code Your Program here
    ########################################
    """
    begin = ord(start)
    last = ord(end)
    for alph in (begin , last + 1):
        alph.append(result)

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
