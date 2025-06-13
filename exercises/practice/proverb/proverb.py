def proverb(*args, **kwargs):
    result = []
    if not args:
        return result
    for i, j in zip(args, args[1:]):
        if i != j:
            result.append(f"For want of a {i} the {j} was lost.")
    else:
        last_phrase = [word for word in [kwargs.get('qualifier'), args[0]] if word]
        result.append(f"And all for the want of a {' '.join(last_phrase)}.")

    return result


