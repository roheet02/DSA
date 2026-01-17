class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        s=0
        bl=bottomLeft
        tr=topRight
        n=len(bl)
        for i in range(n):
            for j in range(i+1,n):
                min_x=max(bl[i][0],bl[j][0])
                max_x=min(tr[i][0],tr[j][0])
                min_y=max(bl[i][1],bl[j][1])
                max_y=min(tr[i][1],tr[j][1])
                if min_x<max_x and min_y<max_y:
                    length=min(max_x-min_x,max_y-min_y)
                    s=max(s,length)
        return s*s
print(Solution().largestSquareArea([[1,1],[2,2],[3,1]],[[3,3],[4,4],[6,6]]))
print(Solution().largestSquareArea([[1,1],[1,3],[1,5]],[[5,5],[5,7],[5,9]]))