class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookings.sort(key=lambda k:k[0])
        store=[]
        p=[0] * n
        
        for srt,en,se in bookings:
            store.append((srt - 1,se))
            store.append((en , -se))
         
        store.sort()
        for i in store:
            if i[0] < n:
                p[i[0]] +=i[1]
            
        for i in range(1,n):
            p[i] +=p[i - 1]
            
        return p