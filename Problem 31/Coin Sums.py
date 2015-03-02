__author__ = 'Shawn'

def moneypermutations(goal):
    goal = goal * 100
    for p1 in range(goal+1):
        if p1 == goal: print p1
        for p2 in range(goal/2):
            for p5 in range(goal/5):
                for p10 in range(goal/10):
                    for p20 in range(goal/20):
                        for p50 in range(goal/50):
                            for p100 in range(goal/100):
                                for p200 in range(goal/200):
                                    if (p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 + 200*p200) == goal:
                                        return (p1,p2,p5,p10,p20,p50,p100,p200)


print moneypermutations(1)