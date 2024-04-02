import sys
import os
import copy

string = input("Enter message to encrypt: ")
block_size = 32

encoded_string = bytes(string ,"utf-16")
length_in_bytes = len(encoded_string)
padding_len = length_in_bytes % 32
for i in range(32 - padding_len):
    encoded_string =  encoded_string + b"\x00"
length_in_bytes = len(encoded_string)
number_of_blocks = int(length_in_bytes/32)
block_stream = []
for i in range(0,number_of_blocks):
    block = encoded_string[i*32:((i+1)*32)]
    block_stream.append(block)


key = os.urandom(32)
print("KEY:")
print(key)


key_matrix = []

for i in range(4):
    key_row = key[i*8:((i+1)*8)]
    key_matrix.append(key_row)


new_block_stream = []
for block in block_stream:

    block_matrix = []

    for i in range(4):
        block_matrix_row = block[i*8:((i+1)*8)]
        block_matrix.append(block_matrix_row)


    xor_rows_mapping = { 1:(1,2) , 2:(2,3) , 3:(3,4) , 4:(4,1)}
    rotr_rows_mapping = { 1:(3,4) , 2:(4,1) , 3:(1,2) , 4:(2,3) }

    for i in range(1,4):
        
        current_round = i

        xor_rows = xor_rows_mapping[i]
        xor_elements = []

        for i in xor_rows:
            current_xor_row = key_matrix[i-1]
            for j in range(2):
                xor_element = current_xor_row[j*4:((j+1)*4)]
                xor_elements.append(xor_element)
        
        rotr_rows = rotr_rows_mapping[i]
        rotr_elements = []

        for i in rotr_rows:
            rotr_element = key_matrix[i-1]
            rotr_elements.append(rotr_element)

        new_block_matrix = []
        for i , block_matrix_row in enumerate(block_matrix):
            new_block_matrix_row = b""
            for x , mini_block in enumerate(block_matrix_row):
                new_mini_block = mini_block
                for xor_element in xor_elements:
                    new_mini_block = new_mini_block  ^ xor_element[i]
                   # rotr_element = rotr_elements[0][x]
                    #rotr_element_net = rotr_element % 8
                    #new_mini_block = rotate_right(new_mini_block , rotr_element_net)
                    #print(new_mini_block)
                new_block_matrix_row = new_block_matrix_row + new_mini_block.to_bytes()
            
            new_block_matrix.append(new_block_matrix_row)

        block_matrix = new_block_matrix.copy()
    xored_block = b""
    for row in block_matrix:
        xored_block = xored_block + row
    new_block_stream.append(xored_block)

encrypted_message = b""
for block in new_block_stream:
    encrypted_message = encrypted_message + block
print("ENCRYPTED MESSAGE: ")
print(encrypted_message)


    
    



          

        
                    

            

        

    