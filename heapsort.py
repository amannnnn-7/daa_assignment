#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  31 12:28:05 2024

@author: angad
"""

def heapsort(characters):
    """
    Sorting a list of characters in lexicographic order using the heapsort algorithm.

    :parameter characters: List of characters to be sorted.
    """
    def heapify(length,rootIndex):
        """
        :parameter length: The length of the current heap.
        :parameter rootIndex: The index of the root of the current subtree.
        """

        largest=rootIndex

        leftChild = 2*rootIndex+1
        rightChild = 2*rootIndex+2

        # check for left child exists & is > than  current largest element
        if leftChild<length and characters[leftChild]>characters[largest]:
            largest = leftChild
        # check for right child exists & is > than  current largest element
        if rightChild<length and characters[rightChild]>characters[largest]:
            largest = rightChild
        # check for largest element is not the root
        if largest!=rootIndex:
            characters[rootIndex],characters[largest] = characters[largest],characters[rootIndex]
            heapify(length,largest)


    # building initial max heap
    for i in range(len(characters)//2-1, -1, -1):
        heapify(len(characters), i)

    # moving largest element to the end and re heapifying
    for i in range(len(characters)-1, 0, -1):

        # swapping max ele with last ele
        characters[0],characters[i]=characters[i],characters[0]
        heapify(i,0)





if __name__=="__main__":

    # reading sequence of alphabets from txt file
    with open('characters.txt', 'r') as file:
        data = file.read().strip().replace(',', '')
        alphabetList = list(data)


    print("Original Sequence Alphabets - ", ''.join(alphabetList))

    # sorting the alphabets
    heapsort(alphabetList)

    print()
    print("Sorted Sequence Alphabets - ", ''.join(alphabetList))
