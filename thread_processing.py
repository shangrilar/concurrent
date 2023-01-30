import time
import concurrent.futures

def do_first_thing(job_id):
  print(f"do first thing: {job_id}")

def do_second_thing(job_id):
  print(f"do second thing: {job_id}")

def do_multiple_things(job_id):
  do_first_thing(job_id) # 1번 작업
  time.sleep(10)
  do_second_thing(job_id) # 2번 작업

def do_heavy_thing(job_id):
  print(f"do heavy thing: {job_id}")
  nums = []
  for i in range(10000000):
    nums.append(i)

if __name__ == '__main__':
    start=time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        job_ids = [2, 1, 3, 5, 4]
        results = [executor.submit(do_heavy_thing, job_id) for job_id in job_ids]

        for f in concurrent.futures.as_completed(results):
            f.result()
    end=time.time()
    print(f"실행시간: {end-start}")
