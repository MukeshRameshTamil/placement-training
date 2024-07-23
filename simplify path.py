class Solution:
    def simplifyPath(self, path: str) -> str:
        l=path.split('/')
        m=[]
        for i in l:
            if i == '..'and len(m) > 0:
                m.pop()
            elif i!='.' and i!='' and i!='..':
                m.append(i)
        
        return  '/'+'/'.join(m)
        
