##### SPHERE-SiPM retina description #####

##################################3
y = [
     2.5,2.5,
     3.0,3.0,3.0,3.0,3.0,
     3.5,3.5,3.5,3.5,3.5,3.5,3.5,
     4.0,4.0,4.0,4.0,4.0,4.0,4.0,
     4.5,4.5,4.5,4.5,4.5,4.5,4.5,
     5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,
     5.5,5.5,5.5,5.5,5.5,5.5,5.5,
     6.0,6.0,6.0,6.0,6.0,
     6.5,6.5
    ]
x = [ 
       11,13,
       6, 8,10,12,14,
       5, 7, 9,11,13,15,17,
       6, 8,10,12,14,16,18,
      5, 7, 9,11,13,15,17,
       4, 6, 8,10,12,14,16,18,
       5, 7, 9,11,13,15,17,
       8,10,12,14,16, 
       9,11
    ]
N = [
       56, 57, 
      53, 32, 33, 34, 35, 
      52, 31, 16, 17, 18, 36, 60, 
      30, 15,  6,  7, 19, 37, 61,
      29, 14,  5,  1,  2,  8, 20,
      49, 28, 13,  4,  3,  9, 21, 39,
      48, 27, 12, 11, 10, 22, 40,
      26, 25, 24, 23, 41, 
      45, 44
    ]
C = [ 127 for i in range(len(N))]