def tower_of_hanoi(n, source, auxiliary, destination):
    """
    Solves the Tower of Hanoi puzzle for n disks.

    Args:
        n (int): The number of disks.
        source (str): The name of the source peg.
        auxiliary (str): The name of the auxiliary peg.
        destination (str): The name of the destination peg.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    num_disks = 3
    source_peg = "A"
    auxiliary_peg = "B"
    destination_peg = "C"

    print(f"Solving Tower of Hanoi for {num_disks} disks:")
    tower_of_hanoi(num_disks, source_peg, auxiliary_peg, destination_peg)