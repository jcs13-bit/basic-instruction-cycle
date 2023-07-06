from io import open
from fciclo import *

''' Clase (Ciclo)
se define la memoria como un diccionario de datos que tiene como claves(keys) el número de la posición de la memoria
'''
class Cycle():
    def __init__(self):
        self.program_counter = 0
        self.memory_address_register = 0
        self.memory_data_register = ''
        self.instruction_register = ''
        self.accumulator = 0
        self.is_finished = False
    def get_accumulator(self):
        return self.accumulator

    def show_memory_address_register(self):
        print(self.memory_address_register)
        return self.memory_address_register

    def show_memory_data_register(self):
        print(self.memory_data_register)
        return self.memory_data_register
      
    def show_instruction_register(self):
        print(self.instruction_register)
        return self.instruction_register

    def read_file(self):
        file = open("instrucciones.txt", "r")
        lines = file.readlines()
        file.close()
        return lines

    def read_instructions(self):
        lines = self.read_file()
        instructions = []
        for line in lines:
            if line:
                instructions.append(line.split())
        return instructions
    def define_memory(self):
      instructions = self.read_instructions()
      memory_addresses = []
      for instruction in instructions:
        if instruction[0] == 'SET':
          for word in instruction[1:]:
            if word.startswith('D'):
              memory_addresses.append(word)
      memory_addresses = list(set(memory_addresses))
      memory_addresses.sort(key=lambda x: int(x[1:]))
      memory_addresses.append('accumulator')
      memory_space = dict(zip(memory_addresses, range(len(memory_addresses))))
      return memory_space
      
    def execute_cycle(self):
      instructions = self.read_instructions()
      memory = self.define_memory()
      
      for i, instruction in enumerate(instructions):
        self.mdr = ''
        if (self.is_finished == True):
          print('Terminated')
          break
        self.pc = i + 1
        self.mar = self.pc
        for word in instruction:
          self.mdr += str(word) + ' '
        self.icr = self.mdr
        self.control_unit(memory, instruction, instruction[0])
    def control_unit(self, memory, instruction, function):
        self.accumulator = memory['accumulator']
        
        if function == 'END':
            self.terminated = True
        else:
            pos = instruction[1].replace('D', '')
        
        if function == 'SET':
            value = int(instruction[2])
            set_function(pos, value, memory)
            
        elif function == 'ADD':
            value = memory[pos]
            sum_function(value, instruction, memory, self.accumulator)
        elif function == 'SUB':
            value = memoria[pos]
            sub_function(value, instruction, self.acumulador, memory)
            
        elif function == 'MUL':
            value = memoria[pos]
            mult_function(value, instruction, self.acumulador, memory)
            
        elif function == 'DIV':
            value = memoria[pos]
            div_function(value, instruction, self.acumulador, memory)
            
        elif function == 'INC':
            inc_function(memory, pos)
            
        elif function == 'DEC':
            dec_function(memory, pos)
            
        elif function == 'MOV':
            move_function(memory, instruccion)
            
        elif function == 'LDR':
            load_function(memory, pos)
            
        elif function == 'STR':
            store_function(memory, pos)
            
        elif function == 'BEQ':
            beq_function(memory, pos)
            
        elif function == 'SHW':
            if instruction[1] == 'MAR':
                self.show_memory_address_register()
            elif instruction[1] == 'MDR':
                self.show_memory_data_register()
            elif instruction[1] == 'ICR':
                self.show_instruction_register()
            else:
                show_function(memory, pos)
                
        elif function == 'END':
            self.terminado = True
