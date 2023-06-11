import unittest
import time

from timeitpoj.timer.internal_timer import InternalTimer
from timeitpoj.timer.timer import Timer


class TimerTests(unittest.TestCase):
    def test_timer_without_parent(self):
        internal_timer = InternalTimer()
        with Timer("Test Timer", internal_timer=internal_timer) as timer:
            time.sleep(1)

        self.assertAlmostEqual(timer.elapsed_time, 1, places=1)

    def test_timer_with_parent(self):
        internal_timer = InternalTimer()
        with Timer("Parent Timer", internal_timer=internal_timer) as parent_timer:
            time.sleep(1)
            with parent_timer("Child Timer 1") as child_timer1:
                time.sleep(2)

            with parent_timer("Child Timer 2") as child_timer2:
                time.sleep(3)

        self.assertAlmostEqual(parent_timer.elapsed_time, 6, places=1)
        self.assertAlmostEqual(child_timer1.elapsed_time, 2, places=1)
        self.assertAlmostEqual(child_timer2.elapsed_time, 3, places=1)


if __name__ == '__main__':
    unittest.main()
