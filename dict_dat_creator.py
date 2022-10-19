import pickle

def main():
    outfile = open('dict.dat', 'wb')
    dict1 = { 'item': [9.99, 7], 'item2': [11.89, 9], 'item3': [3.99, 4] }

    print(dict1)

    pickle.dump(dict1, outfile)

    outfile.close()


main()
    
