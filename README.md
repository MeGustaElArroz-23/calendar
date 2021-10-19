# calendar
A simple calendar app that runs on the console

All dates in YYYY-MM-DD format. To use it, you run the program with some arguments (usually the name of the command + a number or date).
Currently the commands avaiable are

```ls n``` : shows all events today and in the following n days

```add n``` : asks for the description of the event and adds it in n days after today

```add YYYY-MM-DD``` : asks for the description of the event and adds it on the specified date

So for example, if you want to run ls command with n=5 you can open a terminal on the same folder and write this:

```python3 ./main.py ls 5```
