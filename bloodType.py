

# def survive(blood_type, available_blood_types):
    
#     # blood_list = 
#     # {'O+':  ['O+', 'O-'],
#     # 'A+':   ['A+', 'A-', 'O+', 'O-'],
#     # 'B+':   ['B+', 'B-', 'O+', 'O-'],
#     # 'AB+':  ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
#     # 'O-':   'O-',
#     # 'A-':   ['A-', 'O-'],
#     # 'B-':   ['B-', 'O-'],
#     # 'AB-':  ['AB-', 'A-', 'B-' 'O-']   
#     #  }
    
#     # b_match = False

#     # for b in available_blood_types:
#     #     if b == blood_type:
#     #         b_match = True
#     #         break
#     #     else:
#     #         b_match = False
    
#     # return b_match

#     print(blood_list['AB+'])


# from sets import set 

import types

# print(survive('AB-',['A-', 'B+', 'AB+', 'O+', 'B+', 'B-']))
def survive(blood_type, available_blood_types):
    b_match = False
    
    if not isinstance(available_blood_types,list):
        available_blood_types = [available_blood_types]


    blood_list = {
    'O+':  ['O+', 'O-'],
    'A+':   ['A+', 'A-', 'O+', 'O-'],
    'B+':   ['B+', 'B-', 'O+', 'O-'],
    'AB+':  ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
    'O-':   ['O-'],
    'A-':   ['A-', 'O-'],
    'B-':   ['B-', 'O-'],
    'AB-':  ['AB-', 'A-', 'B-' 'O-']}

    b_Compat = blood_list[blood_type]

    blood = set(b_Compat) & set(available_blood_types)

    if len(blood) > 0:
        b_match = True
    else:
        b_match = False

    return b_match
    


print(survive('O-', ['B+', 'B-', 'A-', 'A+', 'AB+', 'B-', 'B+', 'AB-', 'O-', 'A+', 'A-', 'A+', 'O-', 'B+', 'O-', 'A-', 'B-', 'AB+', 'B+', 'B-', 'AB-', 'AB+']))

# b_match = False

# for b in available_blood_types:
#     if b == blood_type:
#         b_match = True
#         break
#     else:
#         b_match = False

# return b_match