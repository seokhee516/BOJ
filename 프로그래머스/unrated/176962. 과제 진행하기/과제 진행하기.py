def solution(plans):
    ans = []
    stack = []
    plans = sorted(plans, key=lambda x:x[1])
    for sub, s, t in plans:
        h, m = map(int, s.split(':'))
        s = 60*h+m
        t = int(t)
        if stack:
            prev_sub, prev_s, prev_t = stack.pop()
            extra_t = s - prev_s
            if extra_t < prev_t:
                stack.append((prev_sub, prev_s, prev_t-extra_t))
            else:
                ans.append(prev_sub)
                extra_t -= prev_t
                while stack and extra_t:
                    prev_sub, prev_s, prev_t = stack.pop()
                    if extra_t < prev_t:
                        stack.append((prev_sub, prev_s, prev_t-extra_t))
                        break
                    else:
                        ans.append(prev_sub)
                        extra_t -= prev_t
            
        stack.append((sub, s, t))

    ans.extend([s for s, _, _ in stack[::-1]])
    
    return ans