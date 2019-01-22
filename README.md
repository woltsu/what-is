## what-is  
what-is is a tool to see what different things look like in average. Using a given keyword, what-is downloads images based on google results and outputs what the average image looks like.  

## Usage  
Before what-is can be used, one must create a .env file to the project root and add the following environmental variables there:  

`API_KEY=X` (https://developers.google.com/custom-search/v1/introduction)  
`CX=Y` (https://cse.google.com/cse/all)  

## Run
1. pip3 install -r requirements.txt  
2. python3 what-is/main.py  

OR

1. docker build -t what-is .
2. docker run -it -v $(pwd)/output:/src/output what-is  

## Examples  
#### Black hole  
![black hole](/examples/black_hole.jpg)  
#### Earth
![earth](/examples/earth.jpg)
#### Eye
![eye](/examples/eye.jpg)
#### Face
![face](/examples/face.jpg)
#### Fire
![fire](/examples/fire.jpg)
#### Flag
![flag](/examples/flag.jpg)
#### Forest
![forest](/examples/forest.jpg)
#### Lightning
![lightning](/examples/lightning.jpg)
#### Milky way
![milky way](/examples/milky_way.jpg)
