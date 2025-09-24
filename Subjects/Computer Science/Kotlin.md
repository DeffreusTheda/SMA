---
tags: []
---
# String
###### Inserting a character at specific index in a string:
(`StringBuilder.insert()`):
 ```kotlin
 val sb = StringBuilder(str)
 sb.insert(index, char)
 ```
Examples:
 ```kotlin
import java.lang.StringBuilder

fun main() {
    val str = "hello world"
    val index = 7
    val char = "p"

    val sb = StringBuilder(str)
    sb.insert(index, char)
    val resultingString = sb.toString()
    println(resultingString)
}
```
output:
 ```
 hello wporld
 ```
###### Get the character at a specific index in a string:
(`String.get()`):
```kotlin
str.get(index)
```
Examples:
```kotlin
fun main() {
    val str = "Hello, World!"
    val index = 7
    val character = str.get(index)
    println("Character at index $index: $character")
}
```
Output:
```
Character at index 7: W
```