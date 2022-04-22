#!/usr/bin/python3
"""Preparation for technical job interview"""


class Box:
    """Defines a class for a box in order to know if the box
    is opened or not"""
    def __init__(self, keys, opened):
        self.keys = keys
        self.opened = opened


def setOpened(listOfBoxes, currentBox):
    """Open the boxes of the list depending of the given keys"""
    for key in currentBox.keys:
        if key >= len(listOfBoxes):
            continue
        if listOfBoxes[key].opened is False:
            listOfBoxes[key].opened = True
            listOfBoxes = setOpened(listOfBoxes, listOfBoxes[key])
    return listOfBoxes


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    for i in range(len(boxes)):
        if i == 0:
            boxes[i] = Box(boxes[i], True)
        else:
            boxes[i] = Box(boxes[i], False)
    boxes = setOpened(boxes, boxes[0])
    for box in boxes:
        if box.opened is False:
            return False
    return True
