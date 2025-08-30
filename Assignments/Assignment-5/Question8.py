L = list(map(int, input("Enter elements of List L: ").split()))
M = list(map(int, input("Enter elements of List M: ").split()))

N = [L[i] + M[i] for i in range(len(L))]

print("Sum list:", N)
