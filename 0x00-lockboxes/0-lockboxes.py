#!/usr/bin/python3
''' comment '''


def canUnlockAll(boxes):
    """ This method checks if all boxes in a list can be unlocked """
    keyset = [0]
    for key in keyset:
        for content in boxes[key]:
            if content not in keyset and content < len(boxes):
                keyset.append(content)

    return len(keyset) == len(boxes)
