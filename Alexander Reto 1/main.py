def finda0(m_list, a0):
    a0_position = 0
    for number in m_list:
        if a0 > number:
            a0_position += 1
            
    return a0_position

if __name__ == "__main__":
    m_list = [25,6,8,9,2,3,62,55]
    a0 = m_list[0]
    
    where_is_a0 = findA0(m_list, a0)
    print(where_is_a0)