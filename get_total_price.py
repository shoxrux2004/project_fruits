def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    rows=data.split('\n')
    data=[]
    sum=0
    for row in rows[:-1]:
        data.append(row.split(','))
    for i in range(1,len(data)):
        price=float(data[i][1])
        sum+=price
    return round(sum,3)
f=open('fruits.csv')
print(get_total_price(f.read()))
    