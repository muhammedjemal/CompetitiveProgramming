class NumMatrix:

    def init(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixsum = [[] for _ in range(len(matrix))]
        self.sum = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.sum += matrix[i][j]
                self.prefixsum[i].append(self.sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        self.sum = 0
        for i in range(row1,row2+1):
            diff = self.prefixsum[i][col2]-self.prefixsum[i][col1] 
            self.sum += diff+self.matrix[i][col1]

        return self.sum
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
