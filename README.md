# Binary Prediction of Poisonous Mushrooms
https://kaggle.com/competitions/playground-series-s4e8


## Preprocessing the data
### Structure of the data
Provided with two files `train.csv` and `test.csv` classify each row in the csv as either an edible mushroom (e) or a poisonous mushroom (p).

`train.csv` has the following structure
|column      |type |missing data|options    |
|------------|-----|------------|-----------|
|id          |int  |false       |           |
|class       |str  |false       |{e,c}      |
|cap-diameter|float|true        |           |
|cap-shape   |str  |true        |{x,f,s,b,o}|
|ca
The output must be a csv named `solution.csv` and the structure must be 
```
id,class\
1,e\
2,e\
3,p\
etc.
```