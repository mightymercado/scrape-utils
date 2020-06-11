import os
import pickle
import time

def cache(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        no_cache = False
        if kwargs.get('no_cache') == True:
            no_cache = True
            del kwargs['no_cache']

        # encode filename
        cache_filename = func.__name__ + '-'
        # encode positional arguments
        cache_filename += ','.join([str(arg) for arg in args[1:]]) + '-'
        # encode keyword arguments
        cache_filename += ','.join([str(key)+'='+str(value) for key, value in sorted(kwargs.items())])
        # turn into a proper filename by removing forward slashes, etc
        cache_filename = cache_filename \
            .replace('/', '-')

        if len(cache_filename) > 255:
            cache_filename = cache_filename[:255]
            
        # load previous response

        if not os.path.exists('cache/'):
          os.mkdir('cache')
        if os.path.exists('cache/' + cache_filename) and not no_cache:
            with open('cache/' + cache_filename, 'rb') as f:
                return pickle.load(f)
        else:
            ret = func(*args, **kwargs)
            with open('cache/' + cache_filename, 'wb') as f:
                pickle.dump(ret, f)
                return ret  

    return wrapper
