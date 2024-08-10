import time
print("Press ENTER to start the stopwatch")
print("and , Press CTRL+C to stop the stopwatch")
while True:
   try:
      input()
      start_time=time.time()
      print("stopwatch started..........!!!!!!!!!!!!!!!")
   except KeyboardInterrupt:
      print("Stopwatch stopped........!!!!!!!!!!!!!")
      end_time=time.time()
      print("The Total Time:",round(end_time - start_time,2),"seconds")
      break

   
