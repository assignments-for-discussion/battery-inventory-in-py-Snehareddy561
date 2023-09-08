
def count_batteries_by_health(present_capacities):
  counts = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  
for capacity in present_capacities:
  if capacity>=100:
    counts["health"]+=1
  elif 80<=capacity<100:
    counts["exchange"]+=1
  else:
    counts["failed"]+=1
return counts
  

def test_bucketing_by_health():
  print("Counting batteries by health...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")

if_name_=='__main__':
  test_bucketing_by_health()



