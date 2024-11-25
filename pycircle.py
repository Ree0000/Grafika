import matplotlib.pyplot as plt

def draw_circle(xc, yc, x, y, titik):
    # kuadran
    titik.append((xc + x, yc + y))
    titik.append((xc - x, yc + y))
    titik.append((xc + x, yc - y))
    titik.append((xc - x, yc - y))
    titik.append((xc + y, yc + x))
    titik.append((xc - y, yc + x))
    titik.append((xc + y, yc - x))
    titik.append((xc - y, yc - x))

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r
    titik = []

    # algoritma
    while x <= y:
        draw_circle(xc, yc, x, y, titik)
        if p < 0:
            p += 4 * x + 6
        else:
            p += 4 * (x - y) + 10
            y -= 1
        x += 1

    return titik

def plot_circle(titik, xc, yc, r):
    x_coords, y_coords = zip(*titik)
    plt.scatter(x_coords, y_coords, c='red', s=10, label="Lingkaran")
    plt.axhline(y=0, color='black', linestyle='--', label="Sumbu X & Y")
    plt.axvline(x=0, color='black', linestyle='--')
    plt.gca().set_aspect('equal', adjustable='box')

    plt.legend()
    plt.title(f"Lingkaran Bresenham\n dengan titik pusat ({xc}, {yc}) dan Jari-jari {r}")
    plt.xlabel("Sumbu X")
    plt.ylabel("Sumbu Y")
    plt.gcf().canvas.manager.set_window_title("Implementasi Algoritma Lingkaran Bresenham")
    plt.show()

if __name__ == "__main__":
    xc, yc, r = 20, 20, 50 # titik pusat & jari-jari lingkaran
    titik = bresenham_circle(xc, yc, r)
    plot_circle(titik, xc, yc, r)
