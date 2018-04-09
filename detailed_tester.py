import cipher_functions

ENCRYPT = 'e'
DECRYPT = 'd'

x1 = cipher_functions.clean_message("Auf30JF*()#i%k")
if x1 == "AUFJFIK":
    print("clean_message:", True)
else:
    print("clean_message:", False)
    print ("expected:","AUFJFIK")
    print ("got:", x1)

x2a = cipher_functions.encrypt_letter("A",1)
x2b = cipher_functions.encrypt_letter("Y",2)
if x2a == "B" and x2b == "A" :
    print("encrypt_letter:", True)
else:
    print("encrypt_letter:", False)
    print ("expected:","B")
    print ("got:", x2a)
    print ("expected:","A")
    print ("got:", x2b)

x3a = cipher_functions.decrypt_letter("A",2)
x3b = cipher_functions.decrypt_letter("C",2)
if x3a == "Y" and x3b == "A":
    print("decrypt_letter:", True)
else:
    print("decrypt_letter:", False)
    print ("expected:","Y")
    print ("got:", x3a)
    print ("expected:","A")
    print ("got:", x3b)

deck1 = [6,2,3,4,1,5]
deck2 = [6,2,3,4,1,5]
x4a = cipher_functions.swap_cards(deck1,1)
x4b = cipher_functions.swap_cards(deck2,5)
if deck1 == [6,3,2,4,1,5] and deck2 == [5,2,3,4,1,6]:
    print("swap_cards:", True)
else:
    print("swap_cards:", False)
    print ("expected:",[6,3,2,4,1,5])
    print ("got:", x4a)
    print ("expected:",[5,2,3,4,1,6])
    print ("got:", x4b)

deck1 = [6,2,3,4,1,5]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
x5a = cipher_functions.get_small_joker_value(deck1)
x5b = cipher_functions.get_small_joker_value(deck2)
if x5a == 5 and x5b == 27:
    print("get_small_joker_value:", True)
else:
    print("get_small_joker_value:", False)
    print ("expected:",[6,2,3,4,1,5])
    print ("got:", x5a)
    print ("expected:",[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    print ("got:", x5b)
    
deck1 = [6,2,3,4,1,5]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
x6a = cipher_functions.get_big_joker_value(deck1)
x6b = cipher_functions.get_big_joker_value(deck2)
if x6a == 6 and x6b == 28:
    print("get_big_joker_value:", True)
else:
    print("get_big_joker_value:", False)
    print ("expected:",6)
    print ("got:", x6a)
    print ("expected:",28)
    print ("got:", x6b)

deck1 = [6,2,3,4,1,5]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
x7a = cipher_functions.move_small_joker(deck1)
x7b = cipher_functions.move_small_joker(deck2)
if deck1 == [5,2,3,4,1,6] and deck2 == [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 2, 27, 5, 8, 11, 14, 17, 20, 23, 26]:
    print("move_small_joker:", True)
else:
    print("move_small_joker:", False)
    print ("expected:",[5,2,3,4,1,6])
    print ("got:", x7a)
    print ("expected:",[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 2, 27, 5, 8, 11, 14, 17, 20, 23, 26])
    print ("got:", x7b)

deck1 = [6,2,3,4,1,5]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
x8a = cipher_functions.move_big_joker(deck1)
x8b = cipher_functions.move_big_joker(deck2)
if deck1 == [2,3,6,4,1,5] and deck2 == [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]:
    print("move_big_joker:", True)
else:
    print("move_big_joker:", False)
    print ("expected:",[2,3,6,4,1,5])
    print ("got:", x8a)
    print ("expected:",[1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    print ("got:", x8b)

deck1 = [6,2,3,4,1,5]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
x9a = cipher_functions.triple_cut(deck1)
x9b = cipher_functions.triple_cut(deck2)
if deck1 == [6,2,3,4,1,5] and deck2 == [ 2, 5, 8, 11, 14, 17, 20, 23, 26, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25]:
    print("triple_cut:", True)
else:
    print("triple_cut:", False)
    print ("expected:",[6,2,3,4,1,5])
    print ("got:", x9a)
    print ("expected:",[ 2, 5, 8, 11, 14, 17, 20, 23, 26, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25])
    print ("got:", x9b)

deck1 = [6,2,3,4,1,5]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
x10a = cipher_functions.insert_top_to_bottom(deck1)
x10b = cipher_functions.insert_top_to_bottom(deck2)
if deck1 == [6,2,3,4,1,5] and deck2 == [ 23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26]:
    print("insert_top_to_bottom:", True)
else:
    print("insert_top_to_bottom:", False)
    print ("got:", x10a)
    print ("expected:",[6,2,3,4,1,5])
    print ("got:", x10b)
    print ("expected:",[ 23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26])

deck1 = [6,2,3,4,1,5]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
x11a = cipher_functions.get_card_at_top_index(deck1)
x11b = cipher_functions.get_card_at_top_index(deck2)
if x11a == 5 and x11b == 4:
    print("get_card_at_top_index:", True)
else:
    print("get_card_at_top_index:", False)
    print ("got:", x11a)
    print ("expected:",5)
    print ("got:", x11b)
    print ("expected:",4)

deck1 = [6,2,3,4,1,5]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
x12a = cipher_functions.get_next_keystream_value(deck1)
x12b = cipher_functions.get_next_keystream_value(deck2)
if x12a == 3 and x12b == 11:
    print("get_next_keystream_value:", True)
else:
    print("get_next_keystream_value:", False)
    print ("got:", x12a)
    print ("expected:",3)
    print ("got:", x12b)
    print ("expected:",11)
    
deck1 = [6,2,3,4,1,5]
deck2 = [6,2,3,4,1,5]
x13a = cipher_functions.process_messages(deck1, ['ABC'], 'e')
x13b = cipher_functions.process_messages(deck2, ['DCD'], 'd')
if x13a == ['DCD'] and x13b == ['ABC']:
    print("process_messages:", True)
else:
    print("process_messages:", False)
    print ("got:", x13a)
    print ("expected:",['DCD'])
    print ("got:", x13b)
    print ("expected:",['ABC'])

deck1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
deck2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 29]
x14a = cipher_functions.is_valid_deck(deck1)
x14b = cipher_functions.is_valid_deck(deck2)
if x14a == True and x14b == False:
    print("is_valid_deck:", True)
else:
    print("is_valid_deck:", False)
    print ("got:", x14a)
    print ("expected:",True)
    print ("got:", x14b)
    print ("expected:",False)    







