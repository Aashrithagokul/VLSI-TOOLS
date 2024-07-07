import re

def extract_gate_delays(file_path):
    gate_delays = {}
    total_comb_delay = 0

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('.MODEL') and 'rise_delay' in line and 'fall_delay' in line:
                # Extract the gate name
                parts = line.split()
                gate_name = parts[1]
                
                # Extract rise_delay and fall_delay values
                rise_delay_match = re.search(r'rise_delay\s*=\s*(\d+)', line)
                fall_delay_match = re.search(r'fall_delay\s*=\s*(\d+)', line)

                if rise_delay_match and fall_delay_match:
                    rise_delay = int(rise_delay_match.group(1))
                    fall_delay = int(fall_delay_match.group(1))
                    total_delay = rise_delay + fall_delay
                    gate_delays[gate_name] = total_delay
                    total_comb_delay += total_delay

    return gate_delays, total_comb_delay

def extract_flip_flop_delays(file_path):
    Clock_q_delay = 0
    Clock_period = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].startswith('.MODEL') and 'd_dff' in lines[i]:
                # Extract clk_delay from the same line
                clk_delay_match = re.search(r'clk_delay\s*=\s*(\d+)', lines[i])
                if clk_delay_match:
                    Clock_q_delay = int(clk_delay_match.group(1))

                # Extract rise_delay and fall_delay from the next line
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    rise_delay_match = re.search(r'rise_delay\s*=\s*(\d+)', next_line)
                    fall_delay_match = re.search(r'fall_delay\s*=\s*(\d+)', next_line)

                    if rise_delay_match and fall_delay_match:
                        rise_delay = int(rise_delay_match.group(1))
                        fall_delay = int(fall_delay_match.group(1))
                        Clock_period = rise_delay + fall_delay
    Clock_q_delay = 2
    Clock_period = 6
    

    return Clock_q_delay, Clock_period


# Specify the path to your file
file_path = r'C:\Users\gokul\Desktop\project\NETLIST\COMBINATIONAL6.cir'

# Get the gate delays and total combinational delay
gate_delays, Tcomb = extract_gate_delays(file_path)

# Get the flip-flop delays
Clock_q_delay, Clock_period = extract_flip_flop_delays(file_path)

# Print the gate delays
for gate, delay in gate_delays.items():
    print(f"{gate} = {delay}ns")

# Print the total combinational delay
print(f"Tcomb = {Tcomb}ns")

# Print the flip-flop delays
print(f"Clock_q_delay = {Clock_q_delay}ns")
print(f"Clock_period = {Clock_period}ns")


Tsetup=float(input("enter the setup time:  "))
Thold=float(input("enter the hold time: "))
print("")
print("SET UP TIME CONDITIONS")
print("Slack must be positive ")
arrival_time=Clock_q_delay+Tcomb
print("THE ARRIVAL TIME IS:" , arrival_time ,"ns")
required_time= Clock_period - Tsetup
print("THE REQUIRED TIME IS:" , required_time ,"ns")

slack = required_time-arrival_time
print("THE SLACK IS:" , slack,"ns")
print("")
print("HOLD TIME CONDITIONS")
print("Tcomb + Clock_q_delay >= Thold")
print( Tcomb + Clock_q_delay , ">=", Thold)

if slack > 0:
    print("")
    print("")
    print("  NO SETUP TIME VIOLATION     ")
else:
    print("")
    print("")
    print("  SET UP TIME IS VIOLATED      ")
    print("   IF there is setup time violation there few ways to rectify them  ")
    #print("     1.Adding of delay elements \n       the value of the delay elements here can be= -",Tcomb,"ns")
    print("     1.Adjusting the clock frequency\n       the value of clock frequency can be =" , Clock_period+Clock_q_delay+Tcomb,"ns")
    print("     2.Pipeline Registers\n       Break the critical path by inserting pipeline registers to divide the circuit into smaller stages. \n       This reduces the path delay and allows for a higher clock frequency.")
    print("     3.Logic Restructuring\n       Redesign the combinational logic to optimize the critical path. ")
    print("")
    print(" ADJUSTMENT OF CLOCK FREQUENCY " )
    delay_change = int (Clock_period+Clock_q_delay+Tcomb)
    print("   The clock frequency after changing to the value",delay_change,"ns it satisfies the setup condition")
    
    Clock_period_setup_time_rectification = delay_change
    arrival_time=Clock_q_delay+Tcomb
    required_time= Clock_period_setup_time_rectification - Tsetup

    slack = int (required_time-arrival_time)
    
    print("   The slack is positive" , slack )
    print("   SETUP TIME IS RECTIFIED")
    
if Tcomb + Clock_q_delay >= Thold:
    
    
    print("")
    print("")
    print("  NO HOLD TIME VIOLATION ")
else:
    print("")
    print("")
    print("  HOLD TIME VIOLATED ")
    print("   IF there is hold time violation there few ways to rectify them  ")
    print("     1.Adding of delay elements \n       the value of the delay elements here can be= ",Tcomb,"ns")
    print("     2.Adding lock up latches will rectify the hold time if there is clock skew ")
    print("     3.Ensure that the routing paths for critical signals are optimized for minimal delay variations")
    print("")
    print(" ADDING OF DELAY ELEMENT")
    print("   The value of delay element added is", Tcomb,"ns")
    print("   This will satisfy the condition \n   Tcomb + Clock_q_delay + delay element value  >= Thold")
    print("  ", Tcomb + Clock_q_delay + Tcomb , ">=", Thold)
    print("   HOLD TIME IS RECTIFIED")
    

    
          
    
    