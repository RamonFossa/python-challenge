import math;

## iterative

def average(list):
    total = 0
    for x in list:
        total+=x
    
    return total/len(list)

def standard_d(list):
    total = 0;
    av = average(list);
    for x in list:
        total+= math.pow(x-av, 2)

    return math.sqrt(total/(len(list)-1))

##

def main(): 

  list = [9, 8.5, 0.5, 10, 1, 4, 5, 6, 6.5, 3];
  av = average(list);
  des = standard_d(list);
  print(av, des)


main();
