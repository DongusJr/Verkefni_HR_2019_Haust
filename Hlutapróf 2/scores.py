def make_list(user_inp):
    ''' Function that makes a list from the input '''
    score_list = user_inp.split()
    score_list = [float(i) for i in score_list]  # Parse the values in the list into float
    if len(score_list) > 1:  # Needs to be a list that is atleast 2 in length
        return score_list
    else:
        return None

def sort_list_and_remove(score_list):
    ''' Function that sorts the list and removes the two lowest numbers '''
    score_list.sort()
    score_list.pop(0)
    score_list.pop(0)
    return score_list

def get_sum(fixed_list):
    ''' Get's the sum from the sorted list of float numbers'''
    sum_score = 0
    for score in fixed_list:
        sum_score += score
    return sum_score 

def print_results(sum_score):
    print("Sum of scores (two lowest removed): {}".format(sum_score) )

def main():
    ''' The main function '''
    score_inp = input("Enter scores separated by space: ")
    score_list = make_list(score_inp)
    if score_list != None:  # If it's more than 1 element
        sum_score = get_sum(sort_list_and_remove(score_list)) # We sort the list and then get the sum 
        print_results(sum_score)
    else:
        print("At least two scores needed!")

main()
