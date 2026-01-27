class Solution:
    def isWordExist(self, mat, word):
        n = len(mat)
        m = len(mat[0])

        def dfs(r, c, idx):
            # If entire word is matched
            if idx == len(word):
                return True

            # Boundary + mismatch check
            if r < 0 or c < 0 or r >= n or c >= m or mat[r][c] != word[idx]:
                return False

            # Mark cell as visited
            temp = mat[r][c]
            mat[r][c] = '#'

            # Explore 4 directions
            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            # Backtrack
            mat[r][c] = temp
            return found

        # Try starting from every cell
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
