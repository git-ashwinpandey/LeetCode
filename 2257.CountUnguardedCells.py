def countUnguarded(m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        

        copy_mat = [[0] * n for _ in range(m)]

        for wall in walls:
            i, j = wall[0], wall[1]
            copy_mat[i][j] = 2
        
        for guard in guards:
            i, j = guard[0], guard[1]
            copy_mat[i][j] = 3

        check = (2, 3)

        for guard in guards:
            i, j = guard[0], guard[1]

            #right
            tmp = j + 1
            while tmp < n and copy_mat[i][tmp] not in check:
                copy_mat[i][tmp] = 1
                tmp += 1
            
            #left
            tmp = j - 1
            while 0 <= tmp and copy_mat[i][tmp] not in check:
                copy_mat[i][tmp] = 1
                tmp -= 1

            #bottom
            tmp = i + 1
            while tmp < m and copy_mat[tmp][j] not in check:
                copy_mat[tmp][j] = 1
                tmp += 1
            
            #top
            tmp = i - 1
            while 0 <= tmp and copy_mat[tmp][j] not in check:
                copy_mat[tmp][j] = 1
                tmp -= 1
        
        unguarded = 0
        for r in range(m):
            for c in range(n):
                if copy_mat[r][c] == 0:
                    unguarded += 1

        return unguarded