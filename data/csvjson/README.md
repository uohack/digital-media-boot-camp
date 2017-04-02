This tutorial walks you through a single, unique example of how you could convert a simple CSV file into JSON. The trick here is that the JSON file will have a different unique key than the CSV file.

### Here's the scenario

You are given an unordered CSV file that contains information about some people and the type of car that they own. Your goal is transform that data into JSON that is grouped by the make of the car.

There are many, many, many ways to do this but the method below is one way it could be done.

# Introduction

### Get to know the data

You have data about people and the type of car they own.

Let's assume this data is properly structured because it came from an Excel or a Google Form.

The data is organized by the person's name. In other words, the name is the unique key of the CSV.

You can infer the data is ordered by the time and date the data was entered. This is of no use to you so the data is, for all intents and purposes, unordered.

To be specific, the data fields are: name, make, model and color.

Name refers to a person's first name. Make, model and color are characteristics of the person's car.

The initial data can be found in demo.csv and looks like this:

```csv
name,make,model,color
Rob,Toyota,4Runner,gold
John,Honda,Accord,silver
Audrey,Mini,Cooper,silver
Dani,Hyundai,Eleantra,blue
Janette,Honda,Pilot,black
Dale,Ford,Mustang,red
```

### Goals

The goal of this process is to take this data and transform it into JSON where the data is grouped by the make of the car.

This could be described as a two-dimensional JSON array with the make of the car as the top-level primary key. For simplicity's sake, let's make the name the second level primary key.

So the JSON will be grouped by car make and ordered within those makes by the person's name.

The data should look something like this:

```json
[
	{
		"Ford": [
			{
				"name": "Dale",
				"model": "Mustang",
				"color": "red"
			}
		]
	},
	{
		"Honda": [
			{
				"name": "Janette",
				"model": "Pilot",
				"color": "black"
			},
			{
				"name": "John",
				"model": "Accord",
				"color": "silver"
			}
		]
	},
	...
]
```

# Getting started

### Clean the data

First, we need to make our lives easier by cleaning the data. In other words, we need to manipulate the data to make writing a script easier.

This could include removing duplicates, removing rows with missing data, re-ordering the data or doing any number of other things.

In our situation, the data is complete and there are no duplicated rows.

Assuming we loop over this data in a Python script, it is always good to order the data based on your primary key, then your secondary key.

So let's re-order the data to be like so:

```csv
name,make,model,color
Dale,Ford,Mustang,red
Janette,Honda,Pilot,black
John,Honda,Accord,silver
Dani,Hyundai,Eleantra,blue
Audrey,Mini,Cooper,silver
Rob,Toyota,4Runner,gold
```

**Note, we've ordered the CSV based on the make and then a secondary order based on the name. So Ford comes before Honda and Janette - Honda comes before John - Honda.**

### Requirements

I will not use any modules that are not available in the standard distribution. AKA: You won't need to download anything special, if you have Python 2.7 installed on your machine.

If you're interested in deeper data analysis, check out [Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html). Be fore-warned, installing Pandas can be a real pain, but it's an extremely powerful tool.

# Write some code

## Reading a CSV file

So, first we need to read out of a csv file. Create a new file called script.py.

`script.py`
```python

import csv

csvfile = open('demo02.csv', 'r')

# See: https://docs.python.org/2/library/csv.html#csv.DictReader
reader = csv.DictReader(csvfile)

for row in reader:
    # For testing purposes, let's just print out the name right now
    print row["make"]


```

You should see:

```
Ford
Honda
Honda
Hyundai
Mini
Toyota
```

Ok, now that we know we have access to the file, let's dig in.


## Mimic JSON structure

Let's try to print out some data that mimics what we want the JSON to look like.

The goal here will be to print out data in this structure:

`Make: Name [Additional name, if it exists]`

In other words, we want to loop through the file and print out a single line for each unique Make, and include all applicable names on that single line.

```python
import csv

csvfile = open('demo.csv', 'r') # This assumes you've ordered the CSV properly

# See: https://docs.python.org/2/library/csv.html#csv.DictReader
reader = csv.DictReader(csvfile)

lastmake = ""
name = ""
for row in reader:
    make = row["make"]
    if lastmake == make:
        name += row["name"]
    else:
        name = row["name"]
    print "{0}: {1}".format(make,name)
    lastmake = make

```

If we do something like this, we get: 

```
Ford: Dale
Honda: Janette
Honda: JanetteJohn
Hyundai: Dani
Mini: Audrey
Toyota: Rob
```

...which is not exactly what we're looking for.

I've finished the script and thoroughly commented it out in `finished.py`. Please read through that and let me know if you have any questions.
