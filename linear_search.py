def linear_search(f, left, delta = 1e-2, eps = 1e-3, factor = 2):
  start_value = f(left)
  cur_delta = delta
  right = left + cur_delta
  while f(right) <= start_value + eps:
    cur_delta *= 2
    right += cur_delta

  return right