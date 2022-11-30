from collections import defaultdict

jug_1, jug_2, aim = 4, 3, 2
visited = defaultdict(lambda: False)

def waterJugSolver(amount_1, amount_2):

	if (amount_1 == aim and amount_2 == 0) or (amount_2 == aim and amount_1 == 0):
		print(amount_1, amount_2)
		return True
	
	if visited[(amount_1, amount_2)]:
		return False
		
	visited[(amount_1, amount_2)] = True
	print(amount_1, amount_2)
	
	return (
      waterJugSolver(0, amount_2) or
      waterJugSolver(amount_1, 0) or
      waterJugSolver(jug_1, amount_2) or
      waterJugSolver(amount_1, jug_2) or
      waterJugSolver(amount_1 + min(amount_2, (jug_1-amount_1)), 
                     amount_2 - min(amount_2, (jug_1-amount_1))
                     ) or
      waterJugSolver(amount_1 - min(amount_1, (jug_2-amount_2)),
                     amount_2 + min(amount_1, (jug_2-amount_2))
                     )
	)


print("Steps: ")


waterJugSolver(0, 0)