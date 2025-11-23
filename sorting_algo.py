import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# ----------------------------------------------
# Bubble Sort 
# ----------------------------------------------
def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data.copy()

# ----------------------------------------------
# Selection Sort 
# ----------------------------------------------
def selection_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if data[j] < data[min_i]:
                min_i = j
        data[i], data[min_i] = data[min_i], data[i]
        yield data.copy()

# ----------------------------------------------
# Side-by-Side Animation
# ----------------------------------------------
def animate_comparison():
    arr = random.sample(range(10, 100), 40)  # 40 random numbers

    bubble_gen = bubble_sort(arr.copy())
    selection_gen = selection_sort(arr.copy())

    # Create 2 charts side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    fig.suptitle("Bubble Sort vs Selection Sort - Side-by-Side Animation", fontsize=14)

    # Bubble plot setup
    ax1.set_title("Bubble Sort")
    ax1.set_ylim(0, max(arr) + 10)
    bars1 = ax1.bar(range(len(arr)), arr)

    # Selection plot setup
    ax2.set_title("Selection Sort")
    ax2.set_ylim(0, max(arr) + 10)
    bars2 = ax2.bar(range(len(arr)), arr)

    # Step counters
    iter1 = [0]
    iter2 = [0]

    t1 = ax1.text(0.02, 0.95, "", transform=ax1.transAxes)
    t2 = ax2.text(0.02, 0.95, "", transform=ax2.transAxes)

    # Final speed comparison text (to appear below both graphs)
    speed_text = fig.text(0.5, 0.02, "", ha="center", fontsize=12, color="blue")

    bubble_done = [False]
    selection_done = [False]

    def update(frame):
        # Bubble Sort update
        if not bubble_done[0]:
            try:
                new_vals1 = next(bubble_gen)
                for rect, val in zip(bars1, new_vals1):
                    rect.set_height(val)
                iter1[0] += 1
                t1.set_text(f"Steps: {iter1[0]}")
            except StopIteration:
                bubble_done[0] = True

        # Selection Sort update
        if not selection_done[0]:
            try:
                new_vals2 = next(selection_gen)
                for rect, val in zip(bars2, new_vals2):
                    rect.set_height(val)
                iter2[0] += 1
                t2.set_text(f"Steps: {iter2[0]}")
            except StopIteration:
                selection_done[0] = True

        # Show fastest algorithm (only once both finish)
        if bubble_done[0] and selection_done[0]:
            if iter1[0] < iter2[0]:
                msg = f"Bubble Sort is Faster ({iter1[0]} steps < {iter2[0]} steps)"
            else:
                msg = f"Selection Sort is Faster ({iter2[0]} steps < {iter1[0]} steps)"

            speed_text.set_text(msg)

    # Animation
    anim = animation.FuncAnimation(
        fig, update, frames=2000, interval=40, repeat=False
    )

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()

# ----------------------------------------------
# Run Program
# ----------------------------------------------
if __name__ == "__main__":
    animate_comparison()
