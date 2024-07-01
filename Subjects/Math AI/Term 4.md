# Term 4

## Vectors

It's like a segment, a line with ending on two point, except it has a direction.
The common symbols for a vector are lowercase: u, v, and w.

We write it with matrix, for example,
A vector from point A (1, 1) to point B (4,6) will be wrote down as [3 5], with the values representing the differences.
It can also be written as $3i + 5j$, with i as X, and j as Y.

Note that direction matters; if it's point B to point A, it'll be [-3 -5].
As you might notice, This means that $AB == -BA$.

- $u + v$
- $[3 5] + [-3 -5]$ <!-- TODO: make the proof -->
- $[(3 - 3) (5 - 5)]$
- $[0 0]$
- $0$

### Exercise 3H

1. <img src='img/Ex3H-1' height=100><br>
   a = [0 -3]  -> $-3j$<br>
   b = [-2 -2] -> $-2i - 2j$<br>
   c = [2 1]   -> $2i + j$<br>
   d = [1 -3]  -> $i - 3j$<br>
   e = [2 0]   -> $2i$<br>

2. Find:
   1. [2 1] + [-5 3]<br>
      [(2 - 5) (1 + 3)]<br>
      [-3 4]
   2. $(3i - j) + (4i + 5j)$<br>
      $7i + 4j$
   3. [-2 5] + [-4 -3]<br>
      [-6 2]
   4. $(i - 2j) + 4i$<br>
      $5i - 2j$<br>

3. Find
   1. [2 3] + [2 3]<br>
      [4 + 6]
   2. [2 3] + [2 3] + [2 3]<br>
      [6 9]
   3. Explain how you multiply a vector by a scalar.<br>
      Just multiply each all elements in a vector by the scalar.
   4. $i$ and $j$ can also be written as [1 0] and [0 1], hence verify $3i + 4j =$ [3 4]<br>
      [3 0] + [0 4]<br>
      [3 4]<br>

4. Let AB = [1 2] as shown.<br>
   <img src='img/Ex3H-4' height=100><br>
   1. Write the following vectors in component form and in terms of the vector AB:
      1. CD<br>
         $i + 2j$<br>
         CD $= AB$
      2. FE<br>
         $-i - 2j$<br>
         FE $= -AB$
      3. GH<br>
         $2i + 4j$<br>
         GH $= 2 \cdot AB$
      4. IJ<br>
         $\frac{i}{2} - j$<br>
         IJ $= \frac{AB}{-2}$<br>

5. State which of the following vectors are parallel to $5i + 2j$.
   1. $-5 - 2j$<br>
      Parallel
   2. $25i - 10j$<br>
      Not parallel
   3. $-i - 0.4j$<br>
      Parallel
   4. $[20 50]$<br>
      Not parallel
   5. $[4 6] + [6 -2]$<br>
      Parallel
   6. $2 \cdot$ [-10 4]<br>
      Not parallel
   7. $2 \cdot$ [3 3] $- 3 \cdot$ [-3 0]<br>
      Parallel<br>

 6. Solve:
    1. Find $p$ and $q$ if
       1. [4p 6] + [6 - 2q] = [-2p 2]<br>
          $4p + 6 = -2p$<br>
          $6p = -6$<br>
          $p = -1$<br>
          $-2q + 6 = 2$<br>
          $-2q = -4$<br>
          $q = 2$
       2. [-3p -2q] + [2q p] = [7 1]<br>
			    $-3p + 2q = 7$<br>
					$p + -2q = 1$<br>
					$-2p = 8$<br>
					$p = -4$<br>
					$12 + 2q = 7$<br>
					$q = -2.5$
    2. 1. Find $p$ if [(p + 1) (2p)] is parallel to [4 1]<br>
          [(p + 1) 2p] $= k \cdot$ [4k k]<br>
          $p + 1 = 4k$<br>
          $2p = k$<br>
          $-7p + 1 = 0$<br>
          $p = \frac{1}{7}$
  	   2. Find $q$ if [(2q - 3) (q + 6)] is parallel to [-3 1]<br>
			    $2q - 3 = -3k$<br>
					$q + 6 = k$<br>
					$5q + 15 = 0$<br>
					$q = -3$<br>
