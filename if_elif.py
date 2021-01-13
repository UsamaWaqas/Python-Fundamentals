user_age = int( input( " enter your age "))
if user_age==0 or user_age< 0:
    print(" youo can not watch")
elif 0<user_age<=3:

    print("free ticket")
elif 3<user_age <=10:
    print(" ticket price: 150")
elif 10<user_age <=60:
    print("ticket price : 180")
else:
    print(" ticket price :200")
    