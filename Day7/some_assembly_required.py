#!C:\python27
#--- Day 7: Some Assembly Required ---
#http://adventofcode.com/day/7

import sys, re

bitwise_dict = {'AND': '&', 'OR': '|', 'LSHIFT': '<<', 'RSHIFT': '>>', 'NOT': '~'}

def main(instructions):
    circuit = connect_wires(instructions)
    print 'The signal provided to wire "a" is {}'.format(circuit['a'] & 0xffff)

    instructions = override_b(instructions, circuit['a'])
    circuit = connect_wires(instructions)
    print 'The signal provided to wire "a" with the new override is {}'.format(circuit['a'] & 0xffff)
    

def connect_wires(links):
    circuit_board = {}
    
    for link in links:
        signal, wire = link.split(' -> ')
        circuit_board[wire] = signal.split(' ')

    return calculate_signals(circuit_board)

def calculate_signals(board):
    signals = {}
    
    # Find Roots first
    roots = search_for_roots(board, 1)
    for root in roots:
        signals[root] = int(board[root][0])

    # Find Wires joined to Roots
    while len(signals) < len(board):
        rooted_wires = search_for_rooted_wires(board, roots)
        for wire in rooted_wires:
            if wire not in signals: # In case of previously found root
                if len(board[wire]) == 3:
                    arg1, gate, arg2 = board[wire]
                    
                    if is_int(arg1):
                        # Case 1 (1 AND x)
                        signal = eval('{}{}{}'.format(int(arg1), bitwise_dict[gate], signals[arg2]))
                    elif gate.endswith('SHIFT'):
                        # Case 2 (L/R SHIFTS)
                        signal = eval('{}{}{}'.format(signals[arg1], bitwise_dict[gate], int(arg2)))
                    else: # Default Case
                        signal = eval('{}{}{}'.format(signals[arg1], bitwise_dict[gate], signals[arg2]))
                elif len(board[wire]) == 2: # NOT statements
                    gate, arg1 = board[wire]
                    signal = eval('{}{}'.format(bitwise_dict[gate], signals[arg1]))
                else: # Direct copy
                    signal = signals[board[wire][0]]

                signals[wire] = signal
        roots = signals.keys()

    return signals
                
def search_for_roots(dic, l):
    keys = []
    for k, v in dic.items():
        if len(v) == l and is_int(v[0]):
            keys.append(k)
    return keys

def search_for_rooted_wires(dic, roots):
    keys = []
    for k, v in dic.items():
        fully_rooted = (len(v) == 3 and ((v[0] in roots and is_int(v[2])) or (is_int(v[0]) and v[2] in roots) or (v[0] in roots and v[2] in roots))) or (len(v) == 2 and v[1] in roots) or (len(v) == 1 and v[0] in roots)
        if fully_rooted:
            keys.append(k)
    return keys

def override_b(instructions, new_value):
    for line in instructions:
        match = re.search('(\d+) -> b$', line)
        if match:
            instructions[instructions.index(line)] = '{} -> b'.format(new_value)
    return instructions
    

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: some_assembly_required.py <filename> <wire>'
    else:
        with open(sys.argv[1], 'r') as f:
            instructions = [line.strip() for line in f.readlines()]

        main(instructions)

