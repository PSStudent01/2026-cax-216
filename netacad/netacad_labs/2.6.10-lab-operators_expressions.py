'''
2.6.10   LAB   Operators and expressions
Scenario
Your task is to complete the code in order to evaluate the following expression:
The result should be assigned to y. Be careful ‒ watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

[See image '2.6.10-lab-operators-expressions.png']

You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.
'''
x = float(input("Enter number: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / (x + 1 / x))))
print(y)

'''
[[[No worries — this is a classic continued fraction, and it looks way scarier than it actually is once you read it from the bottom up. Let me break it down.

What the image represents mathematically:

Reading from the innermost part outward, the expression is:

y = 1 / (x + 1/(x + 1/(x + 1/(x + 1/x))))

Let's build it up piece by piece, starting from the deepest fraction:

Innermost: x + 1/x
Next layer out: x + 1/(x + 1/x)
Next layer out: x + 1/(x + 1/(x + 1/x))
Outermost: 1 / (x + 1/(x + 1/(x + 1/(x + 1/x)))) ← this whole thing is y

Why this matters for your code: each layer is nested inside the denominator of the layer above it. That's why the hint says "use as many parentheses as you need" — you need to carefully nest parentheses to match each layer exactly, or Python will calculate the wrong thing due to order of operations. ]]]
'''