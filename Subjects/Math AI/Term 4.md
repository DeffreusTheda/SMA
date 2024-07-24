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
   3. Hence or otherwise find the vector PR<br>
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
   1. [2 -1 4] and [3 1 2]<br>
      $40.7 \degree$
   2. [2 0 1] and [-2 1 -1]<br>
      $156 \degree$
   3. [2 1 -1] and [3 2 0]<br>
      $25.1 \degree$
   4. [2 -1 -2] and [3 2 -5]<br>
      $40.8 \degree$
   5. [2 3] and [4 6]<br>
      $0$
   6. [2 0 1] and [-4 0 -2]<br>
      $180 \degree$
2. A triangle has vertices at the points A(1,2, 3), B(0,2,5) and C(1,3,−2)
   1. State which two vectors you could use to find the angle at 
      1. A<br>
         AB and AC
      2. B<br>
         BA and BC
   2. Find all the angles of the triangle<br>
      $\angle BAC =$
      $cos^{-1} (\frac{AB AC}{|AB| |AC|}) =$
      $cos^{-1} (\frac{[-1\~0\~2] \cdot [0\~1\~-5]}{\sqrt{(-1)^2 + 2^2} \cdot \sqrt{1^2 + (-5)^2}}) =$
      $cos^{-1} (\frac{-10}{11.40175425}) =$
      $151 \degree$<br><br>
      $\angle ABC =$
      $cos^{-1} (\frac{BA BC}{|BA| |BC|}) =$
      $cos^{-1} (\frac{[-1\~0\~-2] \cdot [1\~1\~-7]}{\sqrt{(-1)^2 + (-2)^2} \cdot \sqrt{1^2 + 1^2 + (-7)^2}}) =$
      $cos^{-1} (\frac{-1 + 14}{15.96871942}) =$
      $35.5 \degree$<br><br>
      $\angle ACB =$
      $cos^{-1} (\frac{AC CB}{|AC| |CB|}) =$
      $cos^{-1} (\frac{[0\~1\~-5] \cdot [-1\~-1\~7]}{\sqrt{1^2 + (-5)^2} \cdot \sqrt{(-1)^2 + (-1)^2 + 7^2}}) =$
      $cos^{-1} (\frac{-1 + -35}{36.41428291}) =$
      $171 \degree$
   3. Find the length of the longest side
      $|BC| =$
      $\sqrt{1^2 + 1^2 + (-7)^2} =$
      $7.14$
3. Find p if the two vectors given are perpendicular.
   1. $[2\~1\~p] and []-3p\~2\~-2]$<br>
      $[2\~1\~p] \cdot [-3p\~2\~-2] = 0$<br>
      $-6p + 2 - 2p = 0$<br>
      $-8p = -2$<br>
      $p = 0.25$
   2. $[p\~-2\~4] and [p-1\~p\~-1]$<br>
      $[p\~-2\~4] \cdot [p-1\~p\~-1]$<br>
      $p^2-p -2p -4 = 0$<br>
      $p^2-3p = 4$<br>
      $p = 0$<br>

### Exercise 3M

2. Find the vector products of the following pairs of vectors.
   1. $[2\~8\~1]$
   2. $[-3\~0\~6]$
   3. $[2\~-3\~1]$
   4. $[9\~4\~7]$
3. Two sides of a triangle ABC are formed by the vectors AB [2 0 1] and AC [2 1 -1]
   1. Find the vector forming the third side.<br>
      $BC = AC - AB$<br>
      $BC = [0 -1 2]$
   2. Find the area of the triangle.<br>
      $\frac{1}{2} |AB \cdot AC|$<br>
      $\frac{1}{2} |[2\~0\~1] \cdot [2\~1\~-1]|$<br>
      $\frac{1}{2} \sqrt{1^2 + 2^2}$<br>
      $1.12$
4. A triangle has vertices at the points A (1, 2, 3), B (0, 2, 5) and C (1, 3, −2). Find the area of triangle ABC.<br>
   $AB = OB - OA$<br>
   $AB = [-1 0 2]$<br>
   $AC = OC - OA$<br>
   $AC = [0 1 -5]$<br><br>
   $\frac{1}{2} |AB \cdot AC|$<br>
   $\frac{1}{2} |[-1 0 2] \cdot [0 1 -5]|$<br>
   $\frac{1}{2} |[-2 -5 -1]|$<br>
   $\frac{1}{2} \sqrt{(-2)^2 + (-5)^2 + (-1)^2}$<br>
   $2.74$

### Practice

1. Find each vector product of U and V
   1. $U = [1\~2\~2]; V = [2\~1\~2]$<br>
      $[2\~2\~-3]$
   2. $U = [5\~2\~-2]; V = [2\~1\~6]$<br>
      $[14\~-34\~1]$
2. Find the angle between each pair of vectors, correct to the nearest degree.
   1. $U = [13\~-12]; V = [-15\~-8]$<br>
      $cos^{-1} (\frac{13 (-15) + -12 (-8)}{\sqrt{13^2 + (-12)^2} \cdot \sqrt{(-15)^2 + (-8)^2}})$<br>
      $109 \degree$
   2. $U = [-1\~2\~2]; V = [3\~6\~-2]$<br>
      $cos^{-1} (\frac{-1 (3) + 2 (6) + 2 (-2)}{\sqrt{(-1)^2 + 2^2 + 2^2} \cdot \sqrt{3^2 + 6^2 + (-2)^2}})$<br>
      $76.2 \degree$

### Exercise 3N

**1. Find a vector equation of the line passing through two points**

**a. (2, 4) and (3, 1)**

$$r = \begin{bmatrix} 3 \\
1 \end{bmatrix} + t \begin{bmatrix} 1 \\
-3 \end{bmatrix}$$

or

$$r = \begin{bmatrix} 2 \\
4 \end{bmatrix} + t \begin{bmatrix} 4 \\
-2 \end{bmatrix}$$

**b. (2, 1, -1) and (4, 2, 0)**

$$r = \begin{bmatrix} 2 \\
1 \\
-1 \end{bmatrix} + t \begin{bmatrix} 2 \\
1 \\
1 \end{bmatrix}$$

**2. The point (a, -2, b) list on the line**

$r = [x\~y\~z] = [1\~2\~1] + t [1\~8\~-2]

$$r = \begin{bmatrix} x \\
y \\
z \end{bmatrix} = \begin{bmatrix} 1 \\
2 \\
1 \end{bmatrix} + t \begin{bmatrix} 1 \\
8 \\
-2 \end{bmatrix}$$

**a. Find a and b.**

$$\begin{bmatrix} a \\
-2 \\
b \end{bmatrix} = \begin{bmatrix} 1+1t \\
2+8t \\
1-2t \end{bmatrix}$$

$2 + 8t = -2 \textrightarrow t = -0.5$<br>
$a = 1 + 1 (-0.5) = 0.5$<br>
$b = 1 - 2 (-0.5) = 2$

**b. Find the coordinates of the point on the line with x-coordinate equal to 0.**

$0 = 1+t \textrightarrow t = -1$<br>
$y = 2 + 8 (-1) = -6$<br>
$z = 1 - 2 (-1) = 3$<br>
$\therefore (0, -6, 3)$

**3. a. Find the value of $s$ and $p$ if the point $(2, s, p−1)$ lies on the line $r = [1\~0\~2] + t [1\~3\~1]$**

$[2\~s\~p-1] = [1+t\~3t\~2+t]$<br>
$2 = 1+t$<br>
$t = 1$<br>
$s = 3t = 3$<br>
$p-1 = 2+t = 3$<br>
$p = 4$

**3. b. i. Verify the point $A$ $(1, −3, 8)$ lies on the line $r = [3\~1\~2] + t [1\~2\~-3]$ and state the value of $t$ for this point.**

$[1\~-3\~8] = [3+t\~1+2t\~2-3t]$<br>
$1 = 3+t$<br>
$t = -2$<br>
$-3 = 1 + 2 (-2)$<br>
$8 = 2 - 3 (-2)$

**3. b. ii. The point $B$ is also on the line and has parameter $t = 5$. Write down the vector $AB$**

$B = ((3 + 5), (1 + 2 \cdot 5), (2 - 3 \cdot 5))$<br>
$B = (8, 11, -13)$<br>
$AB = OB - OA$

$$AB = \begin{bmatrix} 8 \\
11 \\
-13 \end{bmatrix} - \begin{bmatrix} 1 \\
-3 \\
8 \end{bmatrix}$$

$$AB = \begin 7{bmatrix} \\
14 \\
-21 \end{bmatrix}$$

**4. a. Verify that the point $(2, 1, 3)$ lies on both of the lines**

$$r = \begin{bmatrix} 4 \\
-5 \\
1 \end{bmatrix} + t \begin{bmatrix} -1 \\
3 \\
1 \end{bmatrix}$$

and

$$r = \begin{bmatrix} 4 \\
2 \\
0 \end{bmatrix} + s \begin{bmatrix} 2 \\
1 \\
-3 \end{bmatrix}$$

$$\begin{bmatrix} 2 \\
1 \\
3 \end{bmatrix} = \begin{bmatrix} 4-t \\
-5+3t \\
1+t \end{bmatrix}$$

$2 = 4-t \textrightarrow t = 2$<br>
$1 = -5+3t \textrightarrow t = 2$<br>
$3 = 1+t \textrightarrow t = 2$

$$\begin{bmatrix} 2 \\
1 \\
3 \end{bmatrix} = \begin{bmatrix} 4+2s \\
2+s \\
-3s \end{bmatrix}$$

$2 = 4+2s \textrightarrow s = -1$<br>
$1 = 2+s \textrightarrow s = -1$<br>
$3 = -3s \textrightarrow s = -1$

**4. b. Find the acute angle between the two lines**

$$cos^{-1} (\frac{-1 (2) + 3 (1) + 1 (-3)}{\sqrt{(-1)^2 + 3^2 + 1^2} \sqrt{2^2 + 1^2 + (-3)^2}}) = 99.3 \degree$$

What?

**5. Two lines $l_1$ and $l_2$ have equations $r = [3\~5\~2] + t [-1\~2\~1]$ and $r = [3\~5\~2] + s [2\~-4\~-2]$**

**5. a. Explain why $l_1$ and $l_2$ are parallel.**

Because the ratio between the magnitude of elements in the vector &s& and $t$ are the same.<br>

**5. b. Verify that (1, 9, 4) lies on both lines.**

$$\begin{bmatrix} 1 \\
9 \\
4 \end{bmatrix} = \begin{bmatrix} 3-t \\
5+2t \\
2+t \end{bmatrix}$$

$1 = 3-t \textrightarrow t = 2$<br>
$9 = 5+2t \textrightarrow t = 2$<br>
$4 = 2+t \textrightarrow t = 2$

$$\begin{bmatrix} 1 \\
9 \\
4 \end{bmatrix} = \begin{bmatrix} 3+2s \\
5-4s \\
2-2s \end{bmatrix}$$

$1 = 3+2s \textrightarrow s = -1$<br>
$9 = 5-4s \textrightarrow s = -1$<br>
$4 = 2-2s \textrightarrow s = -1$

**5. c. Explain what this tells you about the two lines.**

**6. The points $A$ and $B$ have coordinates (1,−5,6) and (5, −3, 11) respectively. The line $l_1$ has equation**

$$r = \begin{bmatrix} 3 \\
1 \\
2 \end{bmatrix} + s \begin{bmatrix} 1 \\
3 \\
-2 \end{bmatrix}$$

**6. a. Show $A$ lies on $l_1$**

$$\begin{bmatrix} 1 \\
-5 \\
6 \end{bmatrix} = \begin{bmatrix} 3+s \\
1+3s \\
2-2s \end{bmatrix}$$

$1 = 3+s \textrightarrow s = -2$<br>
$-5 = 1+3s \textrightarrow s = -2$<br>
$6 = 2-2s \textrightarrow s = -2$

**6. b. Show $AB$ is perpendicular to $l_1$**

$$AB = OB - OA = \begin{bmatrix} 5 \\
-3 \\
11 \end{bmatrix} - \begin{bmatrix} 1 \\
-5 \\
6 \end{bmatrix} = \begin{bmatrix} 4 \\
2 \\
5 \end{bmatrix}$$

$$cos^{-1} (\frac{4 (1) + 2 (3) + 5 (-2)}{\sqrt{4^2 + 2^2 + 5^2} \sqrt{1^2 + 3^2 + (-2)^2}}) = 90 \degree$$

**7. The line $l_1$ has equation**

$$r = \begin{bmatrix} 2 \\
0 \\
1 \end{bmatrix} + t \begin{bmatrix} 1 \\
3 \\
2 \end{bmatrix}$$

**7. a. Write down the coordinates of the point $P$ which lies on the line and has parameter $t$**

<!-- $$(2+t, 3t, 1+2t), t = 3 \textrightarrow (5, 9, 7)$$ -->

$$(2+t, 3t, 1+2t)$$

**7. b. The point A has coordinates $(1, 2, −2)$. Find the vector $AP$**

$$AP = OP - OA = \begin{bmatrix} 2+t \\
3t \\
1+2t \end{bmatrix} - \begin{bmatrix} 1 \\
2 \\
-2 \end{bmatrix} = \begin{bmatrix} 1+t \\
3t-2 \\
2t-1 \end{bmatrix}$$

**7. c. Find the value of $t$ for which the vector $AP$ is perpendicular to $l_1$**

$$0 = \frac{4 (1+t) + 7 (3t-2) + 9 (2t-1)}{\sqrt{4^2 + 7^2 + 9^2} \sqrt{(1+t)^2 + (3t)^2 + (2t-1)^2}}$$

$$0 = \frac{43t - 19}{\sqrt{146} \sqrt{15t^2}}$$

$$0 = 43t - 19$$

$$t = \frac{19}{43}$$

**7. d. Find the point on $l_1$ that is closest to $A$**

How?

### Exercise 3O

**1. A particle has position vector $a$ at $t = 0$ and position vector $b$ at time $t$. Find: i. the velocity and ii. the speed of the particle if:**

**a. $a = 2i + j, b = 4i + 5j, t = 2$**

$$v = \frac{1}{2} \begin{bmatrix} 4 \\
5 \end{bmatrix} - \begin{bmatrix} 2
1 \end{bmatrix} = \begin{bmatrix} 1 \\
2 \end{bmatrix}$$

$$s = \sqrt{1^2 + 2^2} = 2.24 km s^{-1}$$

**b. $a = 2i - j, b = i + j, t = 4$**

$$v = \frac{1}{4} \begin{bmatrix} 1 \\
1 \end{bmatrix} - \begin{bmatrix} 2
-1 \end{bmatrix} = \begin{bmatrix} \frac{-1}{4} \\
\frac{1}{2} \end{bmatrix}$$

$$s = \sqrt{(\frac{-1}{4})^2 + (\frac{1}{2})^2} = 0.56 km s^{-1}$$

**c. $a = 3i + j - k, b = i + 5j + k, t = 2$**

$$\begin{bmatrix} 1 \\
5 \\
1 \end{bmatrix} = \begin{bmatrix} 3 \\
1 \\
-1 \end{bmatrix} + 2v$$

$$ 2v = \begin{bmatrix} 1 \\
5 \\
1 \end{bmatrix} - \begin{bmatrix} 3 \\
1 \\
-1 \end{bmatrix} = \begin{bmatrix} -2 \\
4 \\
2 \end{bmatrix}$$

$$v = \begin{bmatrix} -1 \\
2 \\
1 \end{bmatrix}$$

$$s = \sqrt{(-1)^2 + 2^2 + 1^2} = 2.45 km s^{-1}$$

**d. $a = i + k, b = i + 4j - 3k, t = 4$**

$$v = \frac{1}{4} \begin{bmatrix} 1 \\
4 \\
-3 \end{bmatrix} - \begin{bmatrix} 1 \\
0 \\
1 \end{bmatrix} = \begin{bmatrix} 0 \\
1 \\
-1 \end{bmatrix}$$

$$s = \sqrt{1^2 + (-1)^2} = 1.41 km s^{-1}$$

**2. Write the following velocities as column vectors taking the base vectors as due east and north.**

**a. 10 km h^{-1} due west**

$$\begin{bmatrix} -10 \\
0 \end{bmatrix} km h^{-1}$$

**b. 7.5 km h^{-1} in the direction**

$$\begin{bmatrix} -3 \\
4 \end{bmatrix}$$

$$\begin{bmatrix} -4.5 \\
6 \end{bmatrix} km h^{-1}$$

**c. 18 km h^{-1} in the direction**

$$\begin{bmatrix} -1 \\
-4 \\
8 \end{bmatrix}$$

$$\begin{bmatrix} -2 \\
-8 \\
16 \end{bmatrix}$$

**d. 5 km h^{-1} south-west**

$$\begin{bmatrix} -3.5355339059 \\
-3.5355339059 \end{bmatrix}$$

**e. 15 km h^{-1} on a bearing of 40 \degree**

$$\begin{bmatrix} 9.641814145 \\
11.49066665 \end{bmatrix}$$

**f. 12 km h^{-1} on a bearing of 120 \degree**

$$\begin{bmatrix} 10.39230485 \\
-6 \end{bmatrix}$$

**3. A buoy is set as the origin of a coordinate system. At 13.00 a boat is $20 m$ east and $30 m$ north of a buoy and has position vector**

$$\begin{bmatrix} 20 \\
30 \end{bmatrix}$$

**a. Find the distance of the boat from the buoy at 13:00**

$$\sqrt{20^2 + 30^2} = 36 km$$

**The boat is moving with velocity**

$$\begin{bmatrix} -3 \\
-5 \end{bmatrix} m s^{-1}$$

**b. Find the position of the boat t seconds after 13:00**

$$\begin{bmatrix} 20 - 3t \\
30 - 5t \end{bmatrix}$$

**c. Hence find the shortest distance from the boat to the buoy**

$$\sqrt{(20-3x)^2 + (30-5x)^2} \textrightarrow Draw \textrightarrow MIN$$

$$\therefore s_{min} = 1.71, at x = 6.14$$

### Formula

Scalar and Vector Product: $v \cdot w  = |v| |w| cos \theta = |v \times w|$

Area of a parallelogram: $A = |v \times w|$ where $v$ and $w$ form two adjacent sides of a parallelogram.

### Checkpoint - Vector

Shift (V-WIN)
F6 (Draw) -> F5 -> EXE

### Vectors Quiz

**2. Determine whether $u$ is orthogonal, parallel to $v$, or neither**

**2. (a)**

$$u = \begin{bmatrix} -frac{1}{2} \\
2 \end{bmatrix}, v = \begin{bmatrix} -2 \\
\frac{1}{2} \end{bmatrix}$$

Orthogonal

**2. (b)**

$$u = \begin{bmatrix} 8 \\
4 \end{bmatrix}, v = \begin{bmatrix} 6 \\
-12 \end{bmatrix}$$

2:1 | 1:-2 -> Orthogonal

**2. (c)**

$$u = \begin{bmatrix} 2\sqrt{3} \\
2 \end{bmatrix}, v = \begin{bmatrix} 1 \\
-\sqrt{3} \end{bmatrix}$$

\sqrt{3}:1 | 1:-\sqrt{3} -> Orthogonal

**3. Find the interior angles of the triangle $ABC$, the coordinates of whose vertices are given.**

**(a) A(1,2), B(3,4), C(2,5)**

$$\angle BAC = cos^{-1} (\frac{AB \cdot AC}{|AB| |AC|}) = cos^{-1} (\frac{2 (1) + 2 (3)}{\sqrt{2^2 + 2^2} \sqrt{1^2 + 3^2}}) = 26.6 \degree$$

$$\angle ABC = cos^{-1} (\frac{BA \cdot BC}{|BA| |BC|}) = cos^{-1} (\frac{-2 (-1) + -2 (1)}{\sqrt{(-2)^2 + (-2)^2} \sqrt{(-1)^2 + 1^2}}) = 90 \degree$$

$$\angle ACB = 180 \degree - 90 \degree - 26.6 \degree = 63.4 \degree$$

**(b) A(3,4), B(-1,-7), C(-8,-2)**

$$\angle BAC = cos^{-1} (\frac{AB \cdot AC}{|AB| |AC|}) = cos^{-1} (\frac{-4 (-11) + -11 (-6)}{\sqrt{(-4)^2 + (-11)^2} \sqrt{(-11)^2 + (-6)^2}}) = 41.4 \degree$$

$$\angle ABC = cos^{-1} (\frac{BA \cdot BC}{|BA| |BC|}) = cos^{-1} (\frac{4 (-7) + 11 (5)}{\sqrt{4^2 + 11^2} \sqrt{(-7)^2 + 5^2}}) = 74.4 \degree$$

$$\angle ACB = 180 \degree - 41.4 \degree - 74.4 \degree = 64.1 \degree$$

**(c) A(3,-5), V(1,-9), C(-7,-9)**

$$\angle BAC = cos^{-1} (\frac{AB \cdot AC}{|AB| |AC|}) = cos^{-1} (\frac{-2 (-8) + -4 (0)}{\sqrt{(-2)^2 + (-4)^2} \sqrt{(-8)^2 + 0^2}}) = 41.6 \degree$$

$$\angle ABC = cos^{-1} (\frac{BA \cdot BC}{|BA| |BC|}) = cos^{-1} (\frac{2 (-8) + 4 (0)}{\sqrt{2^2 + 4^2} \sqrt{(-8)^2 + 0^2}}) = 116.5 \degree$$

$$\angle ACB = 180 \degree - 41.6 \degree - 116.5 \degree = 21.8 \degree$$

**4. Find a vector perpendicular to**

$$u = \begin{bmatrix} 3 \\
5 \end{bmatrix}$$

By rotating the vector by $90 \degree$ clockwise,

$$\begin{bmatrix} 5 \\
-3 \end{bmatrix}$$

**5. Determine if the triangle ABC is right-angled by using the scalar product, where the coordinates of its vertices are A(1,-3), B(2,0), C(6,-2)**

$$\angle BAC = cos^{-1} (\frac{AB \cdot AC}{|AB| |AC|}) = a = cos^{-1} (\frac{1 (5) + 3 (1)}{\sqrt{1^2 + 3^2} \sqrt{5^2 + 1^2}}) = 60.3 \degree$$

$$\angle ABC = cos^{-1} (\frac{BA \cdot BC}{|BA| |BC|}) = 81.9 \degree$$

$$\angle ACB = 180 \degree - 60.3 \degree - 81.9 \degree = 37.9 \degree$$

None of the angle is $90 \degree$, therefore it's not a right-angled triangle.

**6. For what non-zero value(s) of $b$ are the vectors**

$$\begin{bmatrix} -6 \\
b \end{bmatrix}$$

**and**

$$\begin{bmatrix} b \\
b^2 \end{bmatrix}$$

**perpendicular?**

$$0 = \frac{-6 (b) + b (b^2)}{\sqrt{(-6)^2 + b^2} \sqrt{b^2 + (b^2)^2}}$$

**7. Two vectors**

$$\begin{bmatrix} 3 \\
4 \end{bmatrix}$$

**and**

$$\begin{bmatrix} x \\
1 \end{bmatrix}$$

**have an angle of $30 \degree$ between them. Find the possible values of $x$.**

$$30 = cos^{-1} (\frac{3x + 4}{5 \sqrt{x^2 + 1}})$$

With brute-forcing (guessing X, seeing result and adjusting it until it's accurate), I get this:

$$x = 2.34105821$$

I don't know why solver can't do this though

#### Chapter 8 practice questions

**1. Vector**

$$u = \begin{bmatrix} 8 \\
-2 \end{bmatrix}$$

**Determine the components of vector $v$ when:**

**(a) $v = -u$**

$$v = \begin{bmatrix} -8 \\
2 \end{bmatrix}$$

**(b) $v = \frac{u}{2}$**

$$v = \begin{bmatrix} 4 \\
-1 \end{bmatrix}$$

**(c) $3u = 2v$**

$$v = \begin{bmatrix} 12 \\
-3 \end{bmatrix}$$

**2. Vector**

$$u = \begin{bmatrix} 6 \\
-2 \\
7 \end{bmatrix}$$

**and**

$$v = \begin{bmatrix} -2 \\
8 \\
-3 \end{bmatrix}$$

**Determine the vector components of $w$ when:**

**(a) $w = -u + v$**

$$w = \begin{bmatrix} -8 \\
10 \\
-10 \end{bmatrix}$$

**(b) $w = u - v$**

$$w = \begin{bmatrix} 8 \\
-10 \\
10 \end{bmatrix}$$

**(c) $w = 5u - 2v$**

$$w = \begin{bmatrix} 34 \\
-26 \\
41 \end{bmatrix}$$

**3. Find the equation of each line in the form $\frac{x-h}{p} = \frac{y-k}{q}$ that passes through the given point $P$ with gradient $m$**

**(a) $P(-2,2), m = \frac{3}{5}$**

<!-- TODO:-->

**(b) $P(4,-1), m = -\frac{2}{3}$**

<!-- TODO:-->

**(c) $P(0,4), m = \frac{3}{2}$**

<!-- TODO:-->

**(d) $P(11,7), m = -\frac{4}{3}$**

<!-- TODO:-->

**4. Find the equation of the line in 3-space dimensions through the given point $P$ with the gradient described by the direction vector $u$**

$$\textbf (a) P(3,0,-2), u = \begin{bmatrix} 2 \\
-3 \\
-6 \end{bmatrix}$$

$$\begin{bmatrix} 3 \\
0 \\
-2 \end{bmatrix} = \begin{bmatrix} x_i \\
y_i \\
z_i \end{bmatrix} + t \begin{bmatrix} 2 \\
-3 \\
-6 \end{bmatrix}$$

Assuming $t = 0$,

$$r = \begin{bmatrix} 3 \\
0 \\
-2 \end{bmatrix} + t \begin{bmatrix} 2 \\
-3 \\
-6 \end{bmatrix}$$

$$\textbf (b) P(-4,4,0), u = \begin{bmatrix} 5 \\
0 \\
-2 \end{bmatrix}$$

$$r = \begin{bmatrix} -4 \\
4 \\
0 \end{bmatrix} + t \begin{bmatrix} 5 \\
0 \\
-2 \end{bmatrix}$$

**5.**

**6. A radio-controlled boat in a pond moves in a direction described by the vector**

$$u = \begin{bmatrix} -1 \\
2 \end{bmatrix}$$,

**moving $1 m$ to the west for every $2 m$ to the north, every minute. Determine, accurate to 3 significant figures, the distance covered by the boat in:**

**(a) 1 minute**

$$\sqrt{(-1)^2 + 2^2} = \sqrt{5} = 2.24 m$$

**(b) 2.25 minute**

$$sqrt{(-1 \cdot 2.25)^2 + (2 \cdot 2.25)^2} = 5.03 m$$

**(c) 10 minute**

$$sqrt{(-1 \cdot 10)^2 + (2 \cdot 10)^2} = \sqrt{500} = 22.4 m$$

**(d) t minute**

$$sqrt{(-t)^2 + (2t)^2}$$

**7. The boat in question 6 starts from a position $20 m$ to the east of the person controlling it and moves along the same vector $u$. Find the distance from the container to the boat after:**

**(a) 1 minute**

Let B be the coordinate of the boat,

$$B = \begin{bmatrix} 20 \\
0 \end{bmatrix} + \begin{bmatrix} -1 \\
2 \end{bmatrix} = \begin{bmatrix} 19 \\
2 \end{bmatrix}$$

$$\sqrt{19^2 + 2^2} = \sqrt{365} = 19.1 m$$

**(b) t minute**

$$B = \begin{bmatrix} 20 \\
0 \end{bmatrix} + t \begin{bmatrix} -1 \\
2 \end{bmatrix}$$

$$\sqrt{(20 - t)^2 + (2t)^2}$$

**8. A second boat, starting at the same time and $25 m$ to the west of the boat in question 7, moves in a direction described by the vector**

$$v = \begin{bmatrix} 2 \\
1 \end{bmatrix}$$,

**moving $2 m$ to the east for every $1 m$ to the north, every minute.**

**(a) Determine the distance between the two boats after:**

**(i) 1 minute**

Let B the coordinate of the first boat and S the coordinate of the second boat,

$$B = \begin{bmatrix} 20 \\
0 \end{bmatrix} + \begin{bmatrix} -1 \\
2 \end{bmatrix} = \begin{bmatrix} 19 \\
2 \end{bmatrix}$$

$$S = \begin{bmatrix} -25 \\
0 \end{bmatrix} + \begin{bmatrix} 2 \\
1 \end{bmatrix} = \begin{bmatrix} -23 \\
1 \end{bmatrix}$$

$$SB = \begin{bmatrix} -23 \\
1 \end{bmatrix} - \begin{bmatrix} 19 \\
2 \end{bmatrix} = \begin{bmatrix} -42 \\
-1 \end{bmatrix}$$

$$\sqrt{(-42)^2 + (-1)^2} = 42.0 m$$

**(ii) t minute**

Let B the coordinate of the first boat and S the coordinate of the second boat,

$$B = \begin{bmatrix} 20 \\
0 \end{bmatrix} + t \begin{bmatrix} -1 \\
2 \end{bmatrix} = \begin{bmatrix} 20-t \\
2t \end{bmatrix}$$

$$S = \begin{bmatrix} -25 \\
0 \end{bmatrix} + t \begin{bmatrix} 2 \\
1 \end{bmatrix} = \begin{bmatrix} -25+2t \\
t \end{bmatrix}$$

$$SB = \begin{bmatrix} 20-t \\
2t \end{bmatrix} - \begin{bmatrix} -25+2t \\
t \end{bmatrix} = \begin{bmatrix} 45-3t \\
t \end{bmatrix}$$

$$\sqrt{(55-3t)^2 + t^2}$$

**(b) Would the two boats collide?**

Let $s$ be the $t$ of the second boat, they would collide at the coordinate:

$$\begin{bmatrix} 20-t \\
2t \end{bmatrix} = \begin{bmatrix} -25+2s \\
s \end{bmatrix}$$

$$2t = s$$

$$\begin{bmatrix} 20-t \\
2t \end{bmatrix} = \begin{bmatrix} -25+4t \\
2t \end{bmatrix}$$

$$20 - t = -25 + 4t \textrightarrow t = 9$$

No, they wouldn't collide if $t = s$, but
Yes, they may collide, but only if $2t = s$ holds true.

**9. Find the scalar product for each pair of vectors**

$$\textbf (a) u = \begin{bmatrix} -5 \\
2 \end{bmatrix}, v = \begin{bmatrix} 2 \\
1 \end{bmatrix}$$

$$-5 (2) + 2 (1) = -9$$

$$\textbf (b) u = \begin{bmatrix} -3 \\
-6 \end{bmatrix}, v = \begin{bmatrix} -6 \\
3 \end{bmatrix}$$

$$-3 (-6) + -6 (3) = 0$$

$$\textbf (c) u = \begin{bmatrix} 8 \\
2 \\
-7 \end{bmatrix}, v = \begin{bmatrix} -1 \\
4 \\
0 \end{bmatrix}$$

$$8 (-1) + 2 (4) + -7 (0) = 0$$

$$\textbf (d) u = \begin{bmatrix} -2 \\
2 \\
-1 \end{bmatrix}, v = \begin{bmatrix} 2 \\
-3 \\
6 \end{bmatrix}$$

$$-2 (2) + 2 (-3) + -3 (6) = -28$$

**10. Find the scalar product for each pair of vectors, where $\theta$ is the angle between them.**

$$\textbf (a) |u| = 7, |v| = 11, \theta = 60 \degree$$

Let $S$ be the scalar product,

$$\theta = cos^{-1} (\frac{S}{|u| |v|}) \textrightarrow S = cos \theta \cdot |u| |v|$$

$$S = cos 60 \cdot 7 \cdot 11 = 0.5$$

$$\textbf (b) |u| = 11.2, |v| = 5, \theta = 120 \degree$$

$$S = cos 120 \cdot 11.2 \cdot 5 = -0.5$$

$$\textbf (c) |u| = 9, |v| = 9, \theta = 45 \degree$$

$$S = cos 45 \cdot 9 \cdot 9 = 0.71$$

$$\textbf (d) |u| = 13, |v| = 6, \theta = 23 \degree$$

$$S = cos 23 \cdot 13 \cdot 6 = 0.99$$

**11. Find each vector product: $u \times v$**

$$\textbf (a) u = \begin{bmatrix} 0 \\
1 \\
0 \end{bmatrix}, v = \begin{bmatrix} 1 \\
0 \\
0 \end{bmatrix}$$

$$\begin{bmatrix} 1 (0) - 0 (0) \\
0 (1) - 0 (0) \\
0 (0) - 1 (1) \end{bmatrix} = \begin{bmatrix} 0 \\
0 \\
-1 \end{bmatrix}$$

$$\textbf (a) u = \begin{bmatrix} -1 \\
0 \\
0 \end{bmatrix}, v = \begin{bmatrix} 0 \\
-1 \\
0 \end{bmatrix}$$

$$\begin{bmatrix} 0 (0) - -1 (0) \\
0 (0) - 0 (-1) \\
-1 (-1) - 0 (0) \end{bmatrix} = \begin{bmatrix} 0 \\
0 \\
1 end{bmatrix}$$

$$\textbf (a) u = \begin{bmatrix} 1 \\
2 \\
2 \end{bmatrix}, v = \begin{bmatrix} 2 \\
1 \\
2 \end{bmatrix}$$

$$\begin{bmatrix} 2 (2) - 1 (2) \\
2 (2) - 2 (1) \\
1 (1) - 2 (2) \end{bmatrix} = \begin{bmatrix} 2 \\
2 \\
-3 end{bmatrix}$$

$$\textbf (a) u = \begin{bmatrix} 5 \\
2 \\
-2 \end{bmatrix}, v = \begin{bmatrix} 2 \\
1 \\
6 \end{bmatrix}$$

$$\begin{bmatrix} 2 (6) - 1 (-2) \\
-2 (2) - 6 (5) \\
5 (1) - 2 (2) \end{bmatrix} = \begin{bmatrix} 14 \\
-34 \\
1 end{bmatrix}$$

**12. Find the angle between each pair of vectors, correct to the nearest degree.**

$$\textbf (a) u = \begin{bmatrix} -9 \\
12 \end{bmatrix}, v = \begin{bmatrix} 4 \\
3 \end{bmatrix}$$

<!-- TODO:-->

$$\textbf (b) u = \begin{bmatrix} -9 \\
12 \end{bmatrix}, v = \begin{bmatrix} 4 \\
3 \end{bmatrix}$$

<!-- TODO:-->

$$\textbf (c) u = \begin{bmatrix} -9 \\
12 \end{bmatrix}, v = \begin{bmatrix} 4 \\
3 \end{bmatrix}$$

<!-- TODO:-->

$$\textbf (d) u = \begin{bmatrix} -9 \\
12 \end{bmatrix}, v = \begin{bmatrix} 4 \\
3 \end{bmatrix}$$

<!-- TODO:-->

### Parametric Equation of Lines

2D:

$$y = mx + c \textrightarrow m = \frac{q}{p}$$

Passing through (a,b)

$$\frac{x-a}{p} = \frac{y-b}{q}$$

3D:

Point $A(a_1, a_2, a_3)$ with a gradient described by vector 

$$\begin{bmatrix} p \\
q \\
s \end{bmatrix}$$

$$\frac{x-a_1}{p} = \frac{y-a_2}{q} = \frac{z-a_3}{s}$$

### Chapter Review

**18 P2. An aircraft takes off from an airfield. The position of the aircraft at time $t$ hours after takeoff is given by the vector**

$$r = \begin{bmatrix} 0 \\
0 \\
1 \end{bmatrix} + t \begin{bmatrix} 50 \\
60 \\
1 \end{bmatrix}$$

**a. Find the position vector of the aircraft 4 hours after takeoff.**

$$t = 4, \begin{bmatrix} 50t \\
60t \\
1+t \end{bmatrix} = \begin{bmatrix} 200 \\
240 \\
5 \end{bmatrix}$$

**A second aircraft takes off from a different airfield. The position vector of this aircraft is given by the vector**

$$s = \begin{bmatrix} -90 \\
-100 \\
0 \end{bmatrix} + \lambda \begin{bmatrix} 60 \\
70 \\
1 \end{bmatrix}$$

**b. Determine if the two flight paths intersect and, if so, state the point of intersection.**

$$\begin{bmatrix} 50t \\
60t \\
1+t \end{bmatrix} = \begin{bmatrix} 60λ - 90 \\
70λ - 100 \\
λ \end{bmatrix}$$

Using solver, $t = 3, λ = 4$.

$$\begin{bmatrix} 150 \\
180 \\
4 \end{bmatrix}$$

**The two aircraft took off at the same time, so $λ = t$**

**c. State, with a reason, whether the two aircraft actually collide.**

$$\begin{bmatrix} 50t \\
60t \\
1+t \end{bmatrix} = \begin{bmatrix} 60t - 90 \\
70t - 100 \\
t \end{bmatrix}$$

$$t = \begin{bmatrix} 9 \\
10 \\
no\~solution \end{bmatrix}$$

$\therefore$, the two flight paths don't intersect.

**d. Calculate the distance between the two airfields.**

$$\begin{bmatrix} 0 \\
0 \\
1 \end{bmatrix} - \begin{bmatrix} -90 \\
-100 \\
0 \end{bmatrix} = \begin{bmatrix} 90 \\
100 \\
1 \end{bmatrix}$$

$$\sqrt{90^2 + 100+2 + 1^2} = 134 km$$

**e. Calculate the shortest distance that ever exists between the two aircraft and the time when this occurs.**

$$d = s - t = \begin{bmatrix} 10t - 90 \\
10t - 100 \\
1 \end{bmatrix}$$

Using GDC, the minimum value of $|d|$ where $t$ as the X axis is $7.141$ at $t = 9.5$

