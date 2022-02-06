# def solution():
#     n = int(input())
#     q = [int(x) for x in input().rstrip().split()]
#     q.sort()
#     powers = [int(2) for x in range(n)]
#     #? Time for sorting now!
#     for i in reversed(range(n)):
#         for j in reversed(range(i+1, n)):
#             print(i, j)
#             if (q[i] > q[j] and powers[i] != 0 or powers[j] != 0):
#                 powers[i] = 0 #! Person i was bribed by person j so his power is now zero
#                 powers[j] -= 1 #! Power decreases by as he goes bribing
#                 print(powers)
#                 q[i], q[j] = q[j], q[i] #! Swap then
#                 print(q)
#                 powers[i], powers[j] = powers[j], powers[i] #! Swap Powers As Well
    
#     print(q)

# def main():
#     n = int(input())
#     for i in range(n):
#         solution()


# main()

def solution():
    n = int(input())
    q = [int(x) for x in input().rstrip().split()]
    bribecount = 0
    chaotic = False
    for i in range(n):
        powers = 0
        for j in range(i+1, n):
            if q[i] > q[j]:
                powers += 1
                if (powers > 2):
                    chaotic = True
                    print("Too chaotic")
                    break
                else:
                    bribecount += 1
        else:
            continue  # only executed if the inner loop did NOT break
        break  # only executed if the inner loop DID break
                    
    
    if not chaotic:
        print(bribecount)
def main():
    n = int(input())
    for i in range(0, n):
        solution()

main()