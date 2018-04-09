# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'


def clean_message(message):
    """ (str) -> str
    
    Return a copy of the message that includes only its alphabetical 
    characters, where each of those characters has been converted to uppercase.    
    
    >>> clean_message('32I%32Love$4You*.4325')
    'ILOVEYOU'
    >>> clean_message("9234$@I#Don\'t%Love^You.")
    'IDONTLOVEYOU'
    """
    
    # Initialize the new_message.
    new_message = ''
    
    # Accumulate every alphabetical character in new_message.
    for i in message:
        if i.isalpha():
            new_message += i
    return new_message.upper()


def encrypt_letter(unencrypted_letter, keystream):
    """ (str, int) -> str
    
    Translate the unencrypted_letter to a number in the range 0-25.  
    'A' translates to 0, 'B' to 1, 'Z' to 25, and so on.    
    Add the number with the keystream, modulo 26, convert back to a letter, 
    and return the encrypted result.
    
    >>> encrypt_letter('L', 12)
    'X'
    >>> encrypt_letter('H', 1)
    'I'
    """
    
    # Translate to a number in the range 0-25.  'A' translates to 0, 'B' to 1,
    # and so on.
    ord_diff = ord(unencrypted_letter) - ord('A')
    
    # Apply the keystream; we use % to handle the end of the alphabet.
    # The result is still in the range 0-25.
    new_char_ord = (ord_diff + keystream) % 26
        
    # Convert back to a letter.
    return chr(new_char_ord + ord('A'))


def decrypt_letter(encrypted_letter, keystream):
    """ (str, int) -> str
    
    Translate the encrypted_letter to a number in the range 0-25.  
    'A' translates to 0, 'B' to 1, 'Z' to 25, and so on.    
    Subtract the keystream from the number, modulo 26, convert back to a letter, 
    and return the unencrypted result.
    
    >>> decrypt_letter('X', 12)
    'L'
    >>> decrypt_letter('I', 1)
    'H'
    """
    
    # Translate to a number in the range 0-25.  'A' translates to 0, 'B' to 1,
    # and so on.
    ord_diff = ord(encrypted_letter) - ord('A')
    
    # Apply the keystream; we use % to handle the end of the alphabet.
    # The result is still in the range 0-25.
    new_char_ord = (ord_diff - keystream) % 26
        
    # Convert back to a letter.
    return chr(new_char_ord + ord('A'))


def swap_cards(deck_of_cards, index):
    """ (list of int, int) -> NoneType
    
    Swap the card in deck_of_cards at the index with the card that follows it. 
    Treat the deck_of_cards as circular: if the card at the index is on the 
    bottom of the deck_of_cards, swap that card with the top card.
    
    >>> b = [1, 3, 4, 5, 2]
    >>> swap_cards(b, 0)
    >>> b
    [3, 1, 4, 5, 2]
    
    >>> c = [2, 3, 1, 4, 6, 5, 7, 8]
    >>> swap_cards(c, 7)
    >>> c
    [8, 3, 1, 4, 6, 5, 7, 2]
    """
    
    card = deck_of_cards[index]
    
    # Split it into two cases: 
    # The first case is that the card is on the bottom of the deck_of_cards.
    if deck_of_cards[index] == deck_of_cards[len(deck_of_cards) - 1]:
        deck_of_cards[index] = deck_of_cards[0]
        deck_of_cards[0] = card
        
    # The second case is that the card is not on the bottom of the deck_of_cards.
    else:
        deck_of_cards[index] = deck_of_cards[index + 1]
        deck_of_cards[index + 1] = card
        
        
def get_small_joker_value(deck_of_cards):
    """ (list of int) -> int
    
    Return the second largest value in deck_of_cards 
    as the value of small joker.
    
    >>> get_small_joker_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    27
    >>> get_small_joker_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 9, \
                         12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    25
    """

    # Make a copy of the deck_of_cards to avoid modifying the deck_of_cards.
    copy = deck_of_cards.copy()
    
    # Remove the largest value in the copy list to let the second 
    # largest value become the largest one.
    copy.remove(max(copy))
    
    return max(copy)


def get_big_joker_value(deck_of_cards):
    """ (list of int) -> int
    
    Return the largest value in deck_of_cards as the value of big joker.
    
    >>> get_big_joker_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    28
    >>> get_big_joker_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 9, \
                         12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    26
    """
    
    return max(deck_of_cards)


def move_small_joker(deck_of_cards):
    """ (list of int) -> NoneType
    
    Swap the second largest card in deck_of_cards with the card that follows it. 
    If the second largest card is on the bottom of the deck_of_cards, 
    then swap it with the card on the top of deck_of_cards.
    
    >>> b = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_small_joker(b)
    >>> b
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 27, 5, 8, 11, 14, 17, 20, 23, 26]
    
    >>> c = [1, 4, 7, 10, 13, 16, 19, 22, 26, 3, 6, 9, \
                         12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 25]
    >>> move_small_joker(c)
    >>> c
    [25, 4, 7, 10, 13, 16, 19, 22, 26, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 1]
    """
    
    # Get the index of the second largest card.
    index = deck_of_cards.index(get_small_joker_value(deck_of_cards))
    
    # Swap it.
    swap_cards(deck_of_cards, index)


def move_big_joker(deck_of_cards):
    """ (list of int) -> NoneType
    
    Move the largest card two cards down the deck by performing two card swaps.
    If the largest card is on the bottom of the deck_of_cards, 
    then swap it with the card on the top of deck_of_cards.
    
    >>> b = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_big_joker(b)
    >>> b
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    
    
    >>> c = [1, 4, 7, 10, 13, 16, 19, 22, 23, 3, 6, 9, \
                         12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26, 25]
    >>> move_big_joker(c)
    >>> c
    [26, 4, 7, 10, 13, 16, 19, 22, 23, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 25, 1]
    """
    
    # Do the swap twice.
    for i in range(2):
        index = deck_of_cards.index(get_big_joker_value(deck_of_cards))
        swap_cards(deck_of_cards, index)


def triple_cut(deck_of_cards):
    """ (list of int) -> NoneType
    
    Call the joker(largest or second largest card in deck_of_cards) 
    closest to the top of the deck the first joker, 
    and the one closest to the bottom the second joker. 
    Swap the stack of cards above the first joker with 
    the stack of cards below the second joker.
    
    >>> a = [26, 4, 7, 10, 13, 16, 19, 22, 23, 3, 6, 9, 12, 15, 18, 21, 24, 2, \
                                                 5, 8, 11, 14, 17, 20, 25, 1]
    >>> triple_cut(a)
    >>> a
    [1, 26, 4, 7, 10, 13, 16, 19, 22, 23, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 25]
    
    
    >>> b = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(b)
    >>> b
    [2, 5, 8, 11, 14, 17, 20, 23, 26, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25]
    """
    
    # The values of small_joker and big_joker.
    small_joker = get_small_joker_value(deck_of_cards)
    big_joker = get_big_joker_value(deck_of_cards)
    
    # The indices of small_joker and big_joker.
    small_joker_index = deck_of_cards.index(small_joker)
    big_joker_index = deck_of_cards.index(big_joker)
    
    # The indices of first_joker and second_joker.
    first_joker_index = min(small_joker_index, big_joker_index)
    second_joker_index = max(small_joker_index, big_joker_index)
    
    # Split the deck_of_cards into three parts.
    before = deck_of_cards[: first_joker_index]
    midd = deck_of_cards[first_joker_index: second_joker_index + 1]
    after = deck_of_cards[second_joker_index + 1:]
    
    # Reorder the deck_of_cards.
    deck_of_cards.clear()
    deck_of_cards.extend(after + midd + before)
    

def insert_top_to_bottom(deck_of_cards):
    """ (list of int) -> NoneType
    
    Examine the value of the bottom card of the deck_of_cards; 
    move that many cards from the top of the deck to the bottom, 
    inserting them just above the bottom card. 
    Special case: if the bottom card 
    is the big joker, use the value of the small joker as the number of cards.
    
    >>> a = [1, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 28, 11, 14, 17, 20, 23, 8]
    >>> insert_top_to_bottom(a)
    >>> a
    [25, 26, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 28, 11, 14, 17, 20, 23, 1, 4, 7, 10, 13, 16, 19, 22, 8]
    
    
    >>> b = [1, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    >>> insert_top_to_bottom(b)
    >>> b
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    """
    
    # Split it into two cases: 
    # The first case is that the bottom card is not a big joker.
    if deck_of_cards[-1] != get_big_joker_value(deck_of_cards):
        a = deck_of_cards[:deck_of_cards[-1]]
        for i in range(len(a)):
            deck_of_cards.remove(a[i])
            deck_of_cards.insert(-1, a[i])
    
    # The second case is that the bottom card is a big joker.
    # In this case, deck_of_cards remains the same.
            

def get_card_at_top_index(deck_of_cards):
    """ (list of int) -> int
    
    Using the value of the top card as an index, 
    return the card in the deck at that index. 
    Special case: if the top card is the big joker,
    use the value of the small joker as the index.
    
    >>> get_card_at_top_index([4, 1, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 28, 11, 14, 17, 20, 23, 8])
    13
    >>> get_card_at_top_index([28, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, \
                      12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 1])
    1
    """
    
    # Split it into two cases: 
    # The first case is that the top card is a big joker.
    if deck_of_cards[0] == get_big_joker_value(deck_of_cards):
        index = get_small_joker_value(deck_of_cards)
        
    # The second case is that the top card is not a big joker.
    else:
        index = deck_of_cards[0]
        
    return deck_of_cards[index]


def get_next_keystream_value(deck_of_cards):
    """ (list of int) -> int
    
    Get next keystream value by repeating all five steps of the algorithm:
    move_small_joker(deck_of_cards)
    move_big_joker(deck_of_cards)
    triple_cut(deck_of_cards)
    insert_top_to_bottom(deck_of_cards)
    get_card_at_top_index(deck_of_cards)
    until a valid keystream value(which is not a joker) is produced.
    
    
    >>> get_next_keystream_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, \
                     12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    >>> get_next_keystream_value([14, 17, 20, 6, 28, 15, 18, 21, 24, 2, 1, 27, \
                    23, 26, 9, 4, 7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 12])
    23
    """
    
    # Initialize the flag.
    flag = 0
    t = 0
    
    # Execute the while loop until a valid keystream value
    # (which is not a joker) is produced.
    while flag == 0:
        small_joker = get_small_joker_value(deck_of_cards)
        big_joker = get_big_joker_value(deck_of_cards)
        move_small_joker(deck_of_cards)
        move_big_joker(deck_of_cards)
        triple_cut(deck_of_cards)
        insert_top_to_bottom(deck_of_cards)
        t = get_card_at_top_index(deck_of_cards)
        flag = 1
        if t == small_joker or t == big_joker:
            flag = 0
    return t


def process_messages(deck_of_cards, list_of_messages, mode):
    """ (list of int, list of str, str) -> list of str
    
    Return a list of encrypted or decrypted messages, in the same order as 
    they appear in the given list_of_messages. Note that the first parameter 
    may also be mutated during a function call.
    
    >>> process_messages([1,2,3,4,5,6,7,8], ['H', 'E', 'L', 'L', 'O'], ENCRYPT)
    ['K', 'I', 'N', 'M', 'P']
    >>> process_messages([1,2,3,4,5,6,7,8], ['K', 'I', 'N', 'M', 'P'], DECRYPT)
    ['H', 'E', 'L', 'L', 'O']
    """
    
    result = []
    
    # Loop over every message.
    for i in list_of_messages:
        message = clean_message(i)
        
        # Introduce an character accumulator.
        char_acc = ''
        
        # ENCRYPT or DECRYPT every alphabet in the message, 
        # and put the new alphabet into the character accumulator.
        for alphabet in message:
            keystream = get_next_keystream_value(deck_of_cards)
            if mode == ENCRYPT:
                char_acc += encrypt_letter(alphabet, keystream)
            elif mode == DECRYPT:
                char_acc += decrypt_letter(alphabet, keystream)
                
        # Append the character accumulator to the result.
        result.append(char_acc)
    return result


def read_messages(message_file):
    """ (file open for reading) -> list of str
    
    Read and return the contents of the file as a list of messages, in the 
    order in which they appear in the file. Strip the newline from each line.
    
    """
    
    # Store the message_file into the lst as a list of messages.
    lst = message_file.readlines()
    
    # Strip the newline from each string in the list.
    for i in range(len(lst)):
        lst[i] = lst[i].strip()
        
    return lst


def is_valid_deck(deck_of_cards):
    """ (list of int) -> bool
    
    A valid deck contains every integer from 1 up to the number of cards in 
    the deck. 
    Return True if and only if the deck_of_cards is a valid deck of cards. 
    
    >>> is_valid_deck([1, 4, 3, 2])
    True
    >>> is_valid_deck([])
    False
    """
    
    # If the length of deck_of_cards is less than 3, it's not a valid deck.
    if len(deck_of_cards) < 3:
        return False
    
    # Otherwise, check whether every number from 1 up to the biggest integer 
    # is in the deck_of_cards.
    else:
        for i in range(1, len(deck_of_cards) + 1):
            if not (i in deck_of_cards):
                return False
        return True


def read_deck(deck_file):
    """ (file open for reading) -> list of int
    
    Read and return the numbers that are in the file, in the order in which 
    they appear in the file.
    
    """
    
    list_of_int = []
    
    # Store the entire deck_file into the lst as the whole string.
    lst = deck_file.read()
    
    # Introduce a digit accumulator.
    digit_acc = ''
    
    # Check every character in the lst. If it is a digit, put it into the 
    # digit accumulator. If the next character that follows the it is a digit,
    # add it to the digit accumulator too. Otherwise, append the digit 
    # accumulator to the list_of_int.
    for i in lst:
        if i.isdigit():
            digit_acc += i
        else:
            if digit_acc != '':
                list_of_int.append(int(digit_acc))
                digit_acc = ''
    return list_of_int

# End
