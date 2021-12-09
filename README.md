# defect-prediction
This project relies on software metrics to predict defects in code
# Project Composition
The front end and the back end need to run seperately, so please open two terminal windows. 
## predef_prototype:
This has a preliminary version of the project on which we tested the feasability of the project.
## predef_v2
```
Go to predef_v2 by typing
```
cd predef_v2
This contains the project and all the necessary modules. In order to run the back end please type the following commands:
```
pip3 install flask 
pip3 install radon
pip3 install numpy
pip3 install scikit-learn
pip3 install pandas
```

Then please change the python path:
```
export PYTHONPATH="/Users/my_user/code"
```
If we do not perform this step the interpreter will not be able to access multiple files.

Finally run the server file by typing:

```
python3 server.py
```
## front end
Go to the directory by typing 
```
cd front-defect-pred
```
To run it just type:
```
python3 server.py
```
