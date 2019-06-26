import ctypes

user = ctypes.cdll.LoadLibrary('./ot.so')

#overwrite default return type to char
user.GetPublicParams.restype = ctypes.c_char_p
user.GetBlinedKey.restype = ctypes.c_char_p
user.GetSharedTuple.restype = ctypes.c_char_p
user.GetBValue.restype = ctypes.c_char_p
user.GetEValue.restype = ctypes.c_char_p
user.GetAValue.restype = ctypes.c_char_p
user.GetBlinedR.restype = ctypes.c_char_p

user1 = ctypes.cdll.LoadLibrary('./ot2.so')

#overwrite default return type to char
user1.GetPublicParams.restype = ctypes.c_char_p
user1.GetBlinedKey.restype = ctypes.c_char_p
user1.GetSharedTuple.restype = ctypes.c_char_p
user1.GetBValue.restype = ctypes.c_char_p
user1.GetEValue.restype = ctypes.c_char_p
user1.GetAValue.restype = ctypes.c_char_p
user1.GetBlinedR.restype = ctypes.c_char_p