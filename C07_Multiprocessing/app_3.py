import multiprocessing


class MyObject(multiprocessing.Process):

    def run(self):
        super().run()
        print('running')


def f(name, sleep):
    time.sleep(sleep)
    print('hello', name)


if __name__ == '__main__':
    p1 = MyObject(target=f, args=('lily', 2))
    p1.start()
    # p1.join()