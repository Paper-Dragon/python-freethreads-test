import time
import threading

def cpu_intensive_task(iterations):
    """CPU密集型任务 - 用于测试GIL影响"""
    total = 0
    for i in range(iterations):
        total += i * 2
    return total

def single_thread_test(total_iterations):
    """单线程测试"""
    start_time = time.perf_counter()
    cpu_intensive_task(total_iterations)
    return time.perf_counter() - start_time

def multi_thread_test(total_iterations, thread_count):
    """多线程测试（受GIL限制）"""
    start_time = time.perf_counter()
    iterations_per_thread = total_iterations // thread_count
    
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(
            target=cpu_intensive_task, 
            args=(iterations_per_thread,)
        )
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return time.perf_counter() - start_time

def main():
    total_iterations = 100_000_000
    thread_counts = [1, 2, 4, 8]
    
    print(f"迭代次数: {total_iterations:,}")
    
    for threads in thread_counts:
        time_taken = single_thread_test(total_iterations) if threads == 1 else multi_thread_test(total_iterations, threads)
        print(f"{threads}线程: {time_taken:.3f}s")

if __name__ == "__main__":
    main()