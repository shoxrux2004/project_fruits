def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    rows=data.split('\n')
    data=[]
    l=[]
    for row in rows[:-1]:
        data.append(row.split(','))
    for i in range(1,len(data)):
        price=(data[i][0])
        print(price)     
    return price
f=open('fruits.csv')
print(get_frutis_name(f.read()))
    

    