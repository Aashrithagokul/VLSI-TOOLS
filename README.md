1. Ensure the Multisim tool is installed on your system.
2. Design the schematic diagram of your circuit in Multisim, and simulate it.
3. Export the netlist file from Multisim. This file will automatically open in the PSPICE tool from Cadence.
4. Provide the generated netlist file as an input to the Python code.
5. Enter the setup and hold time values as input in the code. Additionally, you can modify the default clock frequency and clock-to-Q delay values in the designated section of the code to suit your research needs.
6. Execute the Python code to read the netlist file and generate the required information for static timing analysis.
7. The tool will calculate setup and hold times, identify violations, and suggest fixes.


Refer to the doc(TOOL_DESCRIPTION.docx) for more details on the tool 
