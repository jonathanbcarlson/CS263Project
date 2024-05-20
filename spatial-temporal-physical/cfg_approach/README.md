# Spatial temporal physical prompts using a CFG

- Inspired by SPARTQA-AUTO (CFG) and TIMEDIAL distance
- Mad libs random combinations from CFG, fill in the blank.
- Different modes of transportation (physical) and different durations
  (temporal) and different distances (spatial)
- Expansion of example Beach trip prompt below
  ```
  If I {transport_method_1} into the street and {days_layer} days later
  I find myself by the {destination} which is {distance} miles away.
  How could I have gotten to the {destination}?
  1. I {transport_method_2} for {duration_1}.
  2. I {transport_method_3} for {duration_2}.
  Please choose the most likely answer and only respond with the number 1 or 2.
  ```
