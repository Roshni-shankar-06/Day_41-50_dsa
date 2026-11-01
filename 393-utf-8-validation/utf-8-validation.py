class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        remaining_bytes = 0
        
        for num in data:
            # We only care about the 8 least significant bits
            byte = num & 255
            
            if remaining_bytes == 0:
                # Count the number of leading 1s
                if (byte >> 7) == 0b0:
                    remaining_bytes = 0
                elif (byte >> 5) == 0b110:
                    remaining_bytes = 1
                elif (byte >> 4) == 0b1110:
                    remaining_bytes = 2
                elif (byte >> 3) == 0b11110:
                    remaining_bytes = 3
                else:
                    return False
            else:
                # Check if it is a valid continuation byte (starts with 10)
                if (byte >> 6) != 0b10:
                    return False
                remaining_bytes -= 1
                
        return remaining_bytes == 0
