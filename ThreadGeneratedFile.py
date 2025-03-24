import os
import threading

# 配置参数
file_size = 1 * (1024**2)    # 文件大小，单位为字节，当前为 1MB
number_of_files = 4_000_000  #生成文件的个数,根据需要修改,当前为 4000 万个文件

num_threads = 32    # 线程数量
files_per_thread = number_of_files // num_threads    # 每个线程处理的文件数量

def generate_file(thread_id):    # 生成文件
    start = thread_id * files_per_thread    # 计算文件编号范围
    end = (thread_id + 1) * files_per_thread    # 计算文件编号范围
    for i in range(start, end):     # 生成文件
        filename = f"{i}.bin"    # 生成文件名 bin可以修改成其他格式,无伤大雅
        if not os.path.exists(filename):    # 判断文件是否存在
            with open(filename, "wb") as f: # 生成文件
                f.write(os.urandom(file_size))  # 生成文件内容

threads = []
for i in range(num_threads):    # 创建线程
    t = threading.Thread(target=generate_file, args=(i,))
    threads.append(t)

for t in threads:    # 启动线程
    t.start()

for t in threads:    # 等待线程结束
    t.join()