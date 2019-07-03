# List of all unique Prime_Genres(categories) in the dataset
import pandas as pd
filepath="AppleStore.csv"

# To read CSV file data
def read_csv_file(filepath):
    data=pd.read_csv(filepath)
    return data

# To print unique categories in the store
def unique_categories(data):
    categories=data['prime_genre']
    categories=set(categories)
    print("We have ",len(categories)," unique categories in AppleStore")
    for i in categories:
        print(i,end="  ")
    
# Category with highest number of apps and lowest number of apps
def highest_lowest_category(data):
    categories=data['prime_genre']
    d={}
    for i in range(0,len(categories),1):
        if categories[i] not in d:
            d[categories[i]]=1
        else:
            d[categories[i]]+=1
    high=-1
    low=999999999999999999999999999999999999999999999999999999
    for key,value in d.items():
        if high<=value:
            high=value
            name=key
        if low>=value:
            low=value
            name1=key
    print("\n")
    print(name, "has highest number of apps as ",high)
    print(name1, "has lowest number of apps as ",low)


# Category with highest user rating
def highest_rating(data):
    categories=data['prime_genre']
    Rating=data['user_rating']
    d={}
    
    '''dd={}
    for i in range(0,len(categories),1):
        if categories[i] not in dd:
            dd[categories[i]]=1
        else:
            dd[categories[i]]+=1'''
    
    for i in range(0,len(categories),1):
        if categories[i] not in d:
            d[categories[i]]=Rating[i]
        else:
            d[categories[i]]+=Rating[i]
    
    high=-1
    for key,value in d.items():
        #d[key]=d[key]/dd[key]
        if high<=d[key]:
            high=d[key]
            name=key
    print("\n")
    print(name, "has highest rating as" , "%0.2f"%high)

# Average user rating for free apps
def avg_user_rating_free_apps(data):
    price=data['price']
    rating=data['user_rating']
    count=0
    c=0
    for i in range(0,len(price),1):
        if price[i]==0:
            #print(price[i])
            count+=rating[i]
            c=c+1
    print("Average user rating for free apps is ",count//c)

# Average user rating for paid apps
def avg_user_rating_paid_apps(data):
    price=data['price']
    rating=data['user_rating']
    count=0
    c=0
    for i in range(0,len(price),1):
        if price[i]>0:
            #print(price[i])
            count+=rating[i]
            c=c+1
    print("Average user rating for paid apps is ",count//c)

# Category with highest average user rating for paid apps
def cate_avg_user_rating_paid_apps(data):
    categories=data['prime_genre']
    price=data['price']
    rating=data['user_rating']
    d={}
    dd={}
    for i in range(0,len(price),1):
        if price[i]>0:
            if categories[i] not in d:
                d[categories[i]]=rating[i]
                dd[categories[i]]=1
                
            else:
                d[categories[i]]+=rating[i]
                dd[categories[i]]+=1
    high=-1
    #print(d,"\n",dd)
    for key,value in d.items():
        d[key]=d[key]/dd[key]
        if high<=d[key]:
            high=d[key]
            name=key
    print(name,"has highest average user rating for paid apps.which is ",'%.2f'%high)
    
# Most frequent Price point > 0
def most_freq_price(data):
    price=data['price']
    d={}
    for i in range(0,len(price),1):
        if price[i]>0:
            if price[i] not in d:
                d[price[i]]=1
            else:
                d[price[i]]+=1
    high=-1
    for key,value in d.items():
        if high<=d[key]:
            high=d[key]
            v=key
    print("Most frequent Price point > 0 is ",v)
    #print(d)

#Compare average user rating for paid vs free gaming apps
def avg_user_rating_game(data):
    categories=data['prime_genre']
    price=data['price']
    rating=data['user_rating']
    d={}
    for i in range(0,len(rating),1):
        if categories[i]=='Games':
            if price[i]==0:
                if 'free' not in d:
                    d['free']=1
                    d['free_game']=rating[i]
                else:
                    d['free']+=1
                    d['free_game']+=rating[i]
            else:
                if 'paid' not in d:
                    d['paid']=1
                    d['paid_game']=rating[i]
                else:
                    d['paid']+=1
                    d['paid_game']+=rating[i]
    print(d)
    f=float(d['free_game']/d['free'])
    p=float(d['paid_game']/d['paid'])
    print(f,"    ",p)
    if p>f:
        print("free games (",'%.2f'%f,") <"," paid game (",'%.2f'%p,")")
    elif f==p :
        print("free games (",'%.2f'%f,") =="," paid game (",'%.2f'%p,")")
    else:
        print("free games (",'%.2f'%f,") >"," paid game (",'%.2f'%p,")")
    
data=read_csv_file(filepath)
unique_categories(data)
highest_lowest_category(data)
highest_rating(data)
avg_user_rating_free_apps(data)
avg_user_rating_paid_apps(data)
cate_avg_user_rating_paid_apps(data)
most_freq_price(data)
avg_user_rating_game(data)
