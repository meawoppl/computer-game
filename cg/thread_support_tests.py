import concurrent.futures
import uuid

import nose.tools

import cg.thread_support


def get_uuid_pairer():
    return cg.thread_support.ThreadPairer(lambda: str(uuid.uuid4()))


def test_thread_pairer_timeout():
    tp = get_uuid_pairer()

    with nose.tools.assert_raises(TimeoutError):
        tp.get_paired_instance(100)


def test_thread_pairer_pair():
    tp = get_uuid_pairer()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as tpe:
        f1 = tpe.submit(tp.get_paired_instance)
        f2 = tpe.submit(tp.get_paired_instance)

        r1 = f1.result()
        r2 = f2.result()

        nose.tools.assert_equal(r1, r2)

        f3 = tpe.submit(tp.get_paired_instance)

        with nose.tools.assert_raises(TimeoutError):
            f3.result()


def test_thread_pair_pairer_hard():
    tp = get_uuid_pairer()

    futs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as tpe:
        for x in range(100):
            futs.append(tpe.submit(tp.get_paired_instance))
            futs.append(tpe.submit(tp.get_paired_instance))

        results = [f.result() for f in futs]

    for element in results:
        assert results.count(element) == 2
