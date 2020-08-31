



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        stack=[]
        def findword(i,j,board,words,stack,curr=""):
            if not (0 <= i < m and 0 <= j < n and board[i][j]): 
                return 
            curr=str(curr)+str(board[i][j])
            if str(curr) in words: 
                stack.append(curr)
                words.remove(curr)
            temp, board[i][j] = board[i][j], ""
            choices = [findword(i+di,j+dj,board,words,stack,curr) for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]]
            board[i][j]=temp
            return choices
        m,n = len(board), len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                findword(i,j,board,words,stack)
        return stack


Class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                # the setdefault function In Python Dictionary, setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    