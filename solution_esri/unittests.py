import solution
import unittest


class TestSolution(unittest.TestCase):

    def test_next_number_generator_even(self):
        expected = 4
        result = next(solution.next_number_generator(8))
        self.assertEqual(expected, result)

    def test_next_number_generator_odd(self):
        expected = 10
        result = next(solution.next_number_generator(3))
        self.assertEqual(expected, result)

    def test_calculate_sequence_len(self):
        expected = 7
        result = solution.calculate_seq_len(3)
        self.assertEqual(expected, result)

    def test_get_the_nth_number(self):
        expected = 8
        result = solution.get_the_nth_number(3, 4)
        self.assertEqual(expected, result)

    def test_sequence_error_in_calculate_sequence_len(self):
        with self.assertRaises(solution.SequenceError):
            solution.calculate_seq_len(0)

    def test_sequence_error_in_get_the_nth_number(self):
        with self.assertRaises(solution.SequenceError):
            solution.calculate_seq_len(0)


