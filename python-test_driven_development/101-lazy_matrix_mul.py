#!/usr/bin/python3
""" Define function. """
import numpy as NumPy


def lazy_matrix_mul(m_a, m_b):
    """
        Return the multiplication of two matrices.
        Args:
            m_a (list of lists of ints/floats): first matrix.
            m_b (list of lists of ints/floats): second matrix.
    """

    return (NumPy.matmul(m_a, m_b))
