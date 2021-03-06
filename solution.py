
f = open("input.txt")
#reading the lines from input txt file
input_lines=f.readlines()       
f.close()
#fetching number of employees as M from the string by slicing
M = int(input_lines[0][input_lines[0].index(":")+1:])      
#fetching the goodie list omitting first part of the text file
goodie_list = [x for x in input_lines[4:]]                  
#defining a sort key to sort depending on price of the goodie
def sort_by_price(entry):                                   
    return int(entry[entry.index(":")+1:])
#sorting the goodie list by prices
goodie_list.sort(key=sort_by_price)
#list for least difference between M elements(highest and lowest prices)
least_difference=[]                          
#getting the differences between M elements (highest and lowest prices) and appending            
for i in range(len(goodie_list)-M+1):
    least_difference.append(abs(int(goodie_list[i][goodie_list[i].index(":")+1:])-int(goodie_list[i+M-1][goodie_list[i+M-1].index(":")+1:])))
#writing to the output file and console according to the format
f=open("output.txt","w")
f.write("Here the goodies that are selected for distribution are:\n\n")
print("Here the goodies that are selected for distribution are:\n")
#printing the elements between which we get the least difference
for i in goodie_list[least_difference.index(min(least_difference)):least_difference.index(min(least_difference))+M]:
    print(i,end="")
    f.write(i)
#printing the least difference
print(f"\nAnd the difference between the chosen goodie with highest price and the lowest price is {min(least_difference)}")
f.write(f"\nAnd the difference between the chosen goodie with highest price and the lowest price is {min(least_difference)}")
f.close()