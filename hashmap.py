class HashMap:
    def __init__(self,size=10):
        self.size=size
        self.hashlist=[None]*self.size
    def GetIndex(self,key):
        return hash(key) % self.size
    def __setitem__(self,key,value):
        index=self.GetIndex(key)
        #print(index)
        if self.hashlist[index] is None :
            self.hashlist[index]=[[key,value]]
        else:
            if self.hashlist[index]:
                subList=self.hashlist[index]
                for pairs in subList:
                    if pairs[0]==key:
                         pairs[1]=value
                         return 
            
            self.hashlist[index].append([key,value]) 
    #def Get(self,key):
     #   index=self.GetIndex(key)
        
      #  if self.hashlist[index]:
       #     subList=self.hashlist[index]
        #    for pairs in subList:
         #       if pairs[0]==key:
          #          return pairs[1]    
           #     else:
            #        return"Key not found"
    def __getitem__(self,key):
        index=self.GetIndex(key)
            
        if self.hashlist[index]:
            subList=self.hashlist[index]
            for pairs in subList:
                if pairs[0]==key:
                    return pairs[1]    
                else:
                    return"Key not found"
    def __delitem__(self,key):
        index=self.GetIndex(key)
         
        if self.hashlist[index]:
            subList=self.hashlist[index]
            for i,pairs in enumerate(subList):
                if pairs[0]==key:
                    del subList[i] #self.hashlist[index][i]
                    return
                return"Key not found"
        
        
    
    #  def Add(self,key,value):
     #   index=self.GetIndex(key)
     #   print(index)
      #  if self.hashlist[index] is None :
       #     self.hashlist[index]=[[key,value]]
       # else:
       #     self.hashlist[index].append([key,value])   
    
        
dictonary=HashMap()
#print(dictonary.hashlist)
#dictonary.Add("name","kishore")
dictonary["Name"]="kishore"
dictonary["Name"]="kishore26"
print(dictonary.hashlist)
#dictonary.Add("age",20)
#dictonary["Age"]=20
#print(dictonary.hashlist)
#print(dictonary.Get("Name"))
#print(dictonary["Name"])
#del dictonary["Name"]
#print(dictonary["Name"])
