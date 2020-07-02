# -*- coding: utf-8 -*-
"""
Project 4

@author: Benny
"""
def open_file():
    
    valid= False
    while not valid:
        file= input("enter a file: ")
        try:
            fp = open(file, "r")
            valid = True
            
            
        except FileNotFoundError:
            print("Error. Invalid file name")
    return fp


     
    
def find_min_percent(line):
    minchange = 10000.0
    min_index = 0
    numdata = int((len(line) - 76)/12) + 1
    for i in range(numdata):
        start = 76 + i*12
        end = start + 12
        change = line[start:end].strip()
        float_change = float(change)
        if float_change < minchange:
            min_index = i
            minchange = float_change
    return min_index, minchange
        
def find_max_percent(line):
    '''Find the max percent change in the line.'''
    maxchange = 0
    max_index = 0
    numdata = int((len(line) - 76)/12) + 1
    for i in range(numdata):
        start = 76 + i*12
        end = start + 12
        change = line[start:end].strip()
        float_change = float(change)
        if float_change > maxchange:
            max_index = i
            maxchange = float(change)
    return max_index, maxchange
    

def find_gdp(line, index):
    '''Use the index to find the gdp value in the line'''
    begin = 76 +12*index
    end = begin + 12
    gdp_num =  float(line[begin:end])
    return gdp_num

def find_year(line, index):
    '''Use the index to find the year'''
    begin = 79 +12*index
    end = begin + 12
    year = line[begin:end]
    return year
    


def display(minchange, min_year, min_gdp, maxchange, max_year, max_gdp):
    '''Display values; convert billions to trillions first.'''    
    print('Gross Domestic product \n')
    print('{:<10s}{:>10s}{:>6s}{:>18.3s}\n'.format('min/max', 'change', 'year', 'GDP'))
    print('{:<10s}{:>8.1f}{:>15s}{:>12.2f}\n'.format('min', minchange, min_year, min_gdp*.001))
    print('{:<10s}{:>8.1f}{:>15s}{:>12.2f}\n'.format('max', maxchange, max_year, max_gdp *.001))
    
    
def main():                    
    fp = open_file()
    lines = fp.readlines()
    line = lines[8]
    min_index, minchange = find_min_percent(line) 
    max_index, maxchange = find_max_percent(line)
    line = lines[43]
    min_gdp = find_gdp(line, min_index)
    max_gdp = find_gdp(line, max_index)
    line= lines[7]
    min_year = find_year(line, min_index)
    max_year = find_year(line, max_index)
    display(minchange, min_year, min_gdp, maxchange, max_year, max_gdp)
    
# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.
if __name__ == "__main__":
    main()
