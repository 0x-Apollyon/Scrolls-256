import sys
import os
import copy



def encrypt_encoded(string , key):
    block_size = 32
    encoded_string = bytes(string ,"latin-1")
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





    def vertical_rotation(block_matrix, rotr_row):

        new_block_matrix = []
        for i in range(0,8):
            new_vertical = []
            for j , row in enumerate(block_matrix):
                new_vertical.append(row[i].to_bytes())
            new_block_matrix.append(new_vertical)
        
        rotated_matrix = []
        for i , vertical in enumerate(new_block_matrix):

            useful_thing = rotr_row[i]%4
            new_vertical = vertical[4-useful_thing:4]
            new_vertical_rotated = new_vertical + vertical[0:4-useful_thing]
            rotated_matrix.append(new_vertical_rotated)


        output_block_matrix = []
        for i in range(0,4):
            horizontal = b""
            for vertical in rotated_matrix:
                horizontal = horizontal + vertical[i]
            output_block_matrix.append(horizontal)

        return output_block_matrix


    def rotate_right(new_block_matrix_row , rotr_row , height):

        rotr_elements = []
        for i in range(0,2):
            rotr_element = rotr_row[i*4:((i+1)*4)]
            rotr_elements.append(rotr_element)
        
        net_useful = 0
        for element in rotr_elements:
            useful_part = element[height]
            net_useful = net_useful + useful_part
        net_useful = net_useful % 6


        new_block_matrix_row_rotate_part = new_block_matrix_row[8-net_useful:8]
        new_block_matrix_row_rotated = new_block_matrix_row_rotate_part + new_block_matrix_row[0:8-net_useful]
        return new_block_matrix_row_rotated

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
                    new_block_matrix_row = new_block_matrix_row + new_mini_block.to_bytes()
                
                rotated_new_block_matrix_row = rotate_right(new_block_matrix_row , rotr_elements[0] , i)
                new_block_matrix.append(rotated_new_block_matrix_row)

            block_matrix = vertical_rotation(block_matrix, rotr_elements[1])
            block_matrix = new_block_matrix.copy()
            
        xored_block = b""
        for row in block_matrix:
            xored_block = xored_block + row
        new_block_stream.append(xored_block)


    encrypted_message = b""
    for block in new_block_stream:
        encrypted_message = encrypted_message + block
    return encrypted_message

    
strng = input("Enter characters to encrypt: ")
key = os.urandom(32)
print(encrypt_encoded(strng, key))
print(f"KEY --> {key}")




          

        
                    

            

        

    


