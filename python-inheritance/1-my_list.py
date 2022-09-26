#!/usr/bin/python3
"""Module"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        m_list = self.copy()
        m_list.sort()
        print(m_list)
        return (m_list)
