# Bulls and Cows

For those of you who loved Wordle, but are better with digits than with letters, here is another game called Bulls and Cows. 

The rules are very straightforward:

* You are supposed to guess a number (technically speaking, it can start with 0 so it might not be a number) that consists of 4 unique digits
* Each round your guess is checked against the true number that was generated randomly
* If you guess both the digit and its position, this is counted as a bull
* If the true number includes the digit, but the position is wrong, it is a cow

**Example**
If the true number is 9543 and your guess is 9532, you have got 2 bulls (9 and 5 are at correct positions) and 1 cow (there is a "3", but at a different index). 

* Note that what is counted as a bull does not increment the cow counter
* You need to be clever to guess the number in **10** steps
* Promise not to use your skills to crack PIN numbers! :) 

## How to run? 

Just do `python main.py` and enjoy your unforgettable CLI experience :) 
