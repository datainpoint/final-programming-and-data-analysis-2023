# final-programming-and-data-analysis-2023

> Final: Programming and Data Analysis 2023.

Define functions or classes in `final.py` with given names and templates then run `test-runner.py`.

## 01. Define a class `ListMethods()` which instantiates objects with three methods `sort_asc()`, `sort_desc()` and `reverse()`.

```python
class ListMethods:
    """
    >>> list_methods = ListMethods([3, 2, 7, 5, 11])
    >>> list_methods.sort_asc()
    [2, 3, 5, 7, 11]
    >>> list_methods.sort_desc()
    [11, 7, 5, 3, 2]
    >>> list_methods.reverse()
    [11, 5, 7, 2, 3]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a class `SequenceGenerator` which instantiates objects with two methods `get_evens()` and `get_odds()` that return a `list` with the first `n` evens or odds.

```python
class SequenceGenerator:
    """
    >>> sequence_generator = SequenceGenerator(5)
    >>> sequence_generator.get_evens()
    [0, 2, 4, 6, 8]
    >>> sequence_generator.get_odds()
    [1, 3, 5, 7, 9]
    >>> sequence_generator = SequenceGenerator(7)
    >>> sequence_generator.get_evens()
    [0, 2, 4, 6, 8, 10, 12]
    >>> sequence_generator.get_odds()
    [1, 3, 5, 7, 9, 11, 13]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a class `AdvancedSequenceGenerator` which instantiates objects with four methods `get_evens()`, `get_odds()`, `get_primes()`, and `get_fibonacci()` that return a `list` with the first `n` evens, odds, primes or integers of a Fibonacci sequence (while `n >= 2`).

- Source: <https://en.wikipedia.org/wiki/Prime_number>
- Source: <https://en.wikipedia.org/wiki/Fibonacci_sequence>

```python
class AdvancedSequenceGenerator:
    """
    >>> advanced_sequence_generator = AdvancedSequenceGenerator(5)
    >>> advanced_sequence_generator.get_evens()
    [0, 2, 4, 6, 8]
    >>> advanced_sequence_generator.get_odds()
    [1, 3, 5, 7, 9]
    >>> advanced_sequence_generator.get_primes()
    [2, 3, 5, 7, 11]
    >>> advanced_sequence_generator.get_fibonacci()
    [0, 1, 1, 2, 3]
    >>> advanced_sequence_generator = AdvancedSequenceGenerator(7)
    >>> advanced_sequence_generator.get_evens()
    [0, 2, 4, 6, 8, 10, 12]
    >>> advanced_sequence_generator.get_odds()
    [1, 3, 5, 7, 9, 11, 13]
    >>> advanced_sequence_generator.get_primes()
    [2, 3, 5, 7, 11, 13, 17]
    >>> advanced_sequence_generator.get_fibonacci()
    [0, 1, 1, 2, 3, 5, 8]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a class `KeyValueMethods` which instantiates objects takes `**kwargs` with 3 methods `reverse()`, `to_upper()`, and `to_lower()`.

```python
class KeyValueMethods:
    """
    >>> key_value_methods = KeyValueMethods(twn="Taiwan")
    >>> key_value_methods.reverse()
    {'Taiwan': 'twn'}
    >>> key_value_methods.to_upper()
    {'TWN': 'TAIWAN'}
    >>> key_value_methods.to_lower()
    {'twn': 'taiwan'}
    >>> key_value_methods = KeyValueMethods(twn="Taiwan", jpn="Japan")
    >>> key_value_methods.reverse()
    {'Taiwan': 'twn', 'Japan': 'jpn'}
    >>> key_value_methods.to_upper()
    {'TWN': 'TAIWAN', 'JPN': 'JAPAN'}
    >>> key_value_methods.to_lower()
    {'twn': 'taiwan', 'jpn': 'japan'}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a class `Rot13` which instantiates objects with 2 methods `rotate_character()` and `rotate_sentence()`.

Source: <https://en.wikipedia.org/wiki/ROT13>

```python
class Rot13:
    """
    >>> rot13 = Rot13()
    >>> rot13.rotate_character("A")
    'N'
    >>> rot13.rotate_character("B")
    'O'
    >>> rot13.rotate_character("L")
    'Y'
    >>> rot13.rotate_character("M")
    'Z'
    >>> rot13.rotate_character("a")
    'n'
    >>> rot13.rotate_character("b")
    'o'
    >>> rot13.rotate_character("l")
    'y'
    >>> rot13.rotate_character("m")
    'z'
    >>> rot13.rotate_sentence("Abj vf orggre guna arire.")
    'Now is better than never.'
    >>> rot13.rotate_sentence("Now is better than never.")
    'Abj vf orggre guna arire.'
    >>> rot13.rotate_sentence("Rkcyvpvg vf orggre guna vzcyvpvg.")
    'Explicit is better than implicit.'
    >>> rot13.rotate_sentence("Explicit is better than implicit.")
    'Rkcyvpvg vf orggre guna vzcyvpvg.'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `import_mlb_teams_json()` which imports `mlb_teams.json` in working directory.

```python
def import_mlb_teams_json() -> list:
    """
    >>> mlb_teams_json = import_mlb_teams_json()
    >>> type(mlb_teams_json)
    list
    >>> len(mlb_teams_json)
    30
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `find_location_with_name()` which returns a MLB team's location given team's name based on `mlb_teams.json` in working directory.

```python
def find_location_with_name(name: str) -> str:
    """
    >>> find_location_with_name("New York Yankees")
    'Bronx'
    >>> find_location_with_name("New York Mets")
    'Flushing'
    >>> find_location_with_name("Los Angeles Dodgers")
    'Los Angeles'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `import_csv_files()` which imports 3 CSV files `movies.csv`, `movies_directors.csv`, and `directors.csv` in working directory.

```python
def import_csv_files() -> tuple:
    """
    >>> movies, movies_directors, directors = import_csv_files()
    >>> type(movies)
    pandas.core.frame.DataFrame
    >>> type(movies_directors)
    pandas.core.frame.DataFrame
    >>> type(directors)
    pandas.core.frame.DataFrame
    >>> movies.shape
    (250, 6)
    >>> movies_directors.shape
    (284, 4)
    >>> directors.shape
    (179, 3)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `merge_dataframes()` which merges(or joins) 3 dataframes based on the following join-keys `movies.id`, `movies_directors.movie_id`, `movies_directors.director_id`, and `directors.id`. Select specified columns showing movie's title, director's name and their directing order given `movies.csv`, `movies_directors.csv`, and `directors.csv` in working directory.

```
                        title              director  ord
0    The Shawshank Redemption        Frank Darabont    1
1              The Green Mile        Frank Darabont    1
2               The Godfather  Francis Ford Coppola    1
3       The Godfather Part II  Francis Ford Coppola    1
4              Apocalypse Now  Francis Ford Coppola    1
..                        ...                   ...  ...
279             The 400 Blows     François Truffaut    1
280                  The Help           Tate Taylor    1
281                   Aladdin          Ron Clements    1
282                   Aladdin           John Musker    2
283                  Drishyam       Nishikant Kamat    1

[284 rows x 3 columns]
```

```python
def merge_dataframes() -> pd.core.frame.DataFrame:
    """
    >>> merged_dataframe = merge_dataframes()
    >>> type(merged_dataframe)
    pandas.core.frame.DataFrame
    >>> merged_dataframe.shape
    (284, 3)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `find_movies_with_multiple_directors()` which finds out movies directed by multiple directors. Select specified columns showing movie's title, director's name and their directing order given `movies.csv`, `movies_directors.csv`, and `directors.csv` in working directory.

```
                                  title               director  ord
0                               Aladdin           Ron Clements    1
1                               Aladdin            John Musker    2
2                     Avengers: Endgame          Anthony Russo    1
3                     Avengers: Endgame              Joe Russo    2
4                Avengers: Infinity War          Anthony Russo    1
5                Avengers: Infinity War              Joe Russo    2
..                                  ...                    ...  ...
55                     The Wizard of Oz          Norman Taurog    4
56                     The Wizard of Oz         Richard Thorpe    5
57                     The Wizard of Oz             King Vidor    6
58                                   Up            Pete Docter    1
59                                   Up           Bob Peterson    2

[60 rows x 3 columns]
```

```python
def find_movies_with_multiple_directors() -> pd.core.frame.DataFrame:
    """
    >>> movies_with_multiple_directors = find_movies_with_multiple_directors()
    >>> type(movies_with_multiple_directors)
    pandas.core.frame.DataFrame
    >>> movies_with_multiple_directors.shape
    (60, 3)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```