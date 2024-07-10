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
   2. Use the cosine and sine rules to find his distance and bearing from his starting point at the end of the walk.<br>
      $u = \sqrt{5^2 + 8^2 - 2 \cdot 5 \cdot 8 cos 105 \degree}$<br>
      $u = 10.5 km$<br>
      $\frac{sin \theta}{8} = \frac{sin 105 \degree}{10.5 km}$<br>
      $\theta = 47.4 \degree$
   3. Answer!
      1. Write the displacements 5km on a bearing of 045˚ and 8km on a bearing of 120˚ as column vectors where the first component indicates displacement east and the second displacement north.<br>
         5 km -> [3.536 -3.536]<br>
         8 km -> [4.330 -2.5]
      2. Use your answer to part c i to find how far east and how far north from his starting point the boy is at the end of his walk.<br>
         east $= 3.536 + 4.330 = 7.866$<br>
         north $= -3.536 - 2.5 = -6.036$
      3. Hence give his resultant (final) displacement as a column vector.<br>
         [7.866 -6.036]
      4. Use your answer to part c iii to find his distance and bearing from his starting point at the end of the walk.<br>
         distance $= \sqrt{7.866^2 + (-6.036)^2} = 9.92$<br>
         bearing $= $ <!-- TODO: Finish this -->

## Exercise 3J

1. For the resultant of each of the vector sums: [1 3] + [-1 2] + [4 -1], $(5i + 2j) + (-6i - 4j)$, 2 [3 2] - 3 [-4 -1], $5 (i + 2j) + 3 (i - 3j)$; find the
   1. magnitude
      1. [4 4]<br>
         $\sqrt{4^2 + 4^2}$<br>
         $5.66$
      2. $-i - 2j$<br>
         $\sqrt{(-1)^2 + (-2)^2}$<br>
         $2.24$
      3. [18 7]<br>
         $\sqrt{18^2 + 7^2}$<br>
         $19.3$
      4. $8i + j$<br>
         $\sqrt{8^2 + 1^2}$<br>
         $8.06$
   2. direction (as an angle anti-clockwise from the direction of i)
      1. $315 \degree$
      2. $270 - sin^{-1} (\frac{sin 90 \degree \cdot 1}{\sqrt{2^2 + 1^1}})$<br>
         $270 - 26.6 \degree$<br>
         $243.4 \degree$
      3. $sin^{-1} (\frac{sin 90 \degree \cdot 7}{\sqrt{18^2 + 7^2}})$<br>
         $tan^{-1} (\frac{7}{18})$<br>
         $21.3 \degree$
      4. $sin^{-1} (\frac{sin 90 \degree}{\sqrt{8^2 + 1^2}})$<br>
         $7.1 \degree$
2. The magnitude of a vector [a b] can be written as |a b|.
   1. Verify that |48 20| is equal to 4 |12 5|.<br>
      $|48 20| = |(4 \cdot 12) (5 \cdot 4)|$<br>
      $|48 20| = |48 20|$
   2. By first taking out a factor and without using a GDC, find the magnitude of
      1. [18 24]<br>
         $\sqrt{18^2 + 24^2}$<br>
         $30$
      2. [-30 40]<br>
         $\sqrt{(-30)^2 + 40^2}$<br>
         $50$
      3. [28 -21]<br>
         $\sqrt{28^2 + (-21)^2}$<br>
         $35$
4. A man walking in a large field walks 200m north-east and 175m west.
   1. Write each of the displacements as a column vector.<br>
      [200cos45 200sin45] & [-175 0]
   2. Hence find his final distance from his starting point.<br>
      [(200cos45 - 175) 200sin45]<br>
      [-33.6 141]<br>
      $145$
5. A boat sails 4km on a bearing of 030°, followed 3km south-east, then 4km due east and 2km on a bearing of 080° as shown on the right. Determine its final distance from the starting point. Find also the bearing it would have to travel on to return directly to the starting point.<br>
   $x = 4 sin 30 + 3 cos 45 + 4 + 2 cos 10$<br>
   $x = 10.91936297$<br>
   $y = 4 cos 30 - 3 sin 45 + 0 + 2 sin 80$<br>
   $y = 3.312396778$<br>
   $d = \sqrt{x^2 + y^2}$<br>
   $d = 11.4 km$<br>
   $\theta = 270 - tan^{-1} (\frac{y}{x})$<br>
   $\theta = 253 \degree$

## Exercise 3K

1. Find the magnitude of each of the following vectors without using a calculator.
   1. $8i − 4j + k$<br>
      $\sqrt{8^2 + 4^2 + 1^2}$<br>
      $\sqrt{64 + 16 + 1}$<br>
      $\sqrt{81}$<br>
      $9$
   2. [2 1 2]<br>
      $\sqrt{2^2 + 1^2 + 2^2}$<br>
      $\sqrt{4 + 1 + 4}$<br>
      $\sqrt{9}$<br>
      $3$
   3. 3 [4 -3 0]<br>
      $\sqrt{12^2 + (-9)^2}$<br>
      $\sqrt{144 + 81}$<br>
      $\sqrt{225}$<br>
      $15$
   4. $5 (2i − 3j + 6k)$<br>
      $\sqrt{10^2 + (−15)^2 + 18^2}$<br>
      $\sqrt{100 + 225 + 324}$<br>
      $\sqrt{649}$<br>
      $\sqrt{649}$
2. A small plane travels along the three vectors [3 1 2], [2 4 1] and [7 4 3] in succession. State the vector it will have to travel along to return to its starting point.<br>
   -1 ([3 1 2] + [2 4 1] + [7 4 3])<br>
   -1 [12 9 6]<br>
   [-12 -9 -6]
3. Answer!
   1. If A and B have position vectors a and b and if M is the midpoint of [AB] show that OM $= \frac{1}{2} (a + b)$.
   2. Three points P, Q and R have coordinates (1, 3, 6), (−1, 0 5) and (2, 4, −1). Find the vectors PQ and QR.<br>
      PQ = OQ - OP<br>
      PQ = [-1 0 5] + [-1 -3 -6]<br>
      PQ = [-2 -3 -1]<br>
      QR = OR - OQ<br>
      QR = [2 4 -1] - [-1 0 5]<br>
      QR = [3 4 -6]
   3. Hence or otherwise find the vector PR	<br>
      PR = PQ + QR<br>
      PR = [-2 -3 -1] + [3 4 -6]<br>
      PR = [1 1 -7]
   4. The quadrilateral PQRS is a parallelogram. Find the coordinate of S.<br>
      QR = PS<br>
      [3 4 -6] = OS - OP<br>
      OS = [4 7 0]<br>
      PQ = SR<br>
      [-2 -3 -1] = OR - OS<br>
      OS = [4 7 0]
   5. Find the midpoint of the vector PR<br>
      $\frac{1}{2}$ PR $= \frac{1}{2}$ (p + r)<br>
      $= \frac{1}{2}$ ([1 3 6] + [2 4 -1])<br>
      $= \frac{1}{2}$ [3 7 5]<br>
      $=$ [1.5 3.5 2.5]
   6. Find the midpoint of the vector QS<br>
      QS = OS - OQ<br>
      QS = [4 7 0] - [-1 0 5]<br>
      QS = [5 0 5]<br>
      $\frac{1}{2}$ QS $= \frac{1}{2}$ (q + s)<br>
      $= \frac{1}{2}$ ([-1 0 5] + [4 7 0])<br>
      $= \frac{1}{2}$ [3 7 5]<br>
      $=$ [1.5 3.5 2.5]
   7. What do the answers for parts e and f tell you about the diagonals of a parallelogram?<br>
      They intersect each other at their midpoint

## Scalar and Vector Product

$a \cdot b = a_1 b_1 + a_2 b_2$<br>
$a \cdot b = |a| |b| cos \theta$<br>
$cos \theta = \frac{a \cdot b}{|a| |b|}$

### Practice

Find the angles between vector:

1. (2i + j - 3k) and (-2i + 10j + 2k)<br>
   $cos^{-1} (\frac{-4i + 10j - 6k}{4i + 10j + 6k})$<br>
   $cos^{-1} (\frac{-4i + 10j - 6k}{4i + 10j + 6k})$
   $cos^{-1} (-i + j - k)$

### Exercise 3L

1. Calculate the angle between the following pairs of vectors
   1. [2 -1 4] and [3 1 2]
      $40.7 \degree$
   2. [2 0 1] and [-2 1 -1]
      $156 \degree$
   3. [2 1 -1] and [3 2 0]
      $25.1 \degree$
   4. [2 -1 -2] and [3 2 -5]
      $40.8 \degree$
   5. [2 3] and [4 6]
      $0$
   6. [2 0 1] and [-4 0 -2]
      $180 \degree$
2. A triangle has vertices at the points A(1,2, 3), B(0,2,5) and C(1,3,−2)
   1. State which two vectors you could use to find the angle at 
      1. A<br>
         AB and AC
      2. B<br>
         BA and BC
   2. Find all the angles of the triangle<br>
      $\angle BAC = $
   3. Find the length of the longest side
3. Find p if the two vectors given are perpendicular.
   1. [2 1 p] and [-3p 2 -2]<br>
      $cos \theta = 0 = \frac{-6p 2 -2p}{6p 2 2p} $
   2. [p -2 4] and [p-1 p -1]<br>
