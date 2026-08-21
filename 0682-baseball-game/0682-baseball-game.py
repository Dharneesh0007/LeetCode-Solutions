class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] # Namma scores-ai store panna oru empty list (stack)
        
        for op in operations:
            if op == '+':
                # Kadaisiya irukka rendu scores-ai add panni stack-la podrom
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # Kadaisiya irukka score-ai double (x2) panni podrom
                stack.append(stack[-1] * 2)
            elif op == 'C':
                # 'C' vantha, kadaisiya ulla score-ai delete (pop) pannidurom
                stack.pop()
            else:
                # Matha padi numbers vantha, atha integer ah maathi stack-la podrom
                stack.append(int(op))
                
        # Kadaisiya stack-la irukka ella scores-oda sum-ai return panrom
        return sum(stack)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna