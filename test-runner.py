import unittest
import importlib
import json
import numpy as np
import pandas as pd

class TestFinal(unittest.TestCase):
    def test_01_ListMethods(self):
        list_methods = asgmt.ListMethods([3, 2, 7, 5, 11])
        self.assertEqual(list_methods.sort_asc(), [2, 3, 5, 7, 11])
        self.assertEqual(list_methods.sort_desc(), [11, 7, 5, 3, 2])
        self.assertEqual(list_methods.reverse(), [11, 5, 7, 2, 3])
        list_methods = asgmt.ListMethods([1, 2, 3])
        self.assertEqual(list_methods.sort_asc(), [1, 2, 3])
        self.assertEqual(list_methods.sort_desc(), [3, 2, 1])
        self.assertEqual(list_methods.reverse(), [3, 2, 1])
    def test_02_SequenceGenerator(self):
        sequence_generator = asgmt.SequenceGenerator(5)
        self.assertEqual(sequence_generator.get_evens(), [0, 2, 4, 6, 8])
        self.assertEqual(sequence_generator.get_odds(), [1, 3, 5, 7, 9])
        sequence_generator = asgmt.SequenceGenerator(7)
        self.assertEqual(sequence_generator.get_evens(), [0, 2, 4, 6, 8, 10, 12])
        self.assertEqual(sequence_generator.get_odds(), [1, 3, 5, 7, 9, 11, 13])
        sequence_generator = asgmt.SequenceGenerator(3)
        self.assertEqual(sequence_generator.get_evens(), [0, 2, 4])
        self.assertEqual(sequence_generator.get_odds(), [1, 3, 5])
    def test_03_AdvancedSequenceGenerator(self):
        sequence_generator = asgmt.AdvancedSequenceGenerator(5)
        self.assertEqual(sequence_generator.get_evens(), [0, 2, 4, 6, 8])
        self.assertEqual(sequence_generator.get_odds(), [1, 3, 5, 7, 9])
        self.assertEqual(sequence_generator.get_primes(), [2, 3, 5, 7, 11])
        self.assertEqual(sequence_generator.get_fibonacci(), [0, 1, 1, 2, 3])
        sequence_generator = asgmt.AdvancedSequenceGenerator(7)
        self.assertEqual(sequence_generator.get_evens(), [0, 2, 4, 6, 8, 10, 12])
        self.assertEqual(sequence_generator.get_odds(), [1, 3, 5, 7, 9, 11, 13])
        self.assertEqual(sequence_generator.get_primes(), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(sequence_generator.get_fibonacci(), [0, 1, 1, 2, 3, 5, 8])
        sequence_generator = asgmt.AdvancedSequenceGenerator(3)
        self.assertEqual(sequence_generator.get_evens(), [0, 2, 4])
        self.assertEqual(sequence_generator.get_odds(), [1, 3, 5])
        self.assertEqual(sequence_generator.get_primes(), [2, 3, 5])
        self.assertEqual(sequence_generator.get_fibonacci(), [0, 1, 1])
    def test_04_KeyValueMethods(self):
        key_value_methods = asgmt.KeyValueMethods(twn="Taiwan")
        self.assertEqual(key_value_methods.reverse(), {'Taiwan': 'twn'})
        self.assertEqual(key_value_methods.to_upper(), {'TWN': 'TAIWAN'})
        self.assertEqual(key_value_methods.to_lower(), {'twn': 'taiwan'})
        key_value_methods = asgmt.KeyValueMethods(twn="Taiwan", jpn="Japan")
        self.assertEqual(key_value_methods.reverse(), {'Taiwan': 'twn', 'Japan': 'jpn'})
        self.assertEqual(key_value_methods.to_upper(), {'TWN': 'TAIWAN', 'JPN': 'JAPAN'})
        self.assertEqual(key_value_methods.to_lower(), {'twn': 'taiwan', 'jpn': 'japan'})
    def test_05_Rot13(self):
        rot13 = asgmt.Rot13()
        self.assertEqual(rot13.rotate_character("A"), 'N')
        self.assertEqual(rot13.rotate_character("B"), 'O')
        self.assertEqual(rot13.rotate_character("L"), 'Y')
        self.assertEqual(rot13.rotate_character("M"), 'Z')
        self.assertEqual(rot13.rotate_character("a"), 'n')
        self.assertEqual(rot13.rotate_character("b"), 'o')
        self.assertEqual(rot13.rotate_character("l"), 'y')
        self.assertEqual(rot13.rotate_character("m"), 'z')
        self.assertEqual(rot13.rotate_sentence("Abj vf orggre guna arire."),
                         "Now is better than never.")
        self.assertEqual(rot13.rotate_sentence("Now is better than never."),
                         "Abj vf orggre guna arire.")
        self.assertEqual(rot13.rotate_sentence("Rkcyvpvg vf orggre guna vzcyvpvg."),
                         "Explicit is better than implicit.")
        self.assertEqual(rot13.rotate_sentence("Explicit is better than implicit."),
                         "Rkcyvpvg vf orggre guna vzcyvpvg.")
    def test_06_import_mlb_teams_json(self):
        mlb_teams_json = asgmt.import_mlb_teams_json()
        self.assertIsInstance(mlb_teams_json, list)
        self.assertEqual(len(mlb_teams_json), 30)
    def test_07_find_location_with_name(self):
        self.assertEqual(asgmt.find_location_with_name("New York Yankees"), 'Bronx')
        self.assertEqual(asgmt.find_location_with_name("New York Mets"), 'Flushing')
        self.assertEqual(asgmt.find_location_with_name("Los Angeles Dodgers"), 'Los Angeles')
        self.assertEqual(asgmt.find_location_with_name("Kansas City Royals"), 'Kansas City')
    def test_08_import_csv_files(self):
        movies, movies_directors, directors = asgmt.import_csv_files()
        self.assertEqual(movies.shape, (250, 6))
        self.assertEqual(movies_directors.shape, (284, 4))
        self.assertEqual(directors.shape, (179, 3))
    def test_09_merge_dataframes(self):
        merged_dataframe = asgmt.merge_dataframes()
        self.assertEqual(merged_dataframe.shape, (284, 3))
        self.assertIn("The Shawshank Redemption", merged_dataframe["title"].values)
        self.assertIn("The Green Mile", merged_dataframe["title"].values)
        self.assertIn("Frank Darabont", merged_dataframe["director"].values)
        self.assertIn("Francis Ford Coppola", merged_dataframe["director"].values)
    def test_10_find_movies_with_multiple_directors(self):
        movies_with_multiple_directors = asgmt.find_movies_with_multiple_directors()
        self.assertEqual(movies_with_multiple_directors.shape, (60, 3))
        self.assertIn("Avengers: Endgame", movies_with_multiple_directors["title"].values)
        self.assertIn("Avengers: Infinity War", movies_with_multiple_directors["title"].values)
        self.assertIn("Anthony Russo", movies_with_multiple_directors["director"].values)
        self.assertIn("Joe Russo", movies_with_multiple_directors["director"].values)

asgmt = importlib.import_module("final")
suite = unittest.TestLoader().loadTestsFromTestCase(TestFinal)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))