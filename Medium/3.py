def lengthOfLongestSubstring(s: str) -> int:
        lis = []
        ans = []
        for i in s:
            lis.append(i)
        for i in range(0,len(lis)):
            st = []
            for j in range(i,len(lis)):
                if lis[j] in st:
                    break
                else:
                    st.append(lis[j])
            ans.append(len(st))
        if len(ans) == 0:
            ans.append(0)
        return max(ans)

s3 = "abcabcbb"
print(lengthOfLongestSubstring(s3))