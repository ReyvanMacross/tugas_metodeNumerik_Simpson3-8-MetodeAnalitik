import numpy as np
import sympy as sp
from tabulate import tabulate

# === Metode Simpson 3/8 ===

def f(x):
    return x * np.sqrt(3 * x + 4)

a = -1
b = 4
n = 6  # kelipatan 3
h = (b - a) / n
x_vals = [a + i * h for i in range(n + 1)]
fx_vals = [f(x) for x in x_vals]

rows = []
integral_sum = 0
for i in range(n + 1):
    xi = x_vals[i]
    fxi = fx_vals[i]
    if i == 0 or i == n:
        coef = 1
    elif i % 3 == 0:
        coef = 2
    else:
        coef = 3
    weighted = coef * fxi
    integral_sum += weighted
    rows.append([i, f"{xi:.4f}", f"{fxi:.4f}", coef, f"{weighted:.4f}"])

hasil_simpson = (3 * h / 8) * integral_sum

# === Metode Analitik ===

x, u = sp.symbols('x u')
f_x = x * sp.sqrt(3 * x + 4)

# Substitusi
u_expr = 3*x + 4
x_expr = (u - 4)/3
dx_expr = 1/3

# Ubah batas
u_lower = 3 * a + 4  # x = -1
u_upper = 3 * b + 4  # x = 4

# Ganti fungsi dalam u
integrand_u = (1/9) * (u - 4) * sp.sqrt(u)
I_analitik = sp.integrate(integrand_u, (u, u_lower, u_upper))
hasil_analitik = float(I_analitik)

# === Perbandingan ===
selisih = abs(hasil_simpson - hasil_analitik)
error_persen = (selisih / hasil_analitik) * 100

# === OUTPUT ===

print("="*70)
print("Tugas E-Learning 2 Metode Numerik".center(70))
print("Nama 1 : Rievan Rivaldy Nur Triana   | NIM : 24552011030")
print("Nama 2 : Moch. Naufal Ar Karim       | NIM : 24552011014")
print("Kelas  : TIF RP 24 B")
print("="*70)

print("\nLANGKAH METODE SIMPSON 3/8:")
print(f"Batas bawah a = {a}")
print(f"Batas atas  b = {b}")
print(f"Jumlah subinterval n = {n}")
print(f"Lebar tiap subinterval h = {h:.4f}\n")

print(tabulate(rows, headers=["i", "xᵢ", "f(xᵢ)", "Koefisien", "Koefisien * f(xᵢ)"], tablefmt="grid"))

print(f"\nLangkah Akhir Simpson:")
print(f"Total penjumlahan = {integral_sum:.4f}")
print(f"Hasil Integral Simpson 3/8 = {hasil_simpson:.4f}")

# === LANGKAH ANALITIK ===

print("\n\nLANGKAH METODE ANALITIK (PENDEKATAN SIMBOLIK):")
print("Fungsi Asli:")
print("       4")
print("      ⌠ ")
print("      ⎮  x√(3x + 4) dx")
print("      ⌡")
print("     -1")

print("\nLangkah 1: Substitusi")
print("  u = 3x + 4   →   x = (u - 4)/3   →   dx = du/3")

print("\nLangkah 2: Ubah fungsi ke dalam u")
print("  f(u) = (1/9)(u - 4)√u")

print("\nLangkah 3: Ganti batas")
print(f"  x = -1 → u = {u_lower}")
print(f"  x =  4 → u = {u_upper}")

print(f"\nLangkah 4: Hitung integral (simbolik):")
print(f"  ∫ (1/9)(u - 4)√u du dari u = {u_lower} sampai u = {u_upper}")
print(f"  Hasil simbolik: {I_analitik}")
print(f"  Hasil desimal : {hasil_analitik:.4f}")

# === Perbandingan ===
print("\nPERBANDINGAN HASIL:")
print(f"Hasil Analitik          = {hasil_analitik:.4f}")
print(f"Hasil Simpson 3/8       = {hasil_simpson:.4f}")
print(f"Selisih                 = {selisih:.4f}")
print(f"Persentase Error        = {error_persen:.4f}%")
print("="*70)