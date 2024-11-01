def is_valid_utf8(data):
    # Number of bytes to be processed in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        # Mask to get only the first byte in binary
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes based on the leading bits
            if (byte & mask1) == 0:
                # 1-byte character (ASCII)
                num_bytes = 0
            elif (byte & (mask1 >> 1)) == mask1:
                # 2-byte character
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 1):
                # 3-byte character
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 2):
                # 4-byte character
                num_bytes = 3
            else:
                # Invalid UTF-8 leading byte
                return False
        else:
            # Check if the byte is a continuation byte (starts with '10')
            if (byte & mask1) != mask1 or (byte & mask2) != 0:
                return False
            # Reduce the number of expected continuation bytes
            num_bytes -= 1

    # If num_bytes is not 0 here, then there was an incomplete character
    return num_bytes == 0
