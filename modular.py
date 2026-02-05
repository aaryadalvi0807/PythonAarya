def create_set():
    return set([10, 20, 30, 40, 50])

def remove_element(num_set, element):
    num_set.discard(element)
    return num_set

def main():
    Num = create_set()
    Num = remove_element(Num, 50)
    print(Num)

main()
