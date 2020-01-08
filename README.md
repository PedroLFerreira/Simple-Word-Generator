# Simple Word Generator
Generates random words similar to a given set of words. 

A conditional probability model of the data is created and used to generate new samples.
Generation can be given 2 parameters, namely:
* Minimum word length
* Maximum word length

## Dependencies
```
Python3
numpy
```
## How to use
```
python3 generateWords.py \<filename\> \<minimum word length\> \<maximum word length\> \<number of words to generate\>
```
## Example
Given a set of elven city names from Lord of the Rings (in a file called "elvenCities.txt"), output a set of elvish-like city names. In this case we want 10 city names that are between 4 and 12 characters long.

### Input:
```
python3 generateWords.py elvenCities.txt 4 12 10
```
### Output:
```
Malinyarindon
Ostha
Gloriot
Endhol
Llorguargrore
Gololl
Endendhin
Dhobey
Andedhelon
Peshiliredos
```

## Authors

* **Pedro L. Ferreira**

## Acknowledgements

* Thank you Mr. Tolkien 💙