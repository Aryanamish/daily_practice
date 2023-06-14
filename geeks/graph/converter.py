# Python3 program to implement
# the above approach
import ctypes

from ctypes.wintypes import BOOL, HWND, HANDLE, HGLOBAL, UINT, LPVOID
from ctypes import c_size_t as SIZE_T

OpenClipboard = ctypes.windll.user32.OpenClipboard
OpenClipboard.argtypes = HWND,
OpenClipboard.restype = BOOL
EmptyClipboard = ctypes.windll.user32.EmptyClipboard
EmptyClipboard.restype = BOOL
GetClipboardData = ctypes.windll.user32.GetClipboardData
GetClipboardData.argtypes = UINT,
GetClipboardData.restype = HANDLE
SetClipboardData = ctypes.windll.user32.SetClipboardData
SetClipboardData.argtypes = UINT, HANDLE
SetClipboardData.restype = HANDLE
CloseClipboard = ctypes.windll.user32.CloseClipboard
CloseClipboard.restype = BOOL
CF_UNICODETEXT = 13

GlobalAlloc = ctypes.windll.kernel32.GlobalAlloc
GlobalAlloc.argtypes = UINT, SIZE_T
GlobalAlloc.restype = HGLOBAL
GlobalLock = ctypes.windll.kernel32.GlobalLock
GlobalLock.argtypes = HGLOBAL,
GlobalLock.restype = LPVOID
GlobalUnlock = ctypes.windll.kernel32.GlobalUnlock
GlobalUnlock.argtypes = HGLOBAL,
GlobalSize = ctypes.windll.kernel32.GlobalSize
GlobalSize.argtypes = HGLOBAL,
GlobalSize.restype = SIZE_T

GMEM_MOVEABLE = 0x0002
GMEM_ZEROINIT = 0x0040

unicode_type = type(u'')


def get():
    text = None
    OpenClipboard(None)
    handle = GetClipboardData(CF_UNICODETEXT)
    pcontents = GlobalLock(handle)
    size = GlobalSize(handle)
    if pcontents and size:
        raw_data = ctypes.create_string_buffer(size)
        ctypes.memmove(raw_data, pcontents, size)
        text = raw_data.raw.decode('utf-16le').rstrip(u'\0')
    GlobalUnlock(handle)
    CloseClipboard()
    return text


def put(s):
    if not isinstance(s, unicode_type):
        s = s.decode('mbcs')
    data = s.encode('utf-16le')
    OpenClipboard(None)
    EmptyClipboard()
    handle = GlobalAlloc(GMEM_MOVEABLE | GMEM_ZEROINIT, len(data) + 2)
    pcontents = GlobalLock(handle)
    ctypes.memmove(pcontents, data, len(data))
    GlobalUnlock(handle)
    SetClipboardData(CF_UNICODETEXT, handle)
    CloseClipboard()


paste = get
copy = put


# Function to insert vertices
# to adjacency list
def insert(adj, u, v):

    # Insert a vertex v to vertex u
    adj[u].append(v)
    return


# Function to display adjacency list
def printList(adj, V):

    for i in range(V):
        print(i, end='')

        for j in adj[i]:
            print(' --> ' + str(j), end='')

        print()

    print()


# Function to convert adjacency
# list to adjacency matrix
def convert(adj, V):

    # Initialize a matrix
    matrix = [[0 for j in range(V)] for i in range(V)]

    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1

    return matrix


# Function to display adjacency matrix
def printMatrix(adj, V):
    rv = ''
    for i in range(V):
        for j in range(V):
            rv += str(adj[i][j]) + ', '

        rv += '\n'
    copy(rv)
    return rv


# Driver code
if __name__ == '__main__':

    V, E = map(int, input().split())
    adj = [[] for i in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)

    # Function call which returns
    # adjacency matrix after conversion
    adjMatrix = convert(adj, V)

    # Display adjacency matrix
    print("Adjacency Matrix: ")
    print(printMatrix(adjMatrix, V))

# This code is contributed by rutvik_56
