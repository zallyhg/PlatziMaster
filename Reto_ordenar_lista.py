from random import randint
import argparse

def random_list(llength, llowerBound, lupperBound):
    lrandomList = [randint(llowerBound, lupperBound) for i in range(llength)]
    return lrandomList

def sort_list(unsorted):
    a0 = 0
    numberOfSwaps = 0
    accumNumberOfSwaps = 0
    lunsorted = [i for i in unsorted]
    for i in range(1,len(lunsorted)):
        for j in range(0,len(lunsorted)-i):
            if lunsorted[j+1] < lunsorted[j]:
                aux_var = lunsorted[j]
                lunsorted[j] = lunsorted[j+1]
                lunsorted[j+1] = aux_var
                if j == a0:
                    a0 += 1
                numberOfSwaps += 1
        accumNumberOfSwaps += numberOfSwaps
        print(f'Swaps in iteration {i}: {numberOfSwaps} | Cumulative swaps: {accumNumberOfSwaps}')
        if numberOfSwaps == 0:
            if i < len(lunsorted)-1:
                print('End for loops as list is already ordered')
            break;
        numberOfSwaps = 0
    print("*"*80)
    print(accumNumberOfSwaps)
    return a0, lunsorted


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", default=argparse.SUPPRESS, action='help',
                        help="This program creates a random list of size l (length), sorts the list but"
                                             "tracks down the first element in the original list.")
    parser.add_argument("-l", "--length", default='100',
                        help="Number of elements in the random list. Defaults to 100 if not specified.")
    parser.add_argument("-m", "--min", default='0',
                        help="Min number to be present in random list. Defaults to 0 if not specified.")
    parser.add_argument("-n", "--max", default='100',
                        help="Max number to be present in random list. Defaults to 100 if not specified.")

    args = parser.parse_args()
    # print(f'length: {args.length} | lower: {args.min} | upper: {args.max}')
    unsorted = random_list(int(args.length), int(args.min), int(args.max))
    key, ordered = sort_list(unsorted)
    print(f'\nFirst element of original list: {unsorted[0]}\n')
    print('*'*80)
    print(f'\nSorted list: {ordered}\n')
    print('*'*80)
    print(f'\nFirst element of original list is located at: {key}')