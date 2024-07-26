func luckyNumbers (matrix [][]int) []int {
    hm := make(map[int][]int)
    n := len(matrix)
    m := len(matrix[0]) 

    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            hm[j] = append(hm[j], matrix[i][j])
        }
		
	}
    _min := 100001
    _min_idx := 0
    for r := 0; r < n; r ++{
        for c := 0; c < m; c++{
            if matrix[r][c] < _min {
                _min = matrix[r][c]
                _min_idx = c
            }
        }
        if _min == slices.Max(hm[_min_idx]) {
            return []int{_min}
        }
        _min = 100001
    }
    
    return []int{}
    
}