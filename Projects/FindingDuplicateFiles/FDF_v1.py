import sys

def find_duplicates(filenames) -> list:
    matches = []

    for i_left in range(len(filenames)):      
        left = filenames[i_left]                
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_bytes(left, right):
                matches.append((left, right))
    return matches


def same_bytes(left_name, right_name) -> bool:
    left_bytes = open(left_name, 'br').read()
    right_bytes = open(right_name, 'br').read()

    return left_bytes == right_bytes


if __name__ == '__main__':
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)





