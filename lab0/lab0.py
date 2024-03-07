def count_pattern(pattern: list, chain: list) -> int:
    """
    Count how many times a given pattern appears in a
    chain of elements.
    """
    pattern_ind = 0
    pattern_count = 0
    for elem in chain:
        if elem == pattern[pattern_ind]:
            pattern_ind += 1

        if pattern_ind == len(pattern) - 1:
            pattern_count += 1
            pattern_ind = 0

    return pattern_count


def depth(expression):
    """
    Compute the depth of a mathematical expression
    Each function it's represented by a tuple of the form:
    ('operation', 'var', val) which resembles the tree data
    structure (node, left, right).
    so, for example:
    exp(2+5) -> ('exp', 'x', ('+', 2, 5)) -> Tree Data Structure
    """
    if not isinstance(expression, (list, tuple)):
        return 0
    
    return 1 + max(depth(expression[1]), depth(expression[2]))


def simplify(expression):
    """
    Reduce nested products and sums of a mathematical expression into
    a single sum of products.
    (x + 1) * (y + 3) = xy + 3x + y + 3y
    ('operation', left, right)
    """
    if not isinstance(expression, list):
        return expression
    
    if expression[0] == "*":
        if isinstance(expression[1], list) and expression[1][0] == "+":
            expression = [
                "+",
                ["*", expression[1][1], expression[2]],
                ["*", expression[1][2], expression[2]]
                ]
            simplify(expression)
        elif isinstance(expression[2], list) and expression[2][0] == "+":
            expression = [
                "+",
                ["*", expression[1], expression[2][1]],
                ["*", expression[1], expression[2][2]]
                ]
            simplify(expression)

    """
    TODO: recursion or iteration? which is clearer?
    """
    

    





def repr_expresion(expresion):
    result = []
    _repr(expresion, result)
    print(" ".join(result))


def _repr(expression, result):
    if isinstance(expression, (tuple, list)):
        result.append("(")
        _repr(expression[1], result)
        result.append(expression[0])
        _repr(expression[2], result)
        result.append(")")
    else:
        result.append(expression if isinstance(expression, str) else str(expression))
    




if __name__ == "__main__":
    print(f"{'EXERCISE 1':=^30}")

    pattern = ["a", "b"]
    chain = ["a", "b", "c", "e", "b", "a", "b", "f"]

    print(count_pattern(pattern, chain))

    pattern = ["a", "b", "a"]
    chain = ["g", "a", "b", "a", "b", "a", "b", "a"]

    print(count_pattern(pattern, chain))

    print(f"{'EXERCISE 2':=^30}")

    expression = ('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))
    repr_expresion(expression)

    print(depth(expression))

