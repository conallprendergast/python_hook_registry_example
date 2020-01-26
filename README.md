# Introduction
This project demonstrates a simple hook-based architecture for customizable long running scripts.

This example code shows how a long-running script might be customized to execute specific actions on specific days of the month and time of day.

Example use cases include simulations that _sometimes_ require very specific actions to be executed when certain conditions are met.


# Usage
```shell

python long_running_code.py --hooks hooks/do_something.py hooks/do_something_else.py
```
