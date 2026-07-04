from multiprocessing import Process
import time

def brew_chai(chai_name):
    print(f"Brewing {chai_name}...")
    time.sleep(5)
    print(f"{chai_name} is ready!")

# This block is mandatory on Windows to prevent infinite process loops
if __name__ == '__main__':
    processes = []
    chai_names = ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai", "Elaichi Chai"]
    
    for chai in chai_names:
        process = Process(target=brew_chai, args=(chai,))
        processes.append(process)
            
    for process in processes:
        process.start()
            
    for process in processes:
        process.join()
            
    print("All chai are ready!")
