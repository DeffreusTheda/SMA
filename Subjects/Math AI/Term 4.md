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

## Exercise 3I

1. The points A, B and C have coordinates (1, 4), (2, 5) and (−1, 6) respectively.
   1. Find the vectors
      1. OA<br>
         [1 4]
      2. AB<br>
         AB = AO + OB<br>
         AB = [-1 -4] + [2 5]<br>
         AB = [1 1]
      3. AC<br>
         AC = AO + OC<br>
         AB = [-1 -4] + [-1 6]<br>
         AB = [-2 2]
      4. CA<br>
         CA = CO + OA<br>
         CA = [1 -6] + [1 4]<br>
         CA = [2 -2]
   2. The point D is such that CD is equal to [4 1]
      1. Write down an equation that gives BD in terms of BA, AC and CD<br>
         BD = BA + (AC + CD)
      2. Hence write down an equation that gives BD in terms of AB , AC and CD<br>
         BD = -AB + (AC + CD)
      3. Hence find BD<br>
         BD = -AB + (AC + CD)<br>
         BD = [-1 -1] + ([-2 2] + [4 1])<br>
         BD = [1 2]
      4. Find the coordinates of D<br>
         OD = OB + BD<br>
         OD = [2 5] + [1 2]<br>
         OD = [3 7]
         D = (3, 7)
2. Answer!
   1. AB = [1 4] and BC = [-1 2], find:
      1. AC; and<br>
         AC = AB + BC<br>
         AC = [1 4] + [-1 2]<br>
         AC = [0 6]
      2. CA<br>
         CA = -AC<br>
         CA = [0 -6]
   2. AB = [2 4] and BC = [1 3], and AD = [2 3] find DC<br>
      DC = -AD + (AB + BC)<br>
      DC = [-2 -3] + ([2 4] + [1 3])<br>
      DC = [1 4]
3. 3 The points A, B, C and D have coordinates (1,0), (2,3), (7,5) and (6,2) respectively.
   1. Find the vectors AB and DC<br>
      AB = B - A<br>
      AB = (2, 3) - (1, 0)<br>
      AB = [1 3]<br>
      DC = C - D<br>
      DC = (7, 5) - (6, 2)<br>
      DC = [1 3]
   2. State which type of quadrilateral is formed by ABCD. Justify your answer.
      
   3. State two other vectors which must be equal.
4. An aircraft flies from an airport at A to one at B and then on to C. The routes taken can be given by the vectors AB = [75 90] and BC = [-35 -100] km.
   1. Find the vector AC<br>
      AC = AB + BC<br>
      AC = [75 90] + [-35 -100]<br>
      AC = [40 -10]
   2. The aircraft then flies directly back to A. Write down the vector that describes this flight.<br>
      CA
   3. Calculate the direct distance from C to A.<br>
      CA = -AC<br>
      CA = [-40 10]
      $\sqrt{-40^2 + 10^2}$
      $41.2 km$
5. A surveyor is putting flags out in a large field. His movements between the flags can be described by the vectors (5i + j), (−2i + 4j), (4i + 2j), (6i + 4j).
   1. Find his displacement from his starting position when he puts out the last flag.<br>
      $(5i + j) + (−2i + 4j) + (4i + 2j) + (6i + 4j)$<br>
      $13i + 11j$
   2. Write down the displacement vector that will take him back to his starting position<br>
      $-13i - 11j$

## Investigation 8

1. A boy walks 5km on a bearing of 045˚ and then 8km on a bearing of 120˚
   1. ******
   2. Use the cosine and sine rules to find his distance and bearing from his starting point at the end of the walk.
      $u = \sqrt{5^2 + 8^2 - 2 \cdot 5 \cdot 8 cos 105 \degree}$
      $u = 10.5 km$
       $\frac{sin \theta}{8} = \frac{sin 105 \degree}{10.5 km}$
      $\theta = 47.4 \degree$
   3. Answer!
      1. Write the displacements 5km on a bearing of 045˚ and 8km on a bearing of 120˚ as column vectors where the first component indicates displacement east and the second displacement north.
         5 km -> [3.536 -3.536]
         8 km -> [4.330 -2.5]
      2. Use your answer to part c i to find how far east and how far north from his starting point the boy is at the end of his walk.
         east $= 3.536 + 4.330 = 7.866$
         north $= -3.536 - 2.5 = -6.036$
      3. Hence give his resultant (final) displacement as a column vector.
         [7.866 -6.036]
      4. Use your answer to part c iii to find his distance and bearing from his starting point at the end of the walk.
         distance $= \sqrt{7.866^2 + (-6.036)^2} = 9.92$
				 bearing $= $ <!-- TODO: Finish this -->

## Exercise 3J

1. For the resultant of each of the vector sums: [1 3] + [-1 2] + [4 -1], $(5i + 2j) + (-6i - 4j)$, 2 [3 2] - 3 [-4 -1], $5 (i + 2j) + 3 (i - 3j)$; find the
   1. magnitude
      1. [4 4]
         $\sqrt{4^2 + 4^2}$
         $5.66$
      2. $-i - 2j$
         $\sqrt{(-1)^2 + (-2)^2}$
         $2.24$
      3. [18 7]
         $\sqrt{18^2 + 7^2}$
         $19.3$
      4. $8i + j$
         $\sqrt{8^2 + 1^2}$
         $8.06$
   2. direction (as an angle anti-clockwise from the direction of i)
      1. $315 \degree$
      2. $270 - sin^{-1} (\frac{sin 90 \degree \cdot 1}{\sqrt{2^2 + 1^1}})$
         $270 - 26.6 \degree$
         $243.4 \degree$
      3. $sin^{-1} (\frac{sin 90 \degree \cdot 7}{\sqrt{18^2 + 7^2}})$
         $tan^{-1} (\frac{7}{18})$
         $21.3 \degree$
      4. $sin^{-1} (\frac{sin 90 \degree}{\sqrt{8^2 + 1^2}})$
         $7.1 \degree$
2. The magnitude of a vector [a b] can be written as |a b|.
   1. Verify that |48 20| is equal to 4 |12 5|.
      $|48 20| = |(4 \cdot 12) (5 \cdot 4)|$
      $|48 20| = |48 20|$
   2. By first taking out a factor and without using a GDC, find the magnitude of
      1. [18 24]
         $\sqrt{18^2 + 24^2}$
         $30$
      2. [-30 40]
         $\sqrt{(-30)^2 + 40^2}$
         $50$
      3. [28 -21]
         $\sqrt{28^2 + (-21)^2}$
         $35$
