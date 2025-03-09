class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        # Initialize bad for the first window: positions 0 to k-1
        bad = 0
        for j in range(k - 1):
            if colors[j % n] == colors[(j + 1) % n]:
                bad += 1
        
        res = 0
        if bad == 0:
            res += 1  # First window is alternating
        
        # Slide the window from i=1 to i=n-1
        for i in range(1, n):
            # Remove the pair that is leaving: (i-1, i)
            if colors[(i - 1) % n] == colors[i % n]:
                bad -= 1
            # Add the new pair entering: (i+k-2, i+k-1)
            if colors[(i + k - 2) % n] == colors[(i + k - 1) % n]:
                bad += 1
            if bad == 0:
                res += 1
        
        return res