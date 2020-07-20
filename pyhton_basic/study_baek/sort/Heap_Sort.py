
def build_heap(arr, heap_size):
    # 힙정렬 시, 두단계로 나눠서 시작 
    # 1 단계 
    # 힙트리 생성
    
    # 2 단계
    # 부모 노드와 잎새노드 swap 후 트리 재정렬
    # swap 후 heapify시 heap size를 줄여 준다. (줄이고 남은 Heap은 부모 노드를 저장하기 위한 공간)

    # step 1
    for i in range(heap_size//2 - 1, -1, -1):
        heapify(arr, i, heap_size)

    print("After 1 step :: " , arr)
    # # step 2
    # for i in range(heap_size-1, 0, -1):
    #     arr[0], arr[i] = arr[i], arr[0]
    #     heapify(arr, 0, i)

    # print("After 2 step :: " , arr)
    return arr

def heapify(arr, index, size):
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2

    if left < size and arr[largest] < arr[left]:
        largest = left
    
    if right < size and arr[largest] < arr[right]:
        largest = right
    
    if index != largest:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, size)


if __name__ == "__main__":
    heap_size = int(input())
    arr = list(map(int, input().split()))
    print("initailize arr :: " , arr)
    arr = build_heap(arr, heap_size)

    # 6 5 3 2 4 1