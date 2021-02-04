import pandas as pd
import matplotlib.pyplot as plt



def first(a,b):

    #length = len(a)    

    """                                 # checks if there are any NULL points
    for i in range(length):             # but there aren't any
        if a[i] == 0 and b[i] == 0:
            a.pop(i)
            b.pop(i)
            length -= 1
            print("ahh")
    """        
    
    plt.scatter(a,b)
    plt.xlabel("Total Listings")
    plt.ylabel("Average Review Score")
    plt.show()
    
    return

def second(a,b):
    
    plt.scatter(a,b)
    plt.xlabel("Total Listings")
    plt.ylabel("Average Review Score")
    plt.xlim(0,55)                     # to get a better view of 0-55 listings
    plt.show()
    
    return

df = pd.read_csv(
    r'C:\Users\Jamie\Documents\Employment\Company Prep\Kleene.ai\Q4_Kleene.csv'
    , delimiter = ',', header=None, 
    names = ['host_name', 'total_listings', 'avg_review_score'], 
    usecols = [0,1,2], skiprows=1)

x = list(df.total_listings)
y = list(df.avg_review_score)

first(x,y)
second(x,y)
