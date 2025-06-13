from itertools import zip_longest

def transpose(text):
    # After splitting the text by '\n', we can guarantee that '\n' is not present in any of the column strings.
    columns = text.split('\n')
    # Therefore, we can use fillvalue='\n' to avoid removing special characters
    # (e.g., in TransposeTest.test_special_characters).
    rows = ("".join(row).rstrip('\n').replace('\n', ' ') \
               for row in zip_longest(*columns, fillvalue='\n'))
    return "\n".join(rows)

