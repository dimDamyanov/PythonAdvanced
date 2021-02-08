import traceback


def raise_exception(exception_type):
    raise exception_type()


try:
    raise_exception(IndexError)
# except (TypeError, ValueError):
#     print('TypeError or ValueError')
except TypeError:
    print('Handled with TypeError')
except ValueError:
    print('Handled with ValueError')
except IndexError as e:
    print(f'Handled with Exception')
    traceback.print_tb(e.__traceback__)
# except:
#     print('Handled in except')

print('It still works')