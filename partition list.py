
class Solution(object):
    def __init__(self):
        self.list_of_values=[] #List of values in LL
        self.list_greater=[] #List of greater values than partition value
        self.list_smaller=[] #List of smaller values than partition value

    
    def arrange_elements(self,elements, partition_value):
        for element in elements:
            print(element)
            if element >=partition_value:
                self.list_greater.append(element)
            else:
                self.list_smaller.append(element)
        return self.list_smaller+self.list_greater #Simple list addition
    
    def partition(self, head, x):
        current_node=head
        if current_node is None: #Condition to check if only 1 element in LL
            return current_node
        else :
            while(current_node is not None):
            #While loop to save all the elements in the LL into a list
                self.list_of_values.append(current_node.val)
                current_node=current_node.next
        self.list_of_values=(self.arrange_elements(self.list_of_values, x)) #Call the sorting function to obtain return order

        if len(self.list_of_values)>1:
            root_node=ListNode(self.list_of_values[0])
            current_node=root_node
            for x in range(1,len(self.list_of_values)):
                dummy_node=ListNode(self.list_of_values[x])
                current_node.next=dummy_node
                current_node=current_node.next
            return root_node
        else :
            return ListNode(self.list_of_values[0])
