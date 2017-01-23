import csv
import json

# Crack open CSV data
csvfile = open('demo.csv', 'r')
# Reads the CSV, see: https://docs.python.org/2/library/csv.html#csv.DictReader
reader = csv.DictReader(csvfile)

# Prepare JSON file for writing later
jsonfile = open('demo.json', 'w')

# Set up necessary vars
make = "" # Car make
subdata = {} # Metadata for each row as a Python dictionary
data = {} # Python dictionary that will be set on a per-row basis like this: { Model: subdata }
stuff = {} # Python dictionary to collect append data dictionaries to.

# Loop over each row of the CSV
for row in reader:
    
    # Get make of each row
    make = row["make"]
    #print type(make) # For testing
    
    # Set metadata about each row, we ignore color because we don't need it, 
    # ... this also could have been removed in cleaning process
    # ... More specifically, we're creating a list of dictionaries here, 
    # ... the list only has one item at first, but
    # ... if the make has more than one person, we can append to this list, and
    # ... the Python dictionary has two keys.
    subdata = [{'name': row['name'],'model': row['model']}]
    #print subdata # For testing
    
    # Create Python dictionary of the make (key) to the metadata (values)
    data = { make: subdata }

    # Test to see if the current make has already been added to stuff
    # ... This would evaluate to TRUE if the make was NOT in the stuff dictionary
    if make not in stuff:
        # Add data to the dictionary
        stuff.update( data )
    # The above conditional would evaluate to FALSE, calling this block, if the make was already in the stuff dictionary,
    # ... AKA: The make is already present
    else:
        # In this case, we simply append the subdat to the list value of the make key that's already in stuff
        stuff[make] += subdata    
    
    #print stuff # For testing
    #print "----------------" # For testing


#print stuff # For testing
#print json.dumps(stuff) # For testing

# Convert dictionary to JSON
json.dump(stuff, jsonfile, indent=4, sort_keys=True)

