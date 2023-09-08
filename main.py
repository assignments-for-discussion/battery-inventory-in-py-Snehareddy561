
def count_batteries_by_health(present_capacities):
  counts = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  rated_capacity=120
  
for i in present_capacities:
  soh=100*i / rated_capacity
  if soh > 80:
    counts["healthy"] +=1
  elif 65 <= soh <= 80:
    counts["exchange"] +=1
  else:
    counts["failed"]+=1
return counts
  

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")

if_name_=='__main__':
  test_bucketing_by_health()


if __name__ == '__main__':
  test_bucketing_by_health()
