# Playing card based en(de)cryption algorithm

## Getting Started

### Prerequisites

* Python 3.x
* Terminal (in Unix) OR PowerShell (in Windows)

### Download and run the algorithm
```
# Change to HOME directory
$ cd ~

# Clone this repo and 'cd' into it
$ git clone https://github.com/jellycsc/card-based-encryption-algorithm.git
$ cd card-based-encryption-algorithm/

# Let's start playing
$ python3 cipher_program.py
```

## Decryption Example
```
Enter the name of the file that contains the card deck: card_deck.txt
Enter the name of the file that contains the message: secret_message.txt
Do you want to encrypt (e) or decrypt (d)? d
THISISITTHEMASTERSWORD
NOTHISCANTBEITTOOBAD
```
Compare with the real message:
```
This is it! The master sword!
No, this can't be it. Too bad.
```

## Encryption Example
```
Enter the name of the file that contains the card deck: card_deck.txt
Enter the name of the file that contains the message: decrypted_message.txt
Do you want to encrypt (e) or decrypt (d)? e
EQFZSRTEAPNXLSRJAMNGAT
GLCEGMOTMTRWKHAMGNME
```
Compare with the encrypted message:
```
EQFZSRTEAPNXLSRJAMNGAT
GLCEGMOTMTRWKHAMGNME
```

## Authors

| Name             | GitHub                                     | Email
| ---------------- | ------------------------------------------ | -------------------------
| Chenjie Ni       | [jellycsc](https://github.com/jellycsc)    | nichenjie2013@gmail.com

## Thoughts and future improvements

* Since this is a rather simple beginner's project, no further improvements will be made.

## Contributing to this project

1. Fork it ( https://github.com/jellycsc/card-based-encryption-algorithm/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to your feature branch (`git push origin my-new-feature`)
5. Create a new Pull Request

Details are described [here](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project).

## Bug Reporting
Please log bugs under [Issues](https://github.com/jellycsc/card-based-encryption-algorithm/issues) tab on github.  
OR you can shoot an email to <nichenjie2013@gmail.com>
