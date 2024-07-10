---
title: "Fridgepwn"
date: 2024-07-10T09:43:48+01:00
draft: true
---
<table style="width:100%; margin-left: auto; margin-right: auto">
<tr><td style="width:30%; padding: 1px;">

```goat
     OUT
 VCC LAT  DS
  |   |   |
  |   |   |
.-+---+---+---.
| |   |   |   |
| * * * * * * |
|   |   |   | |
'---+---+---+-'  
    |   |   |
    |   |   |
   GND  OE CLK
```
</td>
<td style="width:70%; padding: 1px;"></td></tr>
</table>

| PIN        | DESC                                      |
|------------|-------------------------------------------|
| VCC        | Power, 5v                                 |
| GND        | Ground                                    |
| OUT/LAT    | Dual purpose, read: output, write: latch  |
| OE         | Output enable                             |
| DS         | Serial data in                            |
| CLK        | Clock input                               |

> Data latched on 74HC595D parallel outputs selects which button / hall sensor is currently wired up to OUT

<table style="width:100%; margin-left: auto; margin-right: auto">
<tr><td style="width:30%; padding: 1px;">

```goat
                           ^ 5v
                           |
                    .------+
                    |      |
                   .-.     |
              4.7k | |     |
.-+   +-.          '-'   | .
+  '-'  +  1k ___   |    |/
+    Qx +----|___|--+----+
+       +                |\
+       +                | +-----.
+       +                  |     |
+       +                  v    .-.
+       +            /    ---   | |47k
'-------'           /      |    '-'    
 74hc595d      .---+  *----'     | 
               |                 | GND
               |               -----
               | OUT            ---
               o
 ```
</td>
<td style="width:70%; padding: 1px;"></td></tr>
</table>


| BIT (1<<x) | BUTTON                                    |
|------------|-------------------------------------------|
| 11         | Hall sensor                               |
| 12         | Alarm off                                 |
| 13         | Quick                                     |
| 14         | Set                                       |
| 15         | On/Off                                    |