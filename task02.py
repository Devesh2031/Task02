{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e1328ce4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 5\n",
      "The difference is: 12.0\n"
     ]
    }
   ],
   "source": [
    "#write a python program to calculate the difference between a given number and 17\n",
    "#if the number is greater than 17, return twice the absolute difference\n",
    "num = float(input(\"Enter a number: \"))\n",
    "if num > 17:\n",
    "    diff = abs(num - 17) * 2\n",
    "else:\n",
    "    diff = 17 - num\n",
    "print(\"The difference is:\", diff)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fd91fda5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a year: 2022\n",
      "2022 is not a leap year\n"
     ]
    }
   ],
   "source": [
    "# write a python program to check if a year is leap or not?\n",
    "year = int(input(\"Enter a year: \"))\n",
    "if year % 4 == 0:\n",
    "    if year % 100 == 0:\n",
    "        if year % 400 == 0:\n",
    "            print(year, \"is a leap year\")\n",
    "        else:\n",
    "            print(year, \"is not a leap year\")\n",
    "    else:\n",
    "        print(year, \"is a leap year\")\n",
    "else:\n",
    "    print(year, \"is not a leap year\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6ed21f51",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first integer: 4\n",
      "Enter second integer: 6\n",
      "Enter third integer: 3\n",
      "Sum is 13\n"
     ]
    }
   ],
   "source": [
    "# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero\n",
    "a = int(input(\"Enter first integer: \"))\n",
    "b = int(input(\"Enter second integer: \"))\n",
    "c = int(input(\"Enter third integer: \"))\n",
    "if a == b or b == c or c == a:\n",
    "    print(\"Sum is zero\")\n",
    "else:\n",
    "    sum = a + b + c\n",
    "    print(\"Sum is\", sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f55539ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the name of the month: july\n",
      "July has 31 days\n"
     ]
    }
   ],
   "source": [
    "#Write a Python program to convert a month name to a number of days\n",
    "inputt = input(\"Enter the name of the month: \")\n",
    "month_name=inputt.title()\n",
    "if month_name in (\"January\", \"March\", \"May\", \"July\", \"August\", \"October\", \"December\"):\n",
    "    num_days = 31\n",
    "elif month_name in (\"April\", \"June\", \"September\", \"November\"):\n",
    "    num_days = 30\n",
    "elif month_name == \"February\":\n",
    "    num_days = 28  # or 29 for leap years\n",
    "else:\n",
    "    num_days = 0\n",
    "\n",
    "if num_days > 0:\n",
    "    print(month_name, \"has\", num_days, \"days\")\n",
    "else:\n",
    "    print(\"Invalid month name\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6e67c791",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the length of side a: 5\n",
      "Enter the length of side b: 6\n",
      "Enter the length of side c: 5\n",
      "This is an isosceles triangle\n"
     ]
    }
   ],
   "source": [
    "#Write a Python program to check if a triangle is equilateral, isosceles or scalene\n",
    "a = float(input(\"Enter the length of side a: \"))\n",
    "b = float(input(\"Enter the length of side b: \"))\n",
    "c = float(input(\"Enter the length of side c: \"))\n",
    "\n",
    "if a == b == c:\n",
    "    print(\"This is an equilateral triangle\")\n",
    "elif a == b or b == c or c == a:\n",
    "    print(\"This is an isosceles triangle\")\n",
    "else:\n",
    "    print(\"This is a scalene triangle\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92a7416a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}