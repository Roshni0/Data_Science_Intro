#fun fact, python is develops on from c!
#integers
struct _longobject {
    long ob_refcnt;
    PyTypeObject *ob_type;
    size_t ob_size;
    long ob_digit[1];
};

#lists
#integer list
L = list(range(10))
#string list
L2 = [str(c) for c in L]
#heterogeneous list
L3 = [True, "2", 3.0, 4]
#creating arrays from lists
import numpy as np
np.array([1, 4, 2, 5, 3])
# nested lists result in multi-dimensional arrays
np.array([range(i, i + 3) for i in [2, 4, 6]])

#different data types
bool_	#Boolean value (Stored as a byte)
int_	#Integer value
int8	#Byte value from -128 to 127 
int16	#Integer valye from -32768 to 32767
int32	#Integer value from -2147483648 to 2147483647
uint8	#Unsigned integer value from 0 to 255
uint16	#Unsigned integer value from 0 to 65535
float_	#Float with a sign bit, 11 bits for expo, 52 bits for mantissa
complex_	#Complex No 
