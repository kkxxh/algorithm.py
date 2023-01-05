def solution(new_id):
    
    # 1
    new_id = new_id.lower()
    
    # 2
    for id in new_id:
        if id.isalpha() or id.isdigit() or id == '.' or id =='_' or id =='-':
            continue
        else:
            new_id = new_id.replace(id,'')
    
    # 3        
    while '..' in new_id:
        new_id = new_id.replace('..','.')

    #4
    if new_id[0] =='.' and len(new_id) > 1:
        new_id = new_id[1:] 
    if new_id[-1] == '.':
        new_id = new_id[:-1]
        
    #5
    if len(new_id) == 0:
        new_id = 'a'
    
    #6
    if len(new_id) >15:
        new_id = new_id[:15]
        
    #7
    if len(new_id) <3:
        while len(new_id)<3:
            new_id += new_id[-1]
    
    
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    
    return new_id





# 참고
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st