def main():
    Received_Message = input()
    ActualMessage = str()
    
    for i in range((len(Received_Message))):
        if i % 3 == 0:
            ActualMessage += 'S'
        if i % 3 == 1:
            ActualMessage += 'O'
        if i % 3 == 2:
            ActualMessage += 'S'
            
    #! Above loop creates an actual message for us
    #! The loop below is very simple to understand for instance (O, Q) | O != Q | ChangedLetters += 1
    #! Code is Optimized
    
    changedletters = 0
    for i, j in zip(Received_Message, ActualMessage):
        if i != j:
            changedletters += 1
            
    print(changedletters)
    
    
main()

#? Rough Code
# def main():
#     s = input()
#     sos = ['S', 'O', 'S']
#     completes = []
#     for i in range((len(s) // 3)):
#         for j in sos:
#             completes.append(j)
#     completes = "".join(completes)
#     counter = 0
#     for i, j in zip(s, completes):
#         if i != j:
#             counter += 1
    
#     print(counter)
    
# main()
