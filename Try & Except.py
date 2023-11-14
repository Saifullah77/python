#try except

try:
    a = 1/0
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)