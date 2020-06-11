from traceback import print_exc
import time 

def robustify(attempts: int, sleep: int):
  def decorator(call):
    def wrapper(*args, **kwargs):
      for attempt in range(1, attempts + 1):
        try:
          return call(*args, **kwargs)
        except:
          print('Attempt {}/{} of {}() failed'.format(attempt, attempts, call.__name__))
          print_exc()
          time.sleep(sleep)
      raise ValueError('Call to {} failed'.format(call.__name__))
    return wrapper
  return decorator
