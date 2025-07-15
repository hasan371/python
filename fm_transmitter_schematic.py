#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولد شماتیک فرستنده FM
FM Transmitter Schematic Generator
"""

import schemdraw
import schemdraw.elements as elm
from schemdraw import dsp

def create_fm_transmitter_schematic():
    """تولید شماتیک واقعی فرستنده FM"""
    
    # تنظیمات رسم
    d = schemdraw.Drawing()
    d.config(fontsize=12, font='Arial')
    
    # تغذیه +9V
    vcc = d.add(elm.Vdd().label('+9V', loc='top'))
    
    # مقاومت R1 (10kΩ)
    r1 = d.add(elm.Resistor().down().label('R1\n10kΩ', loc='left'))
    
    # نقطه اتصال بایاس
    bias_point = d.add(elm.Dot())
    
    # ترانزیستور BC547
    d.push()
    bjt = d.add(elm.BjtNpn(circle=True).anchor('base').label('Q1\nBC547', loc='right'))
    
    # مقاومت امیتر R2
    d.add(elm.Line().at(bjt.emitter).down(0.5))
    r2 = d.add(elm.Resistor().down().label('R2\n1kΩ', loc='right'))
    d.add(elm.Ground())
    
    # خازن کوپلینگ صوتی C1
    d.pop()
    d.add(elm.Line().left(1))
    c1 = d.add(elm.Capacitor().left().label('C1\n100nF', loc='top'))
    d.add(elm.Line().left(0.5))
    audio_in = d.add(elm.Gap().down().label(['Audio In', '(Mic/Line)'], loc='left'))
    d.add(elm.Ground())
    
    # سلف L1
    d.add(elm.Line().at(bjt.collector).up(0.5))
    l1 = d.add(elm.Inductor().up().label('L1\n10-15 turns\n5mm dia', loc='left'))
    
    # نقطه اتصال خروجی
    output_point = d.add(elm.Dot())
    
    # خازن متغیر C2
    d.push()
    d.add(elm.Line().right(1))
    c2 = d.add(elm.Capacitor(variable=True).down().label('C2\n10-40pF\nVariable', loc='right'))
    d.add(elm.Ground())
    
    # آنتن
    d.pop()
    d.add(elm.Line().right(2))
    antenna = d.add(elm.Antenna().label('Antenna\n20-30cm', loc='top'))
    
    # برچسب‌های اضافی
    d.add(elm.Label().at((4, 3)).label('FM Transmitter Circuit\nمدار فرستنده FM', fontsize=14))
    
    return d

def create_component_table():
    """جدول قطعات"""
    
    d = schemdraw.Drawing()
    
    # عنوان
    d.add(elm.Label().at((0, 5)).label('Parts List - لیست قطعات', fontsize=16))
    
    # جدول قطعات
    components = [
        'Q1: BC547 or 2N3904 (NPN Transistor)',
        'R1: 10kΩ (Bias Resistor)',
        'R2: 1kΩ (Emitter Resistor)',
        'C1: 100nF (Audio Coupling Capacitor)',
        'C2: 10-40pF Variable (Frequency Tuning)',
        'L1: 10-15 turns, 0.5mm wire, 5mm diameter',
        'Antenna: 20-30cm telescopic or wire',
        'Power Supply: 6-12V DC'
    ]
    
    y_pos = 4
    for i, component in enumerate(components):
        d.add(elm.Label().at((0, y_pos - i*0.5)).label(component, fontsize=10))
    
    return d

def main():
    """تابع اصلی"""
    
    print("تولید شماتیک فرستنده FM...")
    print("Generating FM Transmitter Schematic...")
    
    # تولید شماتیک اصلی
    schematic = create_fm_transmitter_schematic()
    schematic.save('fm_transmitter_schematic.svg')
    schematic.save('fm_transmitter_schematic.png', dpi=300)
    
    # تولید جدول قطعات
    parts_table = create_component_table()
    parts_table.save('fm_transmitter_parts.svg')
    parts_table.save('fm_transmitter_parts.png', dpi=300)
    
    print("✅ فایل‌های تولید شده:")
    print("✅ Generated files:")
    print("  - fm_transmitter_schematic.svg")
    print("  - fm_transmitter_schematic.png")
    print("  - fm_transmitter_parts.svg")
    print("  - fm_transmitter_parts.png")
    
    return schematic

if __name__ == "__main__":
    main()