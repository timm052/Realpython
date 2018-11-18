#%%
import argparse
import csv
import sys, os 

#%%
def main():
    # set up command line arguments to parse 
    parser = argparse.ArgumentParser(
    description = "An application for spliting csv files")

    parser.add_argument('-i', '--input', type = str, help = 'input file location as path')
    parser.add_argument('-o', '--output', type = str, help = 'output file location as path')
    parser.add_argument('-r', '--rowlimit', type = int, help = 'row limit to split as int')

    args = parser.parse_args()
    
    # create variables for arguments and subsitute default values if no arguments are given
    input_file_location = args.input
    checkForInput(input_file_location)  
    ##input_file_location = r"E:\Programming\Realpython\Fundamentals\Chapter 7\FL_insurance_sample.csv" 
    output_file_location = checkForArgument(args.output, os.path.dirname(input_file_location))
    ##output_file_location = r"E:\Programming\Realpython\Fundamentals\Chapter 7\test"
    rowlimit = checkForArgument(args.rowlimit, 25)
    ##rowlimit = checkForArgument(None, 100)

    # test if input file exists
    if file_exists(input_file_location):
        pass
    else:
        return print("error: file does not exist")

    #check that the number of rows is greater than the split value
    if length_greater_split(rowlimit, input_file_location):
        pass
    else:
        return print("error: split interval exceeds number of rows")
    
    splitcsv(input_file_location, output_file_location, rowlimit)        

#%%
def checkForInput(input_file):
    if input_file == None:
        sys.exit("error: no input file location use -h for help") 
    else:
        return
#%%
# input check
def checkForArgument(argument, default):
    if argument == None:
            return default
    else:
            return argument 

#%%
# Check that the input file exists
def file_exists(input):
    if os.path.isfile(input):
        return True

#%%
# Check the there are enough rows to allow a split 
def length_greater_split(rowlim, inputpath):
    with open(inputpath) as open_file:
        open_file_reader = csv.reader(open_file)
        data = list(open_file_reader)
        numRows = len(data)

    if numRows > rowlim:
        return True

#%%
#split csv file
def splitcsv(inputpath, outputpath, row_limit):
    with open(inputpath) as open_file:
        open_file_reader = csv.reader(open_file)
        header = next(open_file_reader)
        loop = 0
        part_number = 0
        filename = os.path.basename(inputpath)
        list_rows = []

        for row in open_file_reader:
            list_rows.append(row)

        while (part_number*row_limit) < len(list_rows):
            # create numbered output file, open in cs writer and write header row
            with open((outputpath + "\\" + filename[0:-4] + "_" + str(part_number)) + ".csv", "w", newline='') as output:
                open_file_writer = csv.writer(output)
                open_file_writer.writerow(header)
                
                # write 
                for row in list_rows[part_number*row_limit:]:
                    if loop < row_limit:
                        open_file_writer.writerow(row)
                        loop += 1
                    else:
                        break
                loop = 0
                part_number += 1

#%%
if __name__ == '__main__':
    main()
