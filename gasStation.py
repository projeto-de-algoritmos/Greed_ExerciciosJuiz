def canCompleteCircuit(gas, cost):
    n = len(gas)
    total_tank = 0
    current_tank = 0
    start_station = 0

    for i in range(n):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]

        if current_tank < 0:
            current_tank = 0
            start_station = i + 1

    if total_tank >= 0:
        return start_station
    else:
        return -1

# Solicita ao usuário que insira as listas de gas e cost
gas = list(map(int, input("Insira os valores de gas separados por espaço: ").split()))
cost = list(map(int, input("\nInsira os valores de cost separados por espaço: ").split()))

result = canCompleteCircuit(gas, cost)
if result == -1:
    print("\nNão é possível completar o circuito.")
else:
    print(f"\nVocê pode completar o circuito começando na estação {result}.")
