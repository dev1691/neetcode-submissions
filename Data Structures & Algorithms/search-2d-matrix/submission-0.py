class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recc_search_rows(rows,target):
            if len(rows)==1:
                if rows[0]==target:
                    return True
                else:
                    return False
            hlf=len(rows)//2
            rows1=rows[:hlf]
            rows2=rows[hlf:]
            result1 = recc_search_rows(rows1,target)
            if result1!=False:
                return result1
            result2 = recc_search_rows(rows2,target)
            return result2

        def recc_search(matrix,target):
            if len(matrix)==1:
                return recc_search_rows(matrix[0],target)
            hlf=len(matrix)//2
            matrix1=matrix[:hlf]
            matrix2=matrix[hlf:]
            result1 = recc_search(matrix1,target)
            if result1!=False:
                return result1
            result2 = recc_search(matrix2,target)
            return result2
        return recc_search(matrix,target)


