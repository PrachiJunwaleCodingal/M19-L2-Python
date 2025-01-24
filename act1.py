#	Tip The Waiter

def fun1(bill,tip):
    t = round(bill * (1 + 0.01*tip))
    print("Pay amount:",t)

fun1(200,50)
