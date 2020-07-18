total_cost = 0

cpu_count = int(input("cpu 개수는?"))
cpu_cost = int(input("cpu 가격은?"))
total_cost = total_cost + cpu_count*cpu_cost


board_count = int(input("메인보드 개수는?"))
board_cost = int(input("메인보드 가격은?"))
total_cost = total_cost + board_count*board_cost


memory_count = int(input("메모리 개수는?"))
memory_cost = int(input("메모리 가격은?"))
total_cost = total_cost + memory_count*memory_cost


disk_count = int(input("하드디스크 개수는?"))
disk_cost = int(input("하드디스크 가격은?"))
total_cost = total_cost + disk_count*disk_cost

print(total_cost)
