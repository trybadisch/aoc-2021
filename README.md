# Advent of Code 2021 (Python)

[Advent of Code](https://adventofcode.com/) provides programming puzzle challenges through December. The daily solution attempts along with the provided inputs will be uploaded in each day folder.

Day | Name | Solution
:---:|:---:|:---:
[01](#day-1-sonar-sweep) | Sonar Sweep | [File](advent1/advent1.py)
[02](#day-2-dive) | Dive! | [File](advent2/advent2.py)
[03](#day-3-binary-diagnostic) | Binary Diagnostic | [File](advent3/advent3.py)
[04](#day-4-giant-squid-bingo) | Giant Squid | [Bingo](advent4/advent4.py)
[05](#day-5-hydrotermal-venture) | Hydrotermal Venture | [File](advent5/advent5.py)
[06](#day-6-lanternfish) | Lanternfish | [File](advent6/advent6.py)
[07](#day-7-the-treachery-of-whales-crabs) | The Treachery of Whales | [Crabs](advent7/advent7.py)
[08](#day-8-seven-segment-search) | Seven Segment Search | [File](advent8/advent8.py)
[09](#day-9-smoke-basin) | Smoke Basin | [File](advent9/advent9.py)
[10](#day-10-syntax-scoring) | Syntax Scoring | [File](advent10/advent10.py)

## Day 1: [Sonar Sweep](advent1/advent1.py)

![Day 1](img/carbon1.png)

## Day 2: [Dive!](advent2/advent2.py)

![Day 2](img/carbon2.png)

## Day 3: [Binary Diagnostic](advent3/advent3.py)

~~Requires refactoring to use a bitmask filter. Currently requires to manually check if last "filtered" numbers in CO2 exist in input.~~

## Day 4: [Giant Squid](advent4/advent4.py) (Bingo)

Result is being thrown as an exit code in an exception block due to reusing code from Part 1 without refactoring (recursively plays games until there are no more boards left).
If it works it works.

![Day 4](img/day4out.png)

## Day 5: [Hydrotermal Venture](advent5/advent5.py)

The pillow Python module is required to create these sweet heatmaps for the vents. Install with `pip install pillow`.

![Day 5](img/day5out.png)

## Day 6: [Lanternfish](advent6/advent6.py)

The change of state in each lanternfish cycle share some similarities to a primitive [LFSR](https://en.wikipedia.org/wiki/Linear-feedback_shift_register). They can be simplified as:

```
age[0] = age[1]
age[1] = age[2]
age[2] = age[3]
age[3] = age[4]
age[4] = age[5]
age[5] = age[6]
age[6] = age[7] + age[0]
age[7] = age[8]
age[8] = age[0]
```

![Day 6](img/day6out.png)

## Day 7: [The Treachery of Whales](advent7/advent7.py) (Crabs)

Bruteforce solution also viable for Part 2 (check every possible position):

```python
fuel = pos = 0
for i in range(max(crabs)):
    tmp = 0
    for j in crabs:
        dif = abs(i - j)
        tmp += dif * (dif+1) // 2
    if tmp < fuel or fuel == 0:
        fuel = tmp
        pos = i
print("[+] Position =", pos, "/ Fuel =", fuel)
```
![Day 7](img/carbon7.png)

## Day 8: [Seven Segment Search](advent8/advent8.py)

Deduction rules via character repetitions in display and known character lengths in (1,4,7,8):

Repetitions | In known | Rule
------------|----------|-------------------------
a = 8       | 7, 8     | only in 7,8 (not in 1,4)
b = 6       | 4, 8     | 6 times
c = 8       | 1,4,7,8  | 8 times AND not A
d = 7       | 4, 8     | 7 times AND not G
e = 4       | 8        | 4 times
f = 9       | 1,4,7,8  | 9 times
g = 7       | 8        | 7 times AND only in 8 (not in 1,4,7)

## Day 9: [Smoke Basin](advent9/advent9.py)

## Day 10: [Syntax Scoring](advent10/advent10.py)

![Day 10](img/carbon10.png)
