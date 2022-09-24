class Solution:
    def minWindow(self, s: str, t: str) -> str:
#        String window = "";
#         int j = 0, min = S.length() + 1;
#         for (int i = 0; i < S.length(); i++) {
#             if (S.charAt(i) == T.charAt(j)) {
#                 j++;
#                 if (j == T.length()) {
#                     int end = i + 1;
#                     j--;
#                     while (j >= 0) {
#                         if (S.charAt(i) == T.charAt(j)) j--;
#                         i--;
#                     }
#                     j++;
#                     i++;
#                     if (end - i < min) {
#                         min = end - i;
#                         window = S.substring(i, end);
#                     }
#                 }
#             }
#         }
#         return window;
        res=""
        j=i=0
        n=len(s)
        m=len(t)
        mn=n+1
        while i<n:
            if s[i]==t[j]:
                j+=1
                
                if j==m:
                    j-=1
                    end=i+1
                    while j>=0:
                        if s[i]==t[j]:
                            j-=1
                        i-=1
                    i+=1
                    j+=1
                    
                    if end-i<mn:
                        mn=end-i
                        res=s[i:end]
            i+=1
        return res
        