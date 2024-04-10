class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
        
def insert(temp,key):
    if temp is None:
        return Node(key) 
    else:
        if temp.val<key:
            temp.right=insert(temp.right,key)
        elif temp.val>key:
        	temp.left=insert(temp.left,key)
        return temp
    
def inorder(t):
    if t is None:
        return
    inorder(t.left)
    print(t.val,end=' , ')
    inorder(t.right)
    
def postorder(t):
    if t is None:
        return
    postorder(t.left)
    postorder(t.right)
    print(t.val,end=' , ')
    
def preorder(t):
    if t is None:
        return
    print(t.val,end=' , ')
    preorder(t.left)
    preorder(t.right)

def height(t):
    if t is None:
        return 0
    else:
        lh=height(t.left)
        rh=height(t.right)
        if lh>rh:
            print(lh+1)
        else:
            print(rh+1)
    
root=Node(100)
while True:
    print("Enter your choice :")
    print("1 . Insert ")
    print("2 . Print Inorder " )
    print("3 . Print Post order " )
    print("4 . Print Pre order " )
    print("5 . Calculate Height ")
    k=int(input())
    if k==1:
        v=int(input())
        insert(root,v)
    elif k==2:
        print("Inorder Traversal : ")
        inorder(root)
        print(' ')
    elif k==3:
        print("Post Order Traversal is : ")
        postorder(root)
        print('')
    elif k==4:
        print("Pre Order Traversal is : ")
        preorder(root)
        print('')
    elif k==5:
        print("Height of the BST is : ")
        height(root)
        print("")
    else:
        break
