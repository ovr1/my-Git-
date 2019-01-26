список = {
    'viny':'1234',
    'oleg':'4321',
    }
def р_н(key):

    р_н = True
    while р_н:
        if key in список:
            print("\nПредложенный Вами ник занят   ")
            key = input("\nВведите другой ник  ")
            п_п = True
        else:
            п_п = False
            print("\nЗапомните Ваш ник:   ", key)
            break
