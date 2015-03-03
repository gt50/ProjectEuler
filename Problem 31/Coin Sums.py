__author__ = 'Shawn'

def lessthanorequalgoal(p1,p2,p5,p10,p20,p50,p100,p200, goal):
    return (p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 + 200*p200) <= goal

def equaltogoal(p1,p2,p5,p10,p20,p50,p100,p200, goal):
    return (p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 + 200*p200) == goal

def moneypermutations(goal):
    goal = goal * 100
    count = 0
    for p1 in range(goal+1):
        if lessthanorequalgoal(p1,0,0,0,0,0,0,0, goal):
            for p2 in range(goal/2 + 1):
                if lessthanorequalgoal(p1,p2,0,0,0,0,0,0, goal):
                    for p5 in range(goal/5 +1):
                        if lessthanorequalgoal(p1,p2,p5,0,0,0,0,0, goal):
                            for p10 in range(goal/10 +1):
                                if lessthanorequalgoal(p1,p2,p5,p10,0,0,0,0, goal):
                                    for p20 in range(goal/20 +1):
                                        if lessthanorequalgoal(p1,p2,p5,p10,p20,0,0,0, goal):
                                            for p50 in range(goal/50 +1):
                                                if lessthanorequalgoal(p1,p2,p5,p10,p20,p50,0,0, goal):
                                                    for p100 in range(goal/100 +1):
                                                        if lessthanorequalgoal(p1,p2,p5,p10,p20,p50,p100,0, goal):
                                                            for p200 in range(goal/200 +1):
                                                                if equaltogoal(p1,p2,p5,p10,p20,p50,p100,p200, goal): count += 1
    return count


print moneypermutations(2)