import numpy.linalg

def gradient_descent(f, f_grad, cur_arg, step_calculation_method, eps = 1e-4):
  gradient_trace = [cur_arg]
  while True:
    cur_grad = f_grad(cur_arg)
    gradient_step = step_calculation_method(f, cur_grad, cur_arg)
    cur_arg -= cur_grad * gradient_step
    gradient_trace.append(cur_arg)

    if (numpy.linalg.norm(cur_grad) < eps):
      return gradient_trace

def linear_search(f, left, delta = 1e-2, eps = 1e-3, factor = 2):
  start_value = f(left)
  cur_delta = delta
  right = left + cur_delta
  while f(right) <= start_value + eps:
    cur_delta *= 2
    right += cur_delta

  return right