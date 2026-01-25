from functools import reduce

ProductOfAll= lambda a,b : a*b


def main():
    data=[10,5,3,4,20]
    print("Actual Data is: ",data)

    RData=reduce(ProductOfAll,data)
    print("Product of all elements  : ",RData)


if __name__=="__main__":
    main()