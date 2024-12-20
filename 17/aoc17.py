import re

def parse_ints(s):
    return list(map(int, re.findall(r'-?\d+', s)))

input = open('input', 'r').read().strip()

registers, program = input.split('\n\n')
registers = [parse_ints(l)[0] for l in registers.split('\n')]
program = parse_ints(program)

def combo(o, state):
    ra, rb, rc = state
    match o:
        case 4:
            return ra
        case 5:
            return rb
        case 6:
            return rc
        case _:
            return o

def run(registers, program):
    ra, rb, rc = registers
    ip = 0
    out = []
    while ip < len(program):
        opcode = program[ip]
        jmp = False
        match opcode:
            case 0: # adv
                ra = ra >> combo(program[ip+1], (ra, rb, rc))
            case 1: # bxl
                rb = rb ^ program[ip+1]
            case 2: # bst
                rb = combo(program[ip+1], (ra, rb, rc)) & 7
            case 3: # jnz
                if ra != 0:
                    ip = program[ip+1]
                    jmp = True
            case 4: # bxc
                rb = rb ^ rc
            case 5: # out
                out.append(combo(program[ip+1], (ra, rb, rc))%8)
            case 6: # bdv
                rb =ra >> combo(program[ip + 1], (ra, rb, rc))
            case 7: # cdv
                rc = ra >> combo(program[ip + 1], (ra, rb, rc))
        if not jmp:
            ip += 2
    return out


def dissasemble(program):
    ip = 0
    while ip < len(program):
        opcode = program[ip]
        match opcode:
            case 0:
                print("adv", program[ip+1])
            case 1:
                print("bxl", program[ip+1])
            case 2:
                print("bst", program[ip+1])
            case 3:
                print("jnz", program[ip+1])
            case 4:
                print("bxc", program[ip+1])
            case 5:
                print("out", program[ip+1])
            case 6:
                print("bdv", program[ip+1])
            case 7:
                print("cdv", program[ip + 1])
        ip += 2


out = run(registers, program)
print(",".join(map(str,out)))

# we can build up by octal digits
# later outputs ~ higher order digits
def part2(program, prefix, match_to):
    for i in range(8):
        candidate = prefix * 8 + i
        if run((candidate, 0, 0), program) == program[match_to:]:
            if match_to == 0:
                return candidate
            else:
                res =  part2(program, candidate, match_to-1)
                if res is not None:
                    return res
    return None

p2 = part2(program, 0, len(program)-1)
print(p2)