#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولد شماتیک ساده فرستنده FM
Simple FM Transmitter Schematic Generator
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import numpy as np

def create_simple_fm_schematic():
    """تولید شماتیک ساده فرستنده FM"""
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # حذف محورها
    ax.axis('off')
    
    # عنوان
    ax.text(6, 7.5, 'Simple FM Transmitter Circuit\nمدار ساده فرستنده FM', 
            ha='center', va='center', fontsize=14, fontweight='bold')
    
    # تغذیه +9V
    ax.text(2, 6.5, '+9V', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.plot([2, 2], [6.3, 6], 'k-', linewidth=2)
    
    # مقاومت R1 (10kΩ)
    r1_box = Rectangle((1.7, 5.5), 0.6, 0.4, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(r1_box)
    ax.text(2, 5.7, 'R1\n10kΩ', ha='center', va='center', fontsize=8)
    ax.plot([2, 2], [6, 5.9], 'k-', linewidth=1)
    ax.plot([2, 2], [5.5, 5.2], 'k-', linewidth=1)
    
    # ترانزیستور BC547
    # دایره ترانزیستور
    transistor = Circle((4, 4), 0.4, linewidth=2, edgecolor='black', facecolor='white')
    ax.add_patch(transistor)
    ax.text(4.8, 4, 'Q1\nBC547', ha='left', va='center', fontsize=8)
    
    # پایه‌های ترانزیستور
    # Base
    ax.plot([2, 3.6], [5.2, 4], 'k-', linewidth=1)
    ax.plot([3.6, 3.6], [4, 4], 'k-', linewidth=2)
    
    # Emitter (با پیکان)
    ax.plot([4, 4], [3.6, 3], 'k-', linewidth=1)
    # پیکان emitter
    ax.plot([3.9, 4, 4.1], [3.3, 3.1, 3.3], 'k-', linewidth=1)
    
    # Collector
    ax.plot([4, 4], [4.4, 5.5], 'k-', linewidth=1)
    
    # مقاومت R2 (1kΩ)
    r2_box = Rectangle((3.7, 2.3), 0.6, 0.4, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(r2_box)
    ax.text(4, 2.5, 'R2\n1kΩ', ha='center', va='center', fontsize=8)
    ax.plot([4, 4], [3, 2.7], 'k-', linewidth=1)
    ax.plot([4, 4], [2.3, 2], 'k-', linewidth=1)
    
    # زمین (Ground)
    ax.plot([4, 4], [2, 1.8], 'k-', linewidth=1)
    for i in range(3):
        ax.plot([3.7 + i*0.15, 4.3 - i*0.15], [1.8 - i*0.1, 1.8 - i*0.1], 'k-', linewidth=1)
    
    # خازن C1 (100nF)
    ax.plot([1, 2], [5.2, 5.2], 'k-', linewidth=1)
    # خازن
    ax.plot([1.3, 1.3], [5.4, 5], 'k-', linewidth=2)
    ax.plot([1.5, 1.5], [5.4, 5], 'k-', linewidth=2)
    ax.text(1.4, 5.8, 'C1\n100nF', ha='center', va='center', fontsize=8)
    
    # ورودی صوتی
    ax.plot([0.5, 1.3], [5.2, 5.2], 'k-', linewidth=1)
    ax.text(0.3, 5.2, 'Audio In\n(Mic/Line)', ha='right', va='center', fontsize=8)
    ax.plot([0.5, 0.5], [5.2, 4.5], 'k-', linewidth=1)
    ax.plot([0.35, 0.65], [4.5, 4.5], 'k-', linewidth=1)
    
    # سلف L1
    coil_x = np.linspace(4, 4, 10)
    coil_y = np.linspace(5.5, 6.5, 10)
    for i in range(4):
        center = 5.75 + i*0.2
        circle = Circle((4, center), 0.08, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(circle)
    ax.text(3.2, 6, 'L1\n10-15 turns\n5mm dia', ha='center', va='center', fontsize=8)
    
    # خازن متغیر C2
    ax.plot([6, 4], [6.5, 6.5], 'k-', linewidth=1)
    ax.plot([6, 6], [6.5, 5.5], 'k-', linewidth=1)
    # خازن متغیر
    ax.plot([5.7, 5.7], [5.7, 5.3], 'k-', linewidth=2)
    ax.plot([6.3, 6.3], [5.7, 5.3], 'k-', linewidth=2)
    # پیکان متغیر
    ax.plot([5.5, 6.5], [5.8, 5.2], 'k-', linewidth=1)
    ax.plot([6.3, 6.5, 6.3], [5.4, 5.2, 5.0], 'k-', linewidth=1)
    ax.text(6.8, 5.5, 'C2\n10-40pF\nVariable', ha='left', va='center', fontsize=8)
    ax.plot([6, 6], [5.3, 4.8], 'k-', linewidth=1)
    
    # زمین C2
    ax.plot([6, 6], [4.8, 4.6], 'k-', linewidth=1)
    for i in range(3):
        ax.plot([5.7 + i*0.15, 6.3 - i*0.15], [4.6 - i*0.1, 4.6 - i*0.1], 'k-', linewidth=1)
    
    # آنتن
    ax.plot([8, 6], [6.5, 6.5], 'k-', linewidth=1)
    # آنتن خطی
    ax.plot([8, 8], [6.5, 7.2], 'k-', linewidth=2)
    ax.plot([7.8, 8.2], [7.2, 7.2], 'k-', linewidth=2)
    ax.plot([7.9, 8.1], [7.1, 7.1], 'k-', linewidth=1)
    ax.plot([8, 8], [7, 7], 'ko', markersize=3)
    ax.text(8.5, 6.8, 'Antenna\n20-30cm', ha='left', va='center', fontsize=8)
    
    # جدول قطعات
    parts_text = """Parts List - لیست قطعات:
Q1: BC547 or 2N3904 (NPN Transistor)
R1: 10kΩ (Bias Resistor)  
R2: 1kΩ (Emitter Resistor)
C1: 100nF (Audio Coupling)
C2: 10-40pF Variable (Tuning)
L1: 10-15 turns, 0.5mm wire
Antenna: 20-30cm wire
Power: 6-12V DC"""
    
    ax.text(10, 3, parts_text, ha='left', va='top', fontsize=8, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.5))
    
    plt.tight_layout()
    return fig

def main():
    """تابع اصلی"""
    
    print("تولید شماتیک ساده فرستنده FM...")
    print("Generating Simple FM Transmitter Schematic...")
    
    # تولید شماتیک
    fig = create_simple_fm_schematic()
    
    # ذخیره فایل‌ها
    fig.savefig('simple_fm_schematic.png', dpi=300, bbox_inches='tight')
    fig.savefig('simple_fm_schematic.svg', format='svg', bbox_inches='tight')
    
    print("✅ فایل‌های تولید شده:")
    print("✅ Generated files:")
    print("  - simple_fm_schematic.png")
    print("  - simple_fm_schematic.svg")
    
    plt.show()

if __name__ == "__main__":
    main()