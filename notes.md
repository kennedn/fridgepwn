```goat


 VCC OUT  DS
  |   |   |
  |   |   |
.-+---+---+---.
| |   |   |   |
| * * * * * * |
|   |   |   | |
'---+---+---+-'  
    |   |   |
    |   |   |
   GND ??? SHCP
```

| PIN   | DESC                        |
|-------|-----------------------------|
| VCC   | Power, 5v                   |
| GND   | Ground                      |
| OUT   | Button or hall sensor       |
| OE    | Output enable               |
| DS    | Serial data in              |
| SHCP  | Shift register clock input  |

> Data latched on the 74HC595D selects which button / hall sensor is currently wired up to OUT
