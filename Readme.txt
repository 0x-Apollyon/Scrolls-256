SCROLLS-256

My attempt to create a symmetric encryption algorithm.
This repo documents my journey into basics of cryptography.
The keysize of the scrolls algorithm is 256 bits.
DO NOT USE IN PRODUCTION. DOING SO WOULD BE VERY RETARDED.

Commit-1
Date:1/4/2024
Note: Basic XOR algorithm for now, plan to add row and bit rotations to make it operational and not trash.
Total Number of Keys: 2^198 [401734511064747568885490523085290650630550748445698208825344]

Commit-2
Date:2/4/2024
Note: Added vertical and horizontal rotation to the matrix to make the algorithm better. They still return similar return for smaller texts though.
Also due to padding, it is possible to determine the size of the encrypted message(before padding)
Currently working for the decryption code for the new version
Total Number of Keys: 2^256 [115792089237316195423570985008687907853269984665640564039457584007913129639936]
Thats 288230376151711743 (2^58)-1 times 2^198
(I realised that the whole key is being used even though in every round 2 rows are for rotation, they are used for XORing in other rounds)