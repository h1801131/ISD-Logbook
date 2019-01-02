page = int(input("Enter the page:"))
def PrintPageNumber(page):
    if EvenPage(page) == True:
        print(page)
    else:
        print("%60s%d" % (" ", page))
def EvenPage(nr):
    if nr % 2 == 0:
        return True
    else:
        return False
for i in range(2, 10):
    PrintPageNumber(i)
