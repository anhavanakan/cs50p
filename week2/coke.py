#this is the price for 1 coke
due = 50

# keep accepting coins while total amount is less than 50
while due > 0:
    #remind the user the due
    print(f'Amount due: {due}')
    #take coin if its 5 10 15 otherwise return back
    coin = int(input('Insert coin: '))
    if coin in [5, 10, 25]:
        #if its 5 10 15 subtract from due
        due -= coin
#lastly give back change , due will be negative after 10 -5, thats why we need (* -1) and if its 0, -1 will not bother
print(f"Change owed: {-1 * due}")
