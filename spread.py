from random import random
import math

infected = [];

def randPts(x,y,R,num):
    global infected
    days = 1;
    spread = 1;
    for cur in range(num):
        probRandInfect = 1-(len(infected)/10);
        decide = random();
        if(decide>probRandInfect):
            pick = int(math.floor(random()*len(infected)))
            source = infected[pick];
            infected.append(randInfect(source[0],source[1],20,days));
        else:
            infected.append(randInfect(x,y,R,days));
        if(len(infected)>spread):
            days += 1
            spread *= days

def randInfect(x,y,R,days):
    r = R*math.sqrt(random());
    t = random()*2*math.pi;
    return [x+r*math.cos(t),y+r*math.sin(t),days]

def main():
    global infected
    randPts(40,40,10,1000);
    f = open("fake_data.csv","w")
    for point in infected:
        str = "%f,%f,%i\n"%(point[0],point[1],point[2])
        f.write(str);
    f.close();
    
if __name__ == "__main__":
    main();
