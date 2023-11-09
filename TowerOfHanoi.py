def TowerOfHanoi(Disks, source, temp, destination):  
    if (Disks == 1):  
        print(f"Move Disk 1 From {source} to {destination}")
        return
    TowerOfHanoi(Disks - 1, source, destination, temp)
    print(f"Move Disk {Disks} From {source} to {destination}")
    TowerOfHanoi(Disks - 1, temp, source, destination)  
  
Disks = int(input("Enter Number of Disks: "))

# Source : A, Intermediate : B, Destination : C  
TowerOfHanoi(Disks, 'A', 'B', 'C')