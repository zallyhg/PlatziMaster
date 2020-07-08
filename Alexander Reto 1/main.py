def ordenamientoBurbuja(m_list):
    for numPasada in range(len(m_list)-1,0,-1):
        for i in range(numPasada):
            if m_list[i]>m_list[i+1]:
                temp = m_list[i]
                m_list[i] = m_list[i+1]
                m_list[i+1] = temp


def finda0(m_list, a0):
    for i in range(len(m_list)):
        if a0 == m_list[i]:
            return i 

if __name__ == "__main__":
    m_list = [25,6,8,9,2,3,5,1]
    a0 = m_list[0]
    
    ordenamientoBurbuja(m_list)

    where_is_a0 = finda0(m_list, a0)
    print(where_is_a0)