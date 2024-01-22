def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    if list1[0]==0:
        list1[0]=False
    if list1[1]==0:
        list1[1]=False
    if list1[2]==0:
        list1[2]=False
    if list1[3]==0:
        list1[3]=False
    if list1[4]==0:
        list1[4]=False
    if list1[0]==1:
        list1[0]=True
    if list1[1]==1:
        list1[1]=True
    if list1[2]==1:
        list1[2]=True
    if list1[3]==1:
        list1[3]=True
    if list1[4]==1:
        list1[4]=True
    return list1
print(main([1, 0, 0, 0, 0]))