# Simple 'Countdown' games solver

#### Requirements
<a href="https://pypi.org/project/pyenchant/">pyenchant</a> - `pip install pyenchant`

#### Numbers countdown game
`NumberGame` class has two main methods, first `get_all()` will execute until all possible combinations are checked and return all solutions. `get_any()` method will return the first found solution, which in some cases decrease runtime to less than one second.
```python
>>>from countdown_solvers import NumberGame
>>>game = NumberGame([100, 25, 3, 1, 5, 8], 666)
>>>solution = game.get_any()
>>>print(solution)
 ... ('(100+25+8)*5+1', 666)
```
##### Async class
 \*\*__You should not use this class unless you know what you are doing.__\*\* Package also have async adaptation of `NumberGame` class. I added this implementation to use as a module to telegram userbot, because it will allow my bot to keep control and react to commands while executing this cpu heavy task.
```python
>>>from countdown_solvers import AsyncNumberGame
>>>game = AsyncNumberGame([75, 50, 9, 1, 4, 2], 777)
>>># Assuming async context
>>>solutions = await game.get_all()
>>>print(*solutions, sep="\n")
 ... ('75*9+2*(50+1)', 777)
 ... ('75*9+2*(1+50)', 777)
 ... ('(50+1)*2+75*9', 777)
 ... ('(50+1)*2+9*75', 777)
 ...  ... 
 ... ('(2+50+1)*9+75*4', 777)
 ... ('(2+50+1)*9+4*75', 777)
 ... ('(2+1+50)*9+75*4', 777)
 ... ('(2+1+50)*9+4*75', 777)
```

#### Words countdown game
`TextGame` class finds all possible combinations of symbols that are legit words. Although, it just ignores combinations that are less then 4 symbols, because `enchant` lib that is used for checking doesn't work properly in such case. ¯\\\_(ツ)\_/¯
<br/>
You can still use `bad_search` to find all words, also you can reverse search with `from_smaller=True`.
```python
>>>from countdown_solvers import TextGame
>>>game = TextGame(["a", "b", "c", "d", "e", "f", "g", "h"])
>>>solutions = game.get_all(from_smaller=True, bad_search=True)
>>>print(*solutions, sep="\n")
 ... chafed
 ... beach
 ... badge
 ... decaf
 ... faced
 ... cadge
 ... caged
 ...  ... 
 ... deaf
 ... fade
 ... aged
 ... egad
 ... head
 ... chef
>>>best_solution = game.get_best()
>>>print(best_solution)
 ... chafed
```

### Mentions
__Thanks to @painor (<a href="https://github.com/painor">Github:painor</a>) and @Zacci (<a href="https://github.com/commitZac">Github:commitZac</a>) from telethonofftopic telegram chat for ~~writing code for me and fixing mine~~ helping much to implement this module!__