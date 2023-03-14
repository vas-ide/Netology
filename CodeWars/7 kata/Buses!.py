





def buses(kids, adults, places):
    if kids > 0 and places < 3:
        print(0)
        return 0
    elif places < 1:
        print(0)
        return 0
    elif kids > 0 and adults < 2:
        print(0)
        return 0
    else:
        counter_kids = kids
        counter_adults = adults
        counter_buses = 0
        while counter_kids + counter_adults >= 1:
            if kids > 0 and adults >= 2:
                counter_buses += 1
                counter_adults -= 2
                counter_kids -= (places - 2)
                if counter_adults < 2 and counter_kids > 0:
                    print(0)
                    return 0
            elif counter_kids <= 1:
                counter_kids = 0
                counter_buses += 1
                counter_adults -= places
        print(counter_buses)
        return counter_buses




buses(17, 1, 39)        #0
buses(0, 35, 2)         #18
buses(21, 3, 23)        #2
buses(34, 38, 3)        #0



buses(2, 4, 4)          #2
buses(1, 55, 3)         #19
buses(10, 4, 7)         #2
buses(4, 8, 3)          #4
buses(36, 33, 8)        #9
buses(2, 2, 7)          #1
buses(2, 2, 4)          #1
buses(6, 2, 9)          #1
buses(0, 0, 0)          #0
buses(0, 1, 0)          #0
buses(0, 2, 0)          #0
buses(0, 34, 1)         #34
buses(5, 10, 2)         #0
buses(0, 9, 2)          #5







