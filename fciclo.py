

def calculate_case(instructions):
    counter = 0
    for inst in instructions:
        if inst == "NULL":
            counter += 1
    return counter


def set_function(position, value, memory):
    memory[position] = value





def sub_function(value, instructions, accum_register, memory):
    if calculate_case(instructions) == 2:
        memory['accumRegister'] -= value

    elif calculate_case(instructions) == 1:
        memory['accumRegister'] -= value
        pos = int(instructions[2][1])
        memory[pos] += memory['accumRegister']

    elif calculate_case(instructions) == 0:
        memory['accumRegister'] -= value
        pos = int(instructions[2][1])
        memory[pos] += memory['accumRegister']
        memory['accumRegister'] = memory[pos]
        pos = int(instructions[3][1])
        memory[pos] += memory['accumRegister']

def sum_function(value, instructions, memory, accum_register):
    if calculate_case(instructions) == 2:
        memory['accumRegister'] += value

    elif calculate_case(instructions) == 1:
        memory['accumRegister'] += value
        pos = int(instructions[2][1])
        memory[pos] += memory['accumRegister']

    elif calculate_case(instructions) == 0:
        memory['accumRegister'] += value
        pos = int(instructions[2][1])
        memory[pos] += memory['accumRegister']
        memory['accumRegister'] = memory[pos]
        pos = int(instructions[3][1])
        memory[pos] += memory['accumRegister']
      
def mult_function(value, instructions, accum_register, memory):
    if calculate_case(instructions) == 2:
        memory['accumRegister'] *= value

    elif calculate_case(instructions) == 1:
        memory['accumRegister'] *= value
        pos = int(instructions[2][1])
        memory[pos] *= memory['accumRegister']

    elif calculate_case(instructions) == 0:
        memory['accumRegister'] *= value
        pos = int(instructions[2][1])
        memory[pos] *= memory['accumRegister']
        memory['accumRegister'] = memory[pos]
        pos = int(instructions[3][1])
        memory[pos] *= memory['accumRegister']
      
def move_function(memory, instructions):
    pos = int(instructions[1][1])
    aux = memory[pos]
    memory[pos] = 'D' + str(pos)
    pos = int(instructions[2][1])
    memory[pos] = aux

def div_function(value, instructions, accum_register, memory):
    if calculate_case(instructions) == 2:
        memory['accumRegister'] *= value

    elif calculate_case(instructions) == 1:
        memory['accumRegister'] *= value
        pos = int(instructions[2][1])
        memory[pos] *= memory['accumRegister']

    elif calculate_case(instructions) == 0:
        memory['accumRegister'] *= value
        pos = int(instructions[2][1])
        memory[pos] *= memory['accumRegister']
        memory['accumRegister'] = memory[pos]
        pos = int(instructions[3][1])
        memory[pos] *= memory['accumRegister']


def inc_function(memory, position):
    memory[position] += 1

def show_function(memory, position):
    print(memory[position])


def dec_function(memory, position):
    memory[position] -= 1

def beq_function(memory, position):
    if memory[position] - memory['accumRegister'] == 0:
        pass


def load_function(memory, position):
    memory['accumRegister'] = memory[position]


def store_function(memory, position):
    memory[position] = memory['accumRegister']






