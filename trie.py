class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def Add(self,word):
        CurrentNode=self.root
        for character in word:
            if character not in CurrentNode.children:
                CurrentNode.children[character]=TrieNode()
            CurrentNode=CurrentNode.children[character]
        CurrentNode.isEnd=True
    def Search(self,word):
        CurrentNode=self.root
        for character in word:
            if character not in CurrentNode.children:
                return False
            CurrentNode=CurrentNode.children[character]
        if CurrentNode.isEnd==True:
            return True             
        return False 
    
    def Remove(self,word):
        if not self.Search(word):
            print("word not found...can't remove")
            return
        stack=[]
        
        CurrentNode=self.root
        for character in word:
            stack.append(CurrentNode)
            CurrentNode=CurrentNode.children[character]
        CurrentNode.isEnd=False
        
        while (len(stack)>0):
            node=stack.pop()
            char=word[len(stack)] 
            
            if not node.children[char].isEnd and not node.children[char].children:
                del node.children[char]
            else:
                break
        print("Word removed")
                
                 
    
            
            
    
    
trie=Trie()
#trie.Add("GO")
#trie.Add("GOOD")
#trie.Add("APPLE")
#trie.Add("APPLICATION")
trie.Add("APP")
trie.Remove("APP")
#print(trie.Search("GOOD"))