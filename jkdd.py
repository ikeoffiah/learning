def sliding_window(array,k):
    left_pointer = 0
    right_pointer = k
    largest_sum = 0
    sub_array = array
    last_sum = 0

    if(len(array) < k):
        sub_array = array
        return {
        "larget_sum":sum(array),
        "sub_array": sub_array
    }

    while right_pointer <= len(array):

        if(left_pointer == 0):
            largest_sum = sum(array[:right_pointer])
            last_sum = largest_sum
        else:

            current_sum = (last_sum - array[left_pointer-1]) + array[right_pointer-1]
            last_sum = current_sum
            if current_sum > largest_sum:
                largest_sum = current_sum
                sub_array = array[left_pointer:right_pointer]

        left_pointer +=1
        right_pointer +=1

    return {
        "larget_sum":largest_sum,
        "sub_array": sub_array
    }




# print(sum([1,2,3]))
array = [1, 5, 20, 3, 10, 5]
# k = 4
# print(sum(array[:2]))
# print(sliding_window(array=array, k=k))
# print(array[0:2])


def sliding_window2(array, sum_value):
    print(array)
    left_anchor = 0
    right_anchor = 1
    left_move = False
    right_move = False
    if len(array) >= 2:
        current_sum = array[0] + array[1]
    elif array[0] == sum_value:
        return array
    else:
        return None

    while right_anchor < len(array):

        distance = right_anchor - left_anchor

        if(left_move):
            current_sum = current_sum - array[left_anchor-1]

            left_move = False

        if(right_move):
            current_sum = current_sum + array[right_anchor]

            right_move = False

        if(current_sum == sum_value):
            return array[left_anchor: right_anchor + 1]

        if(distance == 1 and current_sum > sum_value):
            left_anchor += 1
            left_move = True
            right_move = True
            right_anchor += 1

        if(distance == 1 and current_sum < sum_value):
            right_anchor += 1
            right_move = True

        if(distance > 1 and current_sum < sum_value):
            right_anchor +=1
            right_move = True

        if(distance > 1 and current_sum > sum_value):
            left_anchor += 1
            left_move = True





#
#
# print(sliding_window2([7, 4, 0, 0, 3, 10, 5], 7))


def sliding_window3(array, k):
    left_anchor = 0
    right_anchor = k -1
    contiguous_array = []



    while right_anchor < len(array):

        sub_list = array[left_anchor : right_anchor + 1]

        highest_value = sorted(sub_list)[-1]
        contiguous_array.append(highest_value)

        right_anchor +=1
        left_anchor +=1


    return contiguous_array


# print(sliding_window3([2, 3, 7, 9, 5, 1, 6, 4, 3], 3))


def sliding_window4(array, k):
    left_anchor = 0
    right_anchor = 1

    left_move = False
    right_move = False
    highest_length = 0
    the_arr = []
    current_sum = 0


    if len(array) == 1:
        current_sum = array[0]
        if array[0] == k:
            highest_length = len(array)
            the_arr = array
            return [highest_length, the_arr]
    else:
        current_sum = array[0] + array[1]


    while right_anchor < len(array):
        distance = right_anchor - left_anchor
        if (left_move):
            current_sum = current_sum - array[left_anchor - 1]
            left_move = False

        if (right_move):
            current_sum = current_sum + array[right_anchor]
            right_move = False

        if current_sum == k:
            print("here")
            the_arr = array[left_anchor: right_anchor + 1]
            highest_length = len(the_arr)
            right_anchor +=1
            left_anchor +=1
            right_move = True
            left_anchor = True



        if(distance == 1 and current_sum < k):
            right_anchor +=1
            right_move = True

        if(distance == 1 and current_sum > k):
            right_anchor += 1
            left_anchor += 1
            right_move = True
            left_anchor = True

        if(distance > 1 and current_sum < k):
            right_anchor += 1
            right_move = True

        if(distance > 1 and current_sum > k):
            left_anchor +=1
            left_move = True
        print([highest_length, the_arr])

    return [highest_length, the_arr]



print(sliding_window4([10, 5, 2, 7, 1, 9], 15))



