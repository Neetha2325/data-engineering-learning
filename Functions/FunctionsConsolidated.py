#1.Default Parameter
def greetings(greet,to="World!"):
    return(greet+" "+to)

g=greetings("Hey")
print(g)

#2.keyword argument
def greetings(greet,to="World!"):
    return(greet+" "+to)
g=greetings(to="Dev",greet="Hello")
print(g)

#3.Variable Length Argument
#Packing fn -->*-tuple  and **-dictionary
def grocery_order(cust_name,*items,delivery_type="Home",**items_with_qty):
    print("Customer name:",cust_name)
    print("Items:",str(items))
    print("Delivery type:",delivery_type)
    print("Items with quantity:",str(items_with_qty))

grocery_order("XYZ","Bread","Balloon",honey=1,rice=2)

#4.Unpacking argument
argList=["Tooth Paste","Sambar Masala","Rasam Powder"]
argDict={"kellogs":5,"Tamarind":"250 g"}
grocery_order("XYZ",*argList,**argDict)


#5.lambda function
f=lambda x,y:x+y
print(f(1,2))

def apply_ops(*args,ops):
    return ops(args)
print(apply_ops(1,2,3,ops=sum))

num_list=[[1,2,3],[4,5,6],[7,8,9],[2,5,16]]
print(max(num_list,key=lambda x:x[2]))

num_list2=[1,2,3,4,5]
fn=map(lambda x:x*x,num_list2)
print(list(fn))