class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(p, q):




class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue = []
        queue.append([p, q])
        while len(queue) != 0:
            childs = queue.pop()
            pChild = None
            qChild = None
            if len(childs) > 1:
                qChild = childs[1]
            if len(childs) > 0:
                pChild = childs[0]
            if pChild != None and qChild != None:
                if (pChild.val != qChild.val):
                    return False

                childsR = []
                if pChild.right:
                    childsR.append(pChild.right)

                if qChild.right:
                    childsR.append(qChild.right)

                childsL = []
                if pChild.left:
                    childsL.append(pChild.left)

                if qChild.left:
                    childsL.append(qChild.left)
                if len(childsL) > 0:
                    queue.append(childsL)
                if len(childsR) > 0:
                    queue.append(childsR)

            elif pChild == None and qChild != None:
                return False
            elif pChild != None and qChild == None:
               return False

        return True
