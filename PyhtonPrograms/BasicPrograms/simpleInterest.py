# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

p = 1000
r =5
t =5

def simple_interest(p, t, r):
    print("The priincipal is: ", p)
    print("The amount is: ", t)
    print("The time is: ", r)

    si = (p * t* r)/100

    print("The simple interest is: ", si)
    return si

simple_interest(p, t, r)