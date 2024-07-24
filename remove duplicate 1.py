
class Solution(object):
    def deleteDuplicates(self, head):
       
        cur = head 
        hashmap = {}
        head2 = None
        finl_head  = None
        while cur is not None:
            if cur.val in hashmap:
                
                cur = cur.next
            
            else:

                hashmap[cur.val] = 0

                if head2 is None:

                    head2 = ListNode(cur.val)
                    finl_head = head2
                    
                    

                else:    
                    node  =  ListNode(cur.val)

                    
                    
                    while head2.next is not None:
                        head2 = head2.next
                        

                    head2.next = node    

                cur = cur.next 
        
        return finl_head
       

                 
        
        
