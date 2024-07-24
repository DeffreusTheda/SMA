# Topic 4 - Programming

## Pseudocode

`NAME` is a variable name,
and a variable is something that hold a value.
You can pick whatever name you want,
but it' recommended that the name represent the purpose of that variable.

`EXPRESSION` is anything that can be evaluated,
resulting in one value.
For example, the expression `8 div 2` is evaluated to be `4`,
and `1 xor 0` is evaluated to be `1`.
Expression can include variable:

```Pseudocode
FIRSTNAME = "DEFFREUS"
LASTNAME = "THEDA"
FULLNAME = FIRSTNAME + " " + LASTNAME
```



```Pseudocode
// Assignment
NAME = EXPRESSION

// Input
NAME = input(EXPRESSION) // EXPRESSION here is the prompt for the input

// Output
output EXPRESSION

// If Else
if EXPRESSION then
  // your code
end if

// For Loop
loop NAME for EXPRESSION to EXPRESSION
  // your code
end loop

// While Loop
loop while EXPRESSION
  // your code
end loop

// Boolean operators
output 0 and 0 // 0
output 1 and 0 // 0
output 1 and 1 // 1
output 0 or 0 // 0
output 1 or 0 // 1
output 1 or 1 // 1
output 0 xor 0 // 0
output 1 xor 0 // 1
output 1 xor 1 // 0
```

### Practice Question

The test scores of 100 students are held in an array SCORES.

```Pseudocode
// output minimum score
loop I for 0 to 99
  if SCORES[0] > SCORES[I] then // '>' to '<' for maximum score instead
    SCORES[0] = SCORES[I]
  end if
end loop
output SCORES[0]


// output scores above 50
loop I for 0 to 99
  if SCORES[I] > 50 then
    output SCORES[I]
  end if
end loop


// output average score
SUM = 0
loop I for 0 to 99
  SUM = SUM + SCORES[I]
end loop


// output scores between 50 and 80 (boolean operator)
loop I for 0 to 99
  if SCORES[I] > 50 and SCORES[I] < 80 then
    output SCORES[I]
  end if
end loop


// output scores between 50 and 80 (nested ifs)
loop I for 0 to 99
  if SCORES[I] > 50 then
    if SCORES[I] < 80 then
      output SCORES[I]
    end if
  end if
end loop
```
