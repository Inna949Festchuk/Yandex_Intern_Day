# # from pprint import pprint

# def call(weekday, days):
#     if weekday == 'Monday':
#         start = 1
#     elif weekday == 'Tuesday':
#         start = 0 
#     elif weekday == 'Wednesday':
#         start = -1 
#     elif weekday == 'Thursday':
#         start = -2 
#     elif weekday == 'Friday':
#         start = -3 
#     elif weekday == 'Saturday':
#         start = -4 
#     elif weekday == 'Sunday':
#         start = -5 
#     for result in (el for el in range(start, days + 1)):
#         yield result

# el = [el for el in call('Wednesday', 31)]

# out = ['',]
# i = 0
# for k in el:
#     if k <= 0:
#         out.append('..')
#     elif 0 < k < 10:
#         out.append(f'.{k}')
#     else:
#         out.append(k)
#     i += 1
#     if i % 7 == 0:
#         out.append('\n')

# print(*out)

'''= = = = = РЕШЕНИЕ = = = = ='''

def call(weekday, days):
    if weekday == 'Monday':
        start = 1
    elif weekday == 'Tuesday':
        start = 0 
    elif weekday == 'Wednesday':
        start = -1 
    elif weekday == 'Thursday':
        start = -2 
    elif weekday == 'Friday':
        start = -3 
    elif weekday == 'Saturday':
        start = -4 
    elif weekday == 'Sunday':
        start = -5 
   
    out = ['',]
    i = 0
    for k in range(start, days + 1):
        if k <= 0:
            out.append('..')
        elif 0 < k < 10:
            out.append(f'.{k}')
        else:
            out.append(k)
        i += 1
        if i % 7 == 0:
            out.append('\n')

    print(*out)

if __name__ == '__main__':
   
    call('Thursday', 30)


