def preetyprint(solution):
    def line(pos, length=len(solution)):
        return'| '*(pos)+'|X'+'| '*(length-pos)
    for pos in solution:
        print (line(pos))

preetyprint([0,1,2,3,4,5])